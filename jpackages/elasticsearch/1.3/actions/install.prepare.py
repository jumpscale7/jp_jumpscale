
def main(j,jp):
    
    try:
        j.tools.startupmanager.stopProcess("jumpscale","elasticsearch")
    except Exception,e:
        pass


    cmd='dpkg -r elasticsearch'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True,outputToStdout=False)

    cmd='dpkg -P elasticsearch'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True,outputToStdout=False)

    j.system.process.killProcessByPort(9200)

    if not j.application.config.exists("elasticsearch.version") or j.application.config.get("elasticsearch.version")<>"0.9.9":
        #we are updating
        j.console.askYesNo("do you want to remove the old database of elasticsearch, this is required for this version.")
        j.system.fs.removeDirTree("/opt/data/elasticsearch/")
        j.system.fs.removeDirTree("$vardir/elasticsearch/")


    j.system.fs.createDir("$vardir/elasticsearch/data")
    j.system.fs.createDir("$vardir/elasticsearch/tmp")
    j.system.fs.createDir("$vardir/elasticsearch/logs")

