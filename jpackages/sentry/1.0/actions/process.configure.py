def main(j,jp):
    import time   

    j.dirs.replaceFilesDirVars("$cfgdir/sentry")

    import os
    ospath=os.environ["PATH"]


    env={}
    env["VIRTUAL_ENV"]="$base/apps/sentry"
    env["PYTHONPATH"]="$base/apps/sentry/lib/python2.7:$base/apps/sentry/lib/python2.7/site-packages:$base/apps/sentry/lib/python2.7/lib-dynload"
    env["PATH"]="$base/apps/sentry/bin:%s"%ospath

    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd="./sentry --config=$cfgdir/sentry/sentry.conf.py start", \
        args="",\
        env=env,\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir='$base/apps/sentry/bin',\
        jpackage=jp,\
        domain="jumpscale",\
        ports=[9000],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=20,\
        isJSapp=False,\
        upstart=False,\
        stats=True,\
        processfilterstr="sentry --config")#what to look for when doing ps ax to find the process

    import psycopg2

    passwd=j.application.config.get("system.superadmin.passwd")
    conn = psycopg2.connect("dbname='template1' user='postgres' host='localhost' password='%s'"%passwd)

    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur=conn.cursor()

    sql="SELECT 1 from pg_database WHERE datname='sentry';"
    cur.execute(sql)
    res=cur.fetchall()
    
    if res==[] or not res[0][0]==1:
        #db does not exist
        cur.execute("CREATE DATABASE sentry;") 
    
    pd.start()

    result=j.system.net.waitConnectionTest("localhost", 9000, 20)

    if result==False:
        raise RuntimeError("could not start sentry, please fix issue & run configure again.")

    time.sleep(1)

    j.application.redis.delete("sentry:dsn")

    print "configure sentry"
    rc,out=j.system.process.execute("unset PYTHONPATH;sh %s/apps/sentry/configure.sh"%j.dirs.baseDir)
    print out

    if rc<>0:
        raise RuntimeError("Could not init the default projects & administrator")
    dsn={}
    for line in out.split("\n"):
        if line.find("SENTRY_DSN")==-1:
            continue        
        line=line.split("for")[1].strip()        
        name=line.split("=")[0].strip()
        dsnval=line.split("//")[1].split("@")[0]
        dsn[name]=dsnval

        j.application.redis.hset("sentry:dsn",name.lower(),dsnval)

        print 'SENTRY_DSN for %s = "%s"' % (name,dsnval)
    
    time.sleep(1)

    # import os
    # import sys

    # j.system.fs.changeDir("$base_data/cfg/sentry")

    

    # sys.path.insert(0,"$base/apps/sentry/lib/python2.7/")
    # sys.path.insert(0,"$base/apps/sentry/lib/python2.7/lib-dynload/")
    # sys.path.insert(0,"$base/apps/sentry/lib/python2.7/site-packages/")

    # for item in j.system.fs.fileGetContents("$base/apps/sentry/lib/python2.7/site-packages/easy-install.pth").split("\n"):
    #     if item.strip()=="":
    #         continue
    #     if item[0]==".":
    #         sys.path.insert(0,"$base/apps/sentry/lib/python2.7/site-packages/%s"%item[2:])


    # # Bootstrap the Sentry environment
    # from sentry.utils.runner import configure

    # configure()


    # from sentry.models import Team, Project, ProjectKey, User

    # user = User()
    # user.username = 'admin'
    # user.email = 'admin@localhost'
    # user.is_superuser = True
    # user.set_password('admin')

    # try:
    #     user.save()
    # except:
    #     pass

    # team = Team()
    # team.name = 'default'
    # team.owner = user

    # try:
    #     team.save()
    # except:
    #     pass

    # j.application.redis.delete("sentry:dsn")

    # for pname in ["Default","Ops","Bugs"]:

    #     project = Project()
    #     project.team = team
    #     project.owner = user
    #     project.name = pname

    #     try:
    #         project.save()
    #     except:
    #         pass

    #     key = ProjectKey.objects.filter(project=project)[0]
    #     dsn=key.get_dsn()
        
    #     j.application.redis.hset("sentry:dsn",pname.lower(),dsn)

    #     print 'SENTRY_DSN for %s = "%s"' % (pname,dsn,)

