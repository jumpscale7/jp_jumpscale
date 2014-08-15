def main(j,jp):
    # redis system
    jp2=j.packages.findNewest("jumpscale","redis")
    if not jp2.isInstalled(instance='production'):
        jp2.install(hrddata={"redis.name":"production","redis.port":"7768","redis.disk":"1","redis.mem":400},instance="production")
    jp2.load(instance='production')
    jp2.start()
    # grid lib 
    if not j.application.sandbox:
        grid = j.packages.findNewest("jumpscale","grid")
        if not grid.isInstalled():
            grid.install()
