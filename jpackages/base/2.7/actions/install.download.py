def main(j,jp,destination=None,force=False,expand=True,nocode=False):
   
    #copying of files is done in this step
    if not j.application.sandbox:
        jp._download(force=force,destination=destination,expand=expand,nocode=nocode)