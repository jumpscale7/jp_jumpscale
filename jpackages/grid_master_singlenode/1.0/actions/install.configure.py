def main(j,jp):
    j.packages.findNewest('jumpscale', 'mailclient').install()

    rootpasswd='rooter'

    mongodb = j.packages.findNewest('jumpscale', 'mongodb')
    mongodata = {'mongodb.host': '127.0.0,1',
                 'mongodb.port': '27017',
                 'mongodb.replicaset': '',
                 'mongodb.name': 'main'}
    mongodb.install(instance='main', hrddata=mongodata)

    mongoclient = j.packages.findNewest('jumpscale', 'mongodb_client')
    mongodbclientdata = {'mongodb.client.addr': 'localhost',
                         'mongodb.client.port': '27017',
                         'mongodb.client.login': '',
                         'mongodb.client.passwd': ''}
    mongoclient.install(instance='main', hrddata=mongodbclientdata)

    influxdb = j.packages.findNewest('serverapps', 'influxdb')
    influxdb.install(instance='main', hrddata={'influxdb.seedservers':''})
    influxdb.start()

    influxdbclient = j.packages.findNewest('serverapps', 'influxdb_client')
    influxdbclientdata = {'influxdb.client.addr': 'localhost',
                          'influxdb.client.port': '8086',
                          'influxdb.client.login': 'root',
                          'influxdb.client.passwd': 'root'}
    influxdbclient.install(instance='main', hrddata=influxdbclientdata)

    osis = j.packages.findNewest('jumpscale', 'osis')
    osisdata = {'osis.key': '',
            'osis.connection': 'mongodb:main influxdb:main',
            'osis.superadmin.passwd' :rootpasswd}
    osis.install(instance='main', hrddata=osisdata,reinstall=True)

    osisclient = j.packages.findNewest('jumpscale', 'osis_client')
    osisclientdata = {'osis.client.addr': 'localhost',
                      'osis.client.port': '5544',
                      'osis.client.login': 'root',
                      'osis.client.passwd': rootpasswd}
    osisclient.install(instance='main', hrddata=osisclientdata,reinstall=True)

    #generate admin/admin user
    j.application.loadConfig()
    j.application.config.set("grid.master.superadminpasswd",rootpasswd)
    j.application.config.set("osis.superadmin.passwd",rootpasswd)
    if j.application.config.get("agentcontroller.webdiskey")=="" or j.application.config.get("agentcontroller.webdiskey")=="EMPTY":
      j.application.config.set("agentcontroller.webdiskey",j.base.idgenerator.generateGUID())

    j.application.loadConfig()

    import JumpScale.grid.osis

    osis=j.core.osis.getClient("localhost",5544,user="root")
    userclient=j.core.osis.getClientForCategory(osis,"system","user")
    user=userclient.new()
    user.id="admin"
    user.groups="admin"
    user.emails=""
    user.domain="jumpscale"
    user.passwd="admin"
    user.mobile=""
    user.xmpp=""
    user.description=""
    user.authkeys=""
    guid,a,b=userclient.set(user)
    user=userclient.get(guid)
    print "user created:\n%s"%user

    portal = j.packages.findNewest('jumpscale', 'portal')
    portaldata = {'portal.port': '82',
                  'portal.ipaddr': 'localhost',
                  'portal.admin.passwd': rootpasswd,
                  'portal.name': 'main',
                  'osis.connection': 'main'}
    portal.install(instance='main', hrddata=portaldata,reinstall=True)
    portal.start()

    docportal = j.packages.findNewest('jumpscale', 'doc_jumpscale')
    docportal.install(instance='main', hrddata={'portal.instance': 'main'})

    gridportal = j.packages.findNewest('jumpscale', 'grid_portal')
    gridportal.install(instance='main', hrddata={'portal.instance': 'main'})

    webdis = j.packages.findNewest('jumpscale', 'webdis')
    webdis.install()

    webdisclient = j.packages.findNewest('jumpscale', 'webdis_client')
    webdisclientdata = {'addr': '127.0.0.1', 'port': '7779'}
    webdisclient.install(instance='main', hrddata=webdisclientdata,reinstall=True)

    ac = j.packages.findNewest('jumpscale', 'agentcontroller')
    acdata = {'osis.connection': 'main',
            'webdis.connection': 'main'}
    ac.install(instance='main', hrddata=acdata,reinstall=True)
    ac.start()

    #now part of jsagent
    # acclient = j.packages.findNewest('jumpscale', 'agentcontroller_client')
    # acclientdata = {'agentcontroller.client.addr': '127.0.0.1',
    #                 'agentcontroller.client.login': 'node',
    #                 'agentcontroller.client.port': '4444'}
    # acclient.install(instance='main', hrddata=acclientdata)

    pm = j.packages.findNewest('jumpscale', 'jsagent')
    pmdata = {'ac.ipaddress':'localhost',
            'ac.port':4444,
            'ac.login':'node',
            'ac.passwd':'EMPTY'
            }
    pm.install(instance='main', hrddata=pmdata,reinstall=True)


