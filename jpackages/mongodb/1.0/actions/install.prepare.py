def main(j,jp):

    do=j.system.installtools

    # print "get mongodb keys added to apt"
    # do.execute("apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10",dieOnNonZeroExitCode=False)
    # print "get debs"
    # do.execute("echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list")
    # print "update apt metadata"
    # j.system.platform.ubuntu.updatePackageMetadata()
    # # j.system.platform.ubuntu.install("mongodb-org")
    # j.system.platform.ubuntu.install("mongodb-org-server")
    # j.system.platform.ubuntu.install("mongodb-org-mongos")
    # j.system.platform.ubuntu.install("mongodb-org-shell")
    # # j.system.platform.ubuntu.install("mongodb-org-tools")
    
    j.system.fs.createDir("$vardir/mongodb/$(mongodb.name)")

    j.system.platform.ubuntu.stopService("mongod")
    j.system.platform.ubuntu.serviceDisableStartAtBoot("mongod")
