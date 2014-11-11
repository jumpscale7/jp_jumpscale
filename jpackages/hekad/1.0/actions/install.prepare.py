def main(j,jp):
    roles = ['collector', 'master']
    hrd = jp.hrd_instance
    role = hrd.get('heka.role')
    if role not in roles:
        if jp.instance in roles:
            role = jp.instance
        else:
            role = j.console.askChoice(roles, 'Select Heka Type')
        hrd.set('heka.role', role)
    if role == 'collector':
        master = hrd.get('heka.master')
        if not master:
            master = j.console.askString('Provide Heka Master host')
            hrd.set('heka.master', master)
    elif role == 'master':
        for key in ['host', 'dbname', 'user', 'password']:
            value = hrd.get('heka.influxdb.%s' % key)
            if not value:
                value = j.console.askString('Provide Influxdb %s' % key)
                hrd.set('heka.influxdb.%s' % key, value)
