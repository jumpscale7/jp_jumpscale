def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")


    j.system.fs.createDir('$vardir/ssdb')

    j.system.fs.remove("$tmpdir/ssdb.pid")

    pd=j.tools.startupmanager.addProcess(\
        name="ssdb",\
        cmd="rm -rf /opt/jumpscale/var/ssdb/ssdb.pid;./ssdb-server", \
        args="$cfgdir/ssdb/ssdb.conf",\
        env={},\
        numprocesses=1,\
        priority=1,\
        shell=False,\
        workingdir='$base/apps/ssdb',\
        jpackage=jp,\
        domain="serverapps",\
        ports=[8888],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=3,\
        isJSapp=0,\
        upstart=False,\
        stats=True,\
        processfilterstr="ssdb-server")#what to look for when doing ps ax to find the process
    
    pd.start()

    j.system.fs.createDir("$cfgdir/ssdb")
    j.dirs.replaceFilesDirVars("$cfgdir/ssdb")

