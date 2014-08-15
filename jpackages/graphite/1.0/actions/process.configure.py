def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    #start graphite
    cmd = 'source $base/apps/graphite/bin/activate;cd $base/apps/graphite/bin;python run-graphite-devel-server.py $base/apps/graphite --port 8081'
    args = ''
    workingdir = ""
    name = 'graphite'
    domain = "serverapps"
    ports = [8081]
    startstoptimeout=20
    processfilterstr="apps/graphite/webapp"
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=30, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports,check=True,timeoutcheck=startstoptimeout,upstart=False,\
       stats=True,isJSapp=False,processfilterstr=processfilterstr)

    #start carbon
    cmd = 'source $base/apps/graphite/bin/activate;cd $base/apps/graphite/bin;python carbon-cache.py --debug start'
    args = ''
    workingdir = ""
    name = 'carbon'
    domain = "serverapps"
    ports = [2003]
    startstoptimeout=20
    processfilterstr="python carbon-cache.py"
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=31, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports,check=True,timeoutcheck=startstoptimeout,\
       upstart=False,stats=True,isJSapp=False,processfilterstr=processfilterstr)
    
