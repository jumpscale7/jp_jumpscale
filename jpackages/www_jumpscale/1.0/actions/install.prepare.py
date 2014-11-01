def main(j,jp):
   
    instance='$(portal.instance)'

    path="$base/apps/portals/%s"%instance
    if j.system.fs.isLink(path):
        j.system.fs.unlink(path)

    jp2=j.packages.findNewest("jumpscale","portal")
    if not jp2.isInstalled(instance=instance):
        j.events.inputerror_critical("Could not find portal instance with name: %s, please install"%instance)

    if j.system.net.tcpPortConnectionTest("localhost",9999)==False:
        j.events.opserror_critical("could not find redis on port 9999",category="wwwjumpscale.install")

    j.system.fs.removeDirTree("$base/apps/portals/%s/base/test__taskmanager/"%instance)

    