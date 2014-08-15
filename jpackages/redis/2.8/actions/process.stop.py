def main(j,jp):
    from JumpScale.baselib.startupmanager.StartupManager import ProcessNotFoundException
    #stop the application (only relevant for server apps)
    jp.log("stop $(jp.name)")

    name="redis_$(redis.name)"
    try:
        j.tools.startupmanager.stopProcess('redis', name)
    except ProcessNotFoundException:
        pass

