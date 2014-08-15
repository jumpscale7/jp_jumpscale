def main(j,jp):
   
    #find previous files & remove if found
    items=j.system.fs.listFilesInDir(j.system.fs.joinPaths(j.dirs.baseDir,"bin"),True,filter="libvirt*")
    items+=j.system.fs.listFilesInDir(j.system.fs.joinPaths(j.dirs.baseDir,"lib"),True,filter="libvirt*")
    for item in items:
        print "WARNING: found libvirt file on location which should not have been there:'%s'"%item 
        j.system.fs.remove(item)

    jp._copyfiles()