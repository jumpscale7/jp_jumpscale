def main(j,jp):
    appDir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'alerter')
    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd="python", \
        args="alerter.py",\
        env={},\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir=appDir,\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[5005],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=10,\
        isJSapp=1,\
        upstart=False,\
        stats=False,\
        processfilterstr="alerter.py")#what to look for when doing ps ax to find the process
    pd.start()
