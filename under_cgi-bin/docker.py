#!/usr/bin/python3

import subprocess
import cgi
import threading

def reply():
    print("content-type: text/html")
    print()

    form = cgi.FieldStorage()
    ctname = form.getvalue("cnm")
    ctimg = form.getvalue("dimg")

    cmd = "sudo docker run -dit --name {0} {1}".format(ctname, ctimg)
    check = "sudo docker ps | grep {}".format(ctname)
    colhead = "sudo docker ps | grep IMAGE"

    print("Starting container: {0} , with image: {1} | \n".format(ctname, ctimg))
    output = subprocess.getstatusoutput(cmd)

    print("status-code: {} | \n".format(output[0]))
    print("output: <PRE> {} </PRE> \n".format(output[1]))

    checkout = subprocess.getstatusoutput(check)
    setcolhead= subprocess.getstatusoutput(colhead)

    if checkout[0] == 0:
        print("Container Up & Running \n")
    print("<PRE> {} </PRE> \n".format(setcolhead[1]))
    print("<PRE> {} </PRE> \n".format(checkout[1]))

    print("Use this link to work with container: <A href='http://192.168.99.103/forms/cont.html'>/forms/cont.html<A>")

rep=threading.Thread( target=reply )
rep.start()
