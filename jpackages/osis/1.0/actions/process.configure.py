def main(j,jp):
   
    #configure the application to autostart
    
    jp.log("set autostart $(jp.name)")


    #numprocesses: if more than 1 process, will be started in tmux as $name_$nr
    #ports: tcpports
    #autostart: does this app start auto
    #stopcmd: if special command to stop
    #check: check app to see if its running
    #stats: gather statistics by process manager
    #timeoutcheck: how long do we wait to see if app active
    #isJSapp: to tell system if process will self register to redis (is jumpscale app)

    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd = 'python', \
        args = 'osisServerStart.py $jp_instance $(osis.connection)',\
        env={},\
        numprocesses=1,\
        priority=4,\
        shell=False,\
        workingdir="$base/apps/osis",\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[5544],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=20,\
        isJSapp=1,\
        upstart=False,\
        stats=False,\
        processfilterstr="")#what to look for when doing ps ax to find the process
    
    pd.start()
