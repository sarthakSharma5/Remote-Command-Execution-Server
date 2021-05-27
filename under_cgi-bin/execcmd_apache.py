#!/usr/bin/python3

import subprocess
import cgi
import threading

def reply():
    print("content-type: text/html")
    print()

    form = cgi.FieldStorage()
    cmd = form.getvalue("cmd")

    if 'sudo' in cmd:
        cmd = cmd.replace('sudo', '')
        print("Cannot allow use of sudo for general users")

    if 'docker ' in cmd:
        print("You are not authorized to use docker-ce!")
        exit()

    print("command: {} | ".format(cmd))
    output = subprocess.getstatusoutput(cmd)

    print("status-code: {} | ".format(output[0]))
    print()
    print("output: <PRE> {} </PRE> \n".format(output[1]))
    print("<BR>")

    print()

rep = threading.Thread( target=reply )
rep.start()
