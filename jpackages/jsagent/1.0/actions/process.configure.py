def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")

    cmd = 'python jsagent.py'
    args = '--instance=%s' % jp.instance
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'jsagent')
    name="jsagent"
    startstoptimeout=20
    j.tools.startupmanager.addProcess(name, cmd, args=args, env={}, numprocesses=1, priority=100, shell=False, workingdir=workingdir,jpackage=jp,domain="",\
        ports=[4445],check=True,timeoutcheck=startstoptimeout,stats=True,upstart=False)
