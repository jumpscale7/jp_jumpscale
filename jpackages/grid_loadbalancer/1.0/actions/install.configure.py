def main(j,jp):
   
    import JumpScale.baselib.startupmanager

    osis_ips = j.application.config.getList('osis.ip')
    ac_ips = j.application.config.getList('grid.agentcontroller.ip')

    osis_servers = ''
    for ip in osis_ips:
        osis_servers += 'server %s:5544;\n    ' % ip

    ac_servers = ''
    for ip in ac_ips:
        ac_servers += 'server %s:4444;\n    ' % ip

    nginxcfg = '''
upstream osis {
    ip_hash;
    %s
}

upstream ac {
    ip_hash;
    %s
}

server {
    listen 80;
    #ssl on;
    server_name _;
    location /osis {
        proxy_pass  http://osis;
    }
    location /ac {
        proxy_pass  http://ac;
    }
}
    ''' % (osis_servers, ac_servers)
    j.system.fs.createDir('$cfgdir/nginx/sites-enabled/')
    j.system.fs.writeFile('$cfgdir/nginx/sites-enabled/default', nginxcfg)
    j.tools.startupmanager.restartProcess("serverapps", "nginx")

    return True