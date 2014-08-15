def main(j,jp):
    name="rediskvs_master"
    dpath = "$vardir/redis/%s" % name
    cpath = j.system.fs.joinPaths(dpath, "redis.conf")
    pd=j.tools.startupmanager.addProcess(\
        name=name,\
        cmd="./redis-server", \
        args=cpath,\
        env={},\
        numprocesses=1,\
        priority=1,\
        shell=False,\
        workingdir='$base/apps/redis/',\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[7772],\
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
        processfilterstr="redis/%s/redis.conf"%(name))#what to look for when doing ps ax to find the process
    pd.start()

        # self.startInstance(name)
