
def main(j,jp):
    gridid=j.application.config.getInt("gridmaster.grid.id")

    j.application.config.set("grid.id",gridid)
    j.application.config.set("grid.master.ip","127.0.0.1")

    #check osis installed
    if not j.system.net.tcpPortConnectionTest("127.0.0.1", 5544):
        j.tools.startupmanager.startProcess('jumpscale', 'elasticsearch')
        # j.tools.startupmanager.startProcess('jumpscale', 'osis')

    if j.application.config.get("grid.master.superadminpasswd") == "":
        passwdmd5 = j.tools.hash.md5_string(j.console.askString("Please provide: grid.master.superadminpasswd", regex="^(?!\s*$).+", retry=5))
        j.application.config.set("grid.master.superadminpasswd",passwdmd5) #on gridmaster we should remember
    passwdmd5 = j.application.config.get("grid.master.superadminpasswd")


    roles = j.application.config.getList("grid.node.roles")
    if "master" not in roles:
        roles.append("master")
        j.application.config.set("grid.node.roles",",".join(roles))


    redis=j.packages.findNewest(domain="jumpscale",name="redis")
    redis.start()

    j.tools.startupmanager.startProcess("jumpscale","osis")

    #register in osis
    import JumpScale.grid.osis
    client = j.core.osis.getClient(user="root",passwd=passwdmd5)
    client_grid=j.core.osis.getClientForCategory(client,"system","grid")

    gridobj = client_grid.new(name="grid_%s"%gridid,id=gridid)
    gridobj.initFromLocalNodeInfo()
    key, new, changed = client_grid.set(gridobj)


    j.tools.startupmanager.restartProcess('jumpscale', 'osis') #to make sure we have objects loaded from portal 

    #configure avahi
    if j.application.config.getBool("gridmaster.useavahi"):
        j.application.config.set("grid.useavahi",1)
        import JumpScale.baselib.remote.avahi
        j.remote.avahi.registerService("js_grid_%s"%gridid,5544)
    else:
        j.application.config.set("grid.useavahi",0)

    # needs to be done in this order after grid_master is registered
    j.tools.startupmanager.startProcess("jumpscale","agentcontroller")
    j.tools.startupmanager.startProcess("workers",None)
    jp = j.packages.findNewest(domain="jumpscale",name="processmanager")
    jp.install()
    jp.start()
