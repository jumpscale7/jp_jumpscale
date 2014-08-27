def main(j,jp):
    influxdbclientinstance = jp.hrd_instance.get('influxdb.connection')
    influxdbclientjp = j.packages.findNewest('serverapps', 'influxdb_client')
    influxdbclientjp.load(influxdbclientinstance)
    influxhrd = influxdbclientjp.hrd_instance
    serverip = influxhrd.get('influxdb.client.addr')
    if j.system.net.isIpLocal(serverip):
        serverip = 'window.location.hostname'
    configpath = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'portals', 'jslib', 'grafana', 'config.js')
    j.dirs.replaceFilesDirVars(configpath, additionalArgs={'serverip': serverip})
    import JumpScale.baselib.influxdb
    addr = influxhrd.get('influxdb.client.addr')
    port = influxhrd.getInt('influxdb.client.port')
    user = influxhrd.get('influxdb.client.login')
    passwd = influxhrd.get('influxdb.client.passwd')

    client = j.clients.influxdb.get(addr, port, user, passwd)
    dbs = [ x['name'] for x in client.get_database_list() ]
    for dbname in ('main', 'grafana'):
        if 'main' not in dbs:
            client.create_database(dbname)
        client.switch_db(dbname)
        users = [ x['name'] for x in client.get_database_users() ]
        if 'admin' not in users:
            client.add_database_user('admin', 'admin')
        client.set_database_admin('admin')



