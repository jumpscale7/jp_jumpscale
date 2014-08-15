
def main(j,jp):



    basedir="$base/apps/shorewallconfig/"

    if j.application.config.exists("firewall.ruletemplate"):
        fwtype=j.application.config.get("firewall.ruletemplate")
    else:
        fwtypes=j.system.fs.listDirsInDir( path=basedir, recursive=False, dirNameOnly=True, findDirectorySymlinks=True)
        fwtype=j.console.askChoice(fwtypes)    

    ##NO LONGER RELEVANT TRY TO CREATE RULES WHICH ARE MORE GENERIC
    #nics=j.system.net.getNics()
    # if j.application.config.get("firewall.nics.vpn").strip()=="":
    #     for item in nics:
    #         if item.find("tun")<>-1:
    #             j.application.config.set("firewall.nics.vpn",item)
    # intnic=j.application.config.get("firewall.nics.vpn").strip()
    # try:
    #     nics.pop(nics.index(intnic))
    # except:
    #     pass

    # if j.application.config.get("firewall.nics.pub").strip()=="":
    #     intnic=j.console.askChoice(nics,"Choose nics which are public")
    #     j.application.config.set("firewall.nics.pub",intnic)
    # intnic=j.application.config.get("firewall.nics.pub").strip()
    # try:
    #     nics.pop(nics.index(intnic))
    # except:
    #     pass

    # if j.application.config.get("firewall.nics.loc").strip()=="":    
    #     intnics=j.console.askChoiceMultiple(nics,"Choose nics which are private")
    #     for nic in intnics:
    #         nics.pop(nics.index(nic))
    #     intnic=",".join(intnics).strip(",")
    #     if intnic=="":
    #         intnic="none"
    #     j.application.config.set("firewall.nics.loc",intnic)

    # if j.application.config.get("firewall.nics.dmz").strip()=="":
    #     dmznics=j.console.askChoiceMultiple(nics,"Choose nics which are for dmz")
    #     for nic in dmznics:
    #         nics.pop(nics.index(nic))
    #     dmznic=",".join(dmznics).strip(",")
    #     if dmznic=="":
    #         dmznic="none"
    #     j.application.config.set("firewall.nics.dmz",dmznic)

        
    j.application.config.set("firewall.ruletemplate",fwtype)
    j.application.config.set("firewall.type","shorewall")

    j.system.fs.copyDirTree("/%s/%s"%(basedir,j.application.config.get("firewall.ruletemplate")),"/etc/shorewall")

    rescode,res=j.system.process.execute("shorewall check")
    if rescode<>0:
        j.errorconditionhandler.raiseBug(message="Errors in shorewall configuration.",category="shorewall.config")

    rescode,res=j.system.process.execute("shorewall restart")
    if rescode<>0:
        j.errorconditionhandler.raiseBug(message="Could not restart shorewall.",category="shorewall.init")

    rescode,res=j.system.process.execute("shorewall status")
    if rescode<>0:
        j.errorconditionhandler.raiseBug(message="Could not get status from shorewall.",category="shorewall.status")

    res=res.lower()
    if res.find("started")==-1:
        j.errorconditionhandler.raiseBug(message="Could not start shorewall.",category="shorewall.status")

    print "how can node (fw) to to internet:"
    cmd="shorewall-lite show fw2net"
    print j.system.installtools.execute(cmd)
    
    print "how can node internet get to (fw):"
    cmd="shorewall-lite show net2fw"
    print j.system.installtools.execute(cmd)