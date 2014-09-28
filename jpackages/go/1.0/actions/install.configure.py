def main(j,jp):
   
    #configure the package 
    #j.application.config.applyOnDir("$cfgdir/elasticsearch1")
    #j.dirs.replaceFilesDirVars("$cfgdir/elasticsearch1")

    C="""
export GOROOT=/opt/go
export GOPATH=/opt/go/myproj
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
    """

    ed=j.codetools.getTextFileEditor("/root/.bashrc")
    ed.setSection("go", C)

    
