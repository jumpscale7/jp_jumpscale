def main(j,jp):
    import JumpScale.baselib.redis
    name="rediskvs_master"
    j.clients.redis.configureInstance(name,7772,1000,appendonly=True,snapshot=True,slave=(),ismaster=True,passwd=j.application.config.get("rediskvs.secret"))

