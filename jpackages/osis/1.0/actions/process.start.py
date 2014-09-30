def main(j,jp):
   
    #start the application (only relevant for server apps)
    jp.log("start $(jp.name)")

    connectioninfo = jp.hrd_instance.get('osis.connection')

    tags=j.core.tags.getObject(connectioninfo)
    
    if tags.tagExists("mongodb"):
        #start mongodb if local
        mongoinstance=tags.tagGet("mongodb")    

        jp_monogdb = j.packages.findNewest('jumpscale', 'mongodb_client')
        jp_monogdb.load(mongoinstance)

        ip = jp_monogdb.hrd_instance.get('mongodb.client.addr')

        if j.system.net.isIpLocal(ip):
            jp2=j.packages.findByName("mongodb")
            if j.tools.startupmanager.getStatus4JPackage(jp2)==False:
                jp2.start()

    if tags.tagExists("influxdb"):
        #start influxdb if local
        instance=tags.tagGet("influxdb")    

        jp_influxdb = j.packages.findNewest('serverapps', 'influxdb_client')
        jp_influxdb.load(instance)

        ip = jp_influxdb.hrd_instance.get('influxdb.client.addr')

        if j.system.net.isIpLocal(ip):
            jp2=j.packages.findByName("influxdb")
            if j.tools.startupmanager.getStatus4JPackage(jp2)==False:
                jp2.start()


    j.tools.startupmanager.startJPackage(jp)
    jp.waitUp(timeout=20)
