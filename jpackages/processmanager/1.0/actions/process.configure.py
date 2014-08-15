def main(j,jp):

    if j.application.sandbox:
        cmd="$base/bin/python"
    else:
        cmd="python"
    
    name = "%s_%s" % (jp.name, jp.instance)
    pd=j.tools.startupmanager.addProcess(\
        name=name,\
        cmd=cmd, \
        args="processmanager.py --nodeid=$nodeid --instance=%s" % jp.instance,\
        env={},\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir='$base/apps/processmanager',\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=20,\
        isJSapp=0,\
        upstart=True,\
        stats=True,\
        processfilterstr="processmanager.py --nodeid=$nodeid")#what to look for when doing ps ax to find the process
    
    pd.start()


