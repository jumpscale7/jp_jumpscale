def main(j,jp):
    for proc in [item for item in j.tools.startupmanager.listProcesses() if item.find("_worker")<>-1]:
        dom,name=proc.split("__")
        j.tools.startupmanager.removeProcess(dom,name)

    j.system.fs.remove(j.system.fs.joinPaths(j.dirs.cfgDir,"hrd","workers.hrd"))


    redis=j.packages.findNewest("jumpscale","redis")
    instancename = 'production'
    if not redis.isInstalled(instancename):
        redis.install(hrddata={"redis.name":instancename,"redis.port":"7768","redis.disk":"1","redis.mem":400},instance=instancename)
    redis.start()
