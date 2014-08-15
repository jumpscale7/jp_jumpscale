def main(j,jp):
    #stop the application (only relevant for server apps)
    jp.log("start $(jp.name)")

    name="redis_$(redis.name)"
    j.tools.startupmanager.startProcess('redis', name)

    jp.waitUp(timeout=20)
