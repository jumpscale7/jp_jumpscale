def main(j,jp):
   
    dpath = "$vardir/redis/$(redis.name)"
    cpath = j.system.fs.joinPaths(dpath, "redis.conf")
    port=int($(redis.port))
    pd=j.tools.startupmanager.addProcess(\
        name="redis_$(redis.name)",\
        cmd="$base/apps/redis/redis-server", \
        args="$vardir/redis/$(redis.name)/redis.conf",\
        env={},\
        numprocesses=1,\
        priority=1,\
        shell=False,\
        workingdir='$base/apps/redis/',\
        jpackage=jp,\
        domain="redis",\
        ports=[port],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=2,\
        isJSapp=0,\
        upstart=True,\
        stats=True,\
        processfilterstr="redis-server 127.0.0.1:$(redis.port)")#what to look for when doing ps ax to find the process
        
    pd.start()

