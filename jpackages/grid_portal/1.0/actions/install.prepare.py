
def main(j,jp):

    path="$base/apps/portals/$(grid.portal.instance)"
    if j.system.fs.isLink(path):
        j.system.fs.unlink(path)

    jp2=j.packages.findNewest("jumpscale","portal")
    if not jp2.isInstalled(instance='$(grid.portal.instance)'):
        j.events.inputerror_critical("Could not find portal instance with name: $(grid.portal.instance), please install")
        # jp2.install(hrddata={"redis.name":"production","redis.port":"7768","redis.disk":"1","redis.mem":400},instance="$(cloudrobot.portal.instance)")

    j.system.fs.removeDirTree("$base/apps/portals/$(grid.portal.instance)/base/test__taskmanager/")

