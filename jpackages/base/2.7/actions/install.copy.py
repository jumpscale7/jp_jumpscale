def main(j,jp):
    if not j.application.sandbox:
        jp._copyfiles()
