def main(j,jp):
    for instancename, port in (('agentcontroller', '7769'), ('production', '7768')):
        redis=j.packages.findNewest("jumpscale","redis")
        if not redis.isInstalled(instancename):
            redis.install(hrddata={"redis.name":instancename,"redis.port":port,"redis.disk":"1","redis.mem":500},instance=instancename)
        redis.load(instancename)
        redis.start()

