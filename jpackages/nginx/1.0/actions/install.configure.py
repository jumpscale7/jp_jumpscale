def main(j,jp):
   
    #configure the package 
    #j.application.config.applyOnDir("$cfgdir/elasticsearch1")
    #j.dirs.replaceFilesDirVars("$cfgdir/elasticsearch1")

    j.system.fs.createDir("$vardir/log/nginx/")
    if not j.application.sandbox:
        j.system.platform.ubuntu.install('liblua5.1-0')
