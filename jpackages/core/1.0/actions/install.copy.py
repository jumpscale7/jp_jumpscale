def main(j,jp):
   
    #copying of files is done in this step
    if j.application.sandbox:
        return
    jp._copyfiles()