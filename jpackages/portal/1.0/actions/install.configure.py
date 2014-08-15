def main(j,jp):
   
    #configure the package 

    pass
    
    #username:passwd:group1,group2:email1,email2:domain
    cmd="jsuser add -d admin:$(portal.admin.passwd):admin::adomain"
    j.system.process.execute(cmd,False) #do not die

    print "prepare done"