def main(j,jp):
    if j.system.net.tcpPortConnectionTest("localhost",9999)==False:
        j.events.opserror_critical("could not find redis on port 9999",category="processmanager.install")

    acinstance = jp.hrd_instance.get('agentcontroller.connection')
    import JumpScale.grid.agentcontroller
    config = j.clients.agentcontroller.getInstanceConfig(acinstance)
    if config.get('login', 'node') == 'node':
        config['login'] = 'root'
        config['passwd'] = j.console.askPassword('Please enter admin password to register this node', False)

    j.application.initWhoAmI(True)
    acclient = j.clients.agentcontroller.get(**config)
    machineguid = j.application.getUniqueMachineId()
    result = acclient.registerNode(j.system.net.getHostname(), machineguid)
    j.application.config.set('grid.node.id', result['node']['id'])
    j.application.config.set('agentcontroller.webdiskey', result['webdiskey'])
