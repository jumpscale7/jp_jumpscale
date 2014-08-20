def main(j,jp):
    j.packages.findNewest('jumpscale', 'mailclient').install()

    mongodb = j.packages.findNewest('jumpscale', 'mongodb')
    mongodata = {'mongodb.host': '127.0.0,1',
                 'mongodb.port': '27017',
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
            'osis.superadmin.passwd' :'rooter'}
    osis.install(instance='main', hrddata=osisdata)

    osisclient = j.packages.findNewest('jumpscale', 'osis_client')
    osisclientdata = {'osis.client.addr': 'localhost',
                      'osis.client.port': '5544',
                      'osis.client.login': 'root',
                      'osis.client.passwd': 'rooter'}
    osisclient.install(instance='main', hrddata=osisclientdata)

    portal = j.packages.findNewest('jumpscale', 'portal')
    portaldata = {'portal.port': '82',
                  'portal.ipaddr': 'localhost',
                  'portal.admin.passwd': 'rooter',
                  'portal.name': 'main',
                  'portal.osis.connection': 'main'}
    portal.install(instance='main', hrddata=portaldata)

    docportal = j.packages.findNewest('jumpscale', 'doc_jumpscale')
    docportal.install(instance='main', hrddata={'portal.instance': 'main'})

    gridportal = j.packages.findNewest('jumpscale', 'grid_portal')
    gridportal.install(instance='main', hrddata={'portal.instance': 'main'})

    webdis = j.packages.findNewest('jumpscale', 'webdis')
    webdis.install()

    webdisclient = j.packages.findNewest('jumpscale', 'webdis_client')
    webdisclientdata = {'addr': '127.0.0.1', 'port': '7779'}
    webdisclient.install(instance='main', hrddata=webdisclientdata)

    ac = j.packages.findNewest('jumpscale', 'agentcontroller')
    acdata = {'osis.connection': 'main',
            'webdis.connection': 'main'}
    ac.install(instance='main', hrddata=acdata)
    ac.start()

    acclient = j.packages.findNewest('jumpscale', 'agentcontroller_client')
    acclientdata = {'agentcontroller.client.addr': '127.0.0.1',
                    'agentcontroller.client.login': 'node',
                    'agentcontroller.client.port': '4444'}
    acclient.install(instance='main', hrddata=acclientdata)

    pm = j.packages.findNewest('jumpscale', 'processmanager')
    pmdata = {'agentcontroller.connection': 'main',
            'webdis.connection': 'main'}
    pm.install(instance='main', hrddata=pmdata)


    workers = j.packages.findNewest('jumpscale', 'workers')
    workers.install()
    workers.start()
