def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    # #example start osis
    cmd = 'python'
    args = 'portal_start.py $jp_instance'
    workingdir = "$base/apps/portals/$(portal.name)"
    name = jp.name
    domain = jp.domain
    ports = j.basetype.integer.fromString('$(portal.port)')
    
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=90, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=[ports])


