def main(j,jp):
    if not j.application.sandbox:
        #this is needed so libraries are accisble before jumpscale is loaded
        paths = [j.dirs.libDir, j.dirs.libExtDir]
        pthfile = "/usr/local/lib/python2.7/dist-packages/jumpscale.pth"
        j.system.fs.writeFile(pthfile, "\n".join(paths))
