
def main(j,jp):

    j.application.config.applyOnDir("$cfgdir/elasticsearch")
    j.dirs.replaceFilesDirVars("$cfgdir/elasticsearch")
    
