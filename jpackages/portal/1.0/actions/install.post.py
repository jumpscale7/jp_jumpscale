def main(j,jp):
   
    dest="$base/apps/portals/$(portal.name)"
    j.system.fs.copyDirTree("$base/apps/portals/portalexample",dest)
    jp.hrd_instance.applyOnDir(dest)
    j.application.config.applyOnDir(dest)
    j.dirs.replaceFilesDirVars(dest)


