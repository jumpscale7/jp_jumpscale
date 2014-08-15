def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")


    #numprocesses: if more than 1 process, will be started in tmux as $name_$nr
    #ports: tcpports
    #autostart: does this app start auto
    #stopcmd: if special command to stop
    #check: check app to see if its running
    #stats: gather statistics by process manager
    #timeoutcheck: how long do we wait to see if app active
    #isJSapp: to tell system if process will self register to redis (is jumpscale app)

    pd=j.tools.startupmanager.addProcess(\
        name="shellinabox",\
        cmd="shellinaboxd -s ", \
        args="'/:root:root:/root:python  $base/apps/jail/shellinabox_launcher.py ${url} -p $(shellinabox.port)' -t --linkify=aggressive",\
        env={},\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir='$base/apps/jail',\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[$(shellinabox.port)],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd="",\
        check=True,\
        timeoutcheck=10,\
        isJSapp=0,\
        upstart=False,\
        stats=False,\
        processfilterstr="shellinaboxd")#what to look for when doing ps ax to find the process

