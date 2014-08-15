def main(j,jp):
   
    jp=j.packages.findNewest("jumpscale","portal")
    jp.load("$(portal.instance)")
    jp.restart()
