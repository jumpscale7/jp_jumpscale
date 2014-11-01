def main(j,jp):
    if j.system.net.tcpPortConnectionTest("localhost",9999)==False:
        j.events.opserror_critical("could not find redis on port 9999",category="webdis.install")