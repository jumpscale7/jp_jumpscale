def main(j,jp):
    # redis production


    if j.system.net.tcpPortConnectionTest("localhost",9999)==False:
        j.events.opserror_critical("could not find redis on port 9999",category="osis.install")

    # grid lib 
    if not j.application.sandbox:
        grid = j.packages.findNewest("jumpscale","grid")
        if not grid.isInstalled():
            grid.install()
