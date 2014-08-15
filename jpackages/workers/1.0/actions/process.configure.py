def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")

    #e.g. default:2,hypervisor:1,io:1
    workers = j.application.config.getDict('workers.queues')
    for qname, nrinstances in workers.iteritems():
        print "Queue:%s"% qname
        cmd = 'python'
        wname="worker_%s"%(qname)
        args = "worker.py --nodeid=$nodeid -a '127.0.0.1' -p 7768 -qn %s -wn %s_$numprocess "%(qname,wname)
        workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'agent')
        processfilterstr="worker.py --nodeid=$nodeid"
        j.tools.startupmanager.addProcess(wname, cmd, args=args, env={}, numprocesses=nrinstances, priority=21, shell=False, \
            workingdir=workingdir,jpackage=jp,domain="workers",ports=[],upstart=False,processfilterstr=processfilterstr)
        # j.tools.startupmanager.startProcess("workers",wname)

