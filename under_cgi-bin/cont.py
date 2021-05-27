#!/usr/bin/python3

import subprocess
import cgi
import threading

def reply():
    print("content-type: text/html")
    print()

    form = cgi.FieldStorage()
    ctname = form.getvalue("cnm")
    ctcmd = form.getvalue("cmd")

    start = "sudo docker start {}".format(ctname)
    execmd = "sudo docker exec {0} {1}".format(ctname, ctcmd)

    startcont = subprocess.getstatusoutput(start)
    if startcont[0] == 0:
        print("Container {} up & running | \n".format(ctname))

    output = subprocess.getstatusoutput(execmd)
    print("status-code: {} | \n".format(output[0]))
    #if startcont[0] == 126:
    #    print("Container donot have required software or command")
    print("output: <PRE> {} </PRE> \n".format(output[1]))

rep=threading.Thread( target=reply )
rep.start()
