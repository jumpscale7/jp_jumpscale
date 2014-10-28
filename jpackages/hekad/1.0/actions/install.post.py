def main(j,jp):
   
    #copying of files is not done in this step
    # the order is:
    # first do prepare
    # then the system automatically copies (if not in debug) starting from the files section of the jpackage
    # then do this tasklet (postinstall)

    #shortcut to some usefull install tools
    #do=j.system.installtools

    #configuration is not done in this step !!!!!
    #preparation like system preps like ubuntu deb installs also not done here
    
    j.system.fs.createDir("/opt/heka/cfg")

    C="""
[hekad]
#maxprocs = 2
share_dir = "/opt/heka/share"

[PayloadEncoder]
append_newlines = false

[TcpInput]
address = "localhost:999"
parser_type = "token"
delimiter = "\\n"

"""

    j.system.fs.writeFile(filename="/opt/heka/cfg/main.toml",contents=C)