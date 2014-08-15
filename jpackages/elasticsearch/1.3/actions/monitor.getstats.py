def main(j,jp):

    import JumpScale.baselib.startupmanager
    status = j.tools.startupmanager.status('elasticsearch')
    return status
