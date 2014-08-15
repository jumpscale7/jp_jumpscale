def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")

    cmd = 'python controller.py'
    args = '--instance=%s' % jp.instance
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'agentcontroller')
    name="agentcontroller_%s" % jp.instance
    startstoptimeout=20
    j.tools.startupmanager.addProcess(name, cmd, args=args, env={}, numprocesses=1, priority=20, shell=False, workingdir=workingdir,jpackage=jp,domain="",\
        ports=[4444],check=True,timeoutcheck=startstoptimeout,stats=True,upstart=False)


