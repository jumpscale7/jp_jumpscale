def main(j,jp):
   
    #configure the application to autostart
    
    cmd = 'python'
    args = 'blobserver2_master.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'blobserver2')
    name = jp.name
    domain = jp.domain
    startstoptimeout=20
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=24, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=[2344],check=True,timeoutcheck=startstoptimeout)

    pass
