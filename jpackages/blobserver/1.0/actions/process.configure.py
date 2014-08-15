def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")

    cmd = 'python'
    args = 'blobserver.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'blobserver')
    name="blobserver"
    j.tools.startupmanager.addProcess(name, cmd, args=args, env={}, numprocesses=1, priority=30, shell=False, workingdir=workingdir,jpackage=jp,domain="",ports=[21])


    jp.start()