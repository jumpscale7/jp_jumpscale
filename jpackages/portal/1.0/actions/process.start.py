def main(j,jp):
    #start the application (only relevant for server apps)
    jp.log("start $(jp.name)")


    osisinstance = jp.hrd_instance.get('portal.osis.connection')
    osisclientjp = j.packages.findNewest('jumpscale', 'osis_client')
    osisclientjp.load(osisinstance)
    
    osisip = osisclientjp.hrd_instance.get('osis.client.addr')

    if j.system.net.isIpLocal(osisip):
        jposis=j.packages.findByName("osis")
        if j.tools.startupmanager.getStatus4JPackage(jposis)==False:
            jposis.start()

    j.tools.startupmanager.startJPackage(jp)
    jp.waitUp(timeout=20)

