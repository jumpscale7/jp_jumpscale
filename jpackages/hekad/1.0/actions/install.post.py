def main(j,jp):
    hrd = jp.hrd_instance
    role = hrd.get('heka.role')
    cfgpath = '/opt/heka/cfg'
    if role == 'master':
        toremove = ['tcpoutput.toml', 'httpoutput.toml']
    else:
        toremove = ['influx_ouput.toml', 'tcpinput.toml', 'httpinput.toml']
    for file in toremove:
        filepath = j.system.fs.joinPaths(cfgpath, file)
        j.system.fs.remove(filepath)

    hrd.applyOnDir(cfgpath)
