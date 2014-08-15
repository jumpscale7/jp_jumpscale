def main(j,jp):
   
    # cmd="killall redis-server"
    # j.system.process.execute(cmd,dieOnNonZeroExitCode=False)

    import JumpScale.baselib.redis

    j.clients.redis.deleteInstance("$(redis.name)")


