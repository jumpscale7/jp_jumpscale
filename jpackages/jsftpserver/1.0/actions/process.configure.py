def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    # #example start osis
    cmd = 'python'
    args = 'jsftpserver.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'jsftpserver')
    name = jp.name
    domain = "serverapps"
    ports = [2111]
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=99, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports,check=False,timeoutcheck=5)
    
    #can configure more apps to start than just 1 linked to the jpackage

    j.tools.startupmanager.start(name=name,domain=domain)

    pass
