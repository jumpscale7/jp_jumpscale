def main(j,jp):
    import JumpScale.baselib.redis

    name="rediskvs"
    if j.application.config.get("rediskvs.master.addr")=="" or j.application.config.get("rediskvs.master.addr").lower()=="none":
        slave=False
        ismaster=True
    else:
        slave=(j.application.config.get("rediskvs.master.addr"),j.application.config.get("rediskvs.master.port"),j.application.config.get("rediskvs.secret"))
        ismaster=False
    
    j.clients.redis.configureInstance(name,7771,100,appendonly=False,snapshot=True,slave=slave,ismaster=ismaster)



    
