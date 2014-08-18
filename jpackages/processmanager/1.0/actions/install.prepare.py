def main(j,jp):
    redis=j.packages.findNewest("jumpscale","redis")
    instancename = 'production'
    if not redis.isInstalled(instancename):
        redis.install(hrddata={"redis.name":instancename,"redis.port":"7768","redis.disk":"1","redis.mem":400},instance=instancename)
    redis.start()

    acinstance = jp.hrd_instance.get('agentcontroller.connection')
    import JumpScale.grid.agentcontroller
    config = j.clients.agentcontroller.getInstanceConfig(acinstance)
    if config.get('login', 'node') == 'node':
        config['login'] = 'root'
        config['passwd'] = j.console.askPassword('Please enter admin password to register this node', False)

    acclient = j.clients.agentcontroller.get(**config)
    machineguid = j.application.getUniqueMachineId()
    result = acclient.registerNode(j.system.net.getHostname(), machineguid)
    j.application.config.set('grid.node.id', result['node']['id'])
    j.application.config.set('agentcontroller.webdiskey', result['webdiskey'])
