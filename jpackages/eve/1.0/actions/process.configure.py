def main(j,jp):
    args = ['eve_start.py']
    
    port = 5000

    if jp.hrd_instance.exists("eve.port"):
        p = jp.hrd_instance.get("eve.port")
        if p:
            port = p
        args.append('--port %s' % port)
    
    if jp.hrd_instance.exists("eve.mongo.host"):
        mh = jp.hrd_instance.get("eve.mongo.host")
        if mh:
            args.append('--mongo_host %s' % mh)
            
    if jp.hrd_instance.exists("eve.mongo.port"):
        mp = jp.hrd_instance.get("eve.mongo.port")
        if mp:
           args.append('--mongo_port %s' % mp)

    if jp.hrd_instance.exists("eve.pagination.limit"):
        pl = jp.hrd_instance.get("eve.pagination.limit")
        if pl:
            args.append('--pagination_limit %s' % pl)
    
    args = ' '.join(args)

    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd="python" ,\
        args=args,\
        env={},\
        numprocesses=1,\
        priority=90,\
        shell=True,\
        workingdir='$base/apps/eve/',\
        jpackage=jp,\
        domain=jp.domain,\
        ports=[port],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=20,\
        isJSapp=0,\
        upstart=False,\
        stats=False,\
        processfilterstr="eve_start.py")#what to look for when doing ps ax to find the process
    pd.start()


