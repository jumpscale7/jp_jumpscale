def main(j,jp):
    
    import JumpScale.baselib.redis
    j.clients.redis.configureInstance("$(redis.name)",$(redis.port),$(redis.mem),int($(redis.disk))==1)

    
