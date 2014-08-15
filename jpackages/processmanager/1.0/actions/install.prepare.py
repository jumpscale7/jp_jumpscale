def main(j,jp):
    redis=j.packages.findNewest("jumpscale","redis")
    instancename = 'production'
    if not redis.isInstalled(instancename):
        redis.install(hrddata={"redis.name":instancename,"redis.port":"7768","redis.disk":"1","redis.mem":400},instance=instancename)
    redis.start()

    acinstance = jp.hrd_instance.get('agentcontroller.connection')
    import JumpScale.grid.agentcontroller
    acclient = j.clients.agentcontroller.getByInstance(acinstance)
    machineguid = j.application.getUniqueMachineId()
    j.application.config.set('grid.node.machineguid', machineguid)
    node = acclient.registerNode(j.system.net.getHostname(), machineguid)
    j.application.config.set('grid.node.id', node['id'])
