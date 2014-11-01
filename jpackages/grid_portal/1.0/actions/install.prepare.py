
def main(j,jp):

    path="$base/apps/portals/$(portal.instance)"
    if j.system.fs.isLink(path):
        j.system.fs.unlink(path)

    jp2=j.packages.findNewest("jumpscale","portal")
    if not jp2.isInstalled(instance='$(portal.instance)'):
        j.events.inputerror_critical("Could not find portal instance with name: $(portal.instance), please install")

    j.system.fs.removeDirTree("$base/apps/portals/$(portal.instance)/base/test__taskmanager/")

