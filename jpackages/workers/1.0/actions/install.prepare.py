def main(j,jp):
    for proc in [item for item in j.tools.startupmanager.listProcesses() if item.find("_worker")<>-1]:
        dom,name=proc.split("__")
        j.tools.startupmanager.removeProcess(dom,name)

    j.system.fs.remove(j.system.fs.joinPaths(j.dirs.cfgDir,"hrd","workers.hrd"))

    if j.system.net.tcpPortConnectionTest("localhost",9999)==False:
        j.events.opserror_critical("could not find redis on port 9999",category="worker.install")