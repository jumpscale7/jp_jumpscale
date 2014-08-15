def main(j,jp):
   

    # if j.system.net.tcpPortConnectionTest("127.0.0.1",7768)==False:
        # j.clients.redis.deleteInstance("redisp")
    # if j.system.net.tcpPortConnectionTest("127.0.0.1",7767)==False:
        # j.clients.redis.deleteInstance("redisc")

    cmd="killall redis-server"
    j.system.process.execute(cmd,dieOnNonZeroExitCode=False)

    import JumpScale.baselib.redis

    j.clients.redis.deleteInstance("redisp")
    j.clients.redis.deleteInstance("redisc")
    j.clients.redis.deleteInstance("redisac")


