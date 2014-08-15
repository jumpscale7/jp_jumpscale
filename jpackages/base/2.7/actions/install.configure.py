
def main(j,jp):

    if not j.application.sandbox:

        j.application.config.set("jumpscale.paths.base",j.dirs.baseDir)

