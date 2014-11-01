def main(j,jp):
    import sys
    path = j.system.fs.joinPaths(j.dirs.libDir, 'python.zip')
    if path not in sys.path:
        sys.path.append(path)

    import JumpScale.baselib.startupmanager
    j.tools.startupmanager.installRedisSystem()

    # redis=j.packages.findNewest("jumpscale","redis")
    # if not redis.isInstalled():        
    #     redis.install(hrddata={"redis.name":"system","redis.port":"9999","redis.disk":"0","redis.mem":20},instance="system")
    # redis.instance="system"
    # redis.start()
    
    j.dirs.replaceFilesDirVars("$base/bin/celery")
    j.dirs.replaceFilesDirVars("$base/bin/celerybeat")
    j.dirs.replaceFilesDirVars("$base/bin/celeryd")
    j.dirs.replaceFilesDirVars("$base/bin/celeryd-multi")
    j.dirs.replaceFilesDirVars("$base/bin/fab")