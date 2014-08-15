
def main(j,jp):
    j.system.fs.removeDirTree("/etc/shorewall")
    j.system.platform.ubuntu.install("shorewall")
    j.system.platform.ubuntu.install("shorewall-lite")

    if not j.system.fs.exists(path="/var/log/messages"):
         j.system.fs.writeFile("/var/log/messages","")


