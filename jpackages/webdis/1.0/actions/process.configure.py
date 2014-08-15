def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    j.system.fs.createDir('$vardir/webdis')

    # j.system.fs.remove("$tmpdir/webdis.pid")

    pd=j.tools.startupmanager.addProcess(\
        name="webdis",\
        cmd="./webdis", \
        args="$cfgdir/webdis/webdis.json",\
        env={},\
        numprocesses=1,\
        priority=6,\
        shell=False,\
        workingdir='$base/apps/webdis',\
        jpackage=jp,\
        domain="serverapps",\
        ports=[7779],\
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
        processfilterstr="./webdis")#what to look for when doing ps ax to find the process
    
    pd.start()    
