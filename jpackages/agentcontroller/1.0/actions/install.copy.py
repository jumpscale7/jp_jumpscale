def main(j,jp):
   
    #copying of files is done in this step
    j.system.fs.removeDirTree("$basedir/apps/agentcontroller/jumpscripts/")
    j.system.fs.removeDirTree("$basedir/apps/agentcontroller/processmanager/eventhandling/")
    j.system.fs.removeDirTree("$basedir/apps/agentcontroller/processmanager/loghandling/")
    j.system.fs.removeDirTree("$basedir/apps/agentcontroller/processmanager/monitoringobjects/")
    j.system.fs.removeDirTree("$basedir/apps/agentcontroller/processmanager/processmanagercmds/")
    jp._copyfiles()