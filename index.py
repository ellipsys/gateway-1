import sqlite3
import json
import re

from datetime import timedelta


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORTS
import sys
import pprint

from mpd import (MPDClient, CommandError)
from socket import error as SocketError

HOST = 'localhost'
PORT = '6600'
PASSWORD = False
##
CON_ID = {'host':HOST, 'port':PORT}
##  

## Some functions
def mpdConnect(client, con_id):
    """
    Simple wrapper to connect MPD.
    """
    try:
        client.connect(**con_id)
    except SocketError:
        return False
    return True

def mpdAuth(client, secret):
    """
    Authenticate
    """
    try:
        client.password(secret)
    except CommandError:
        return False
    return True
##

def getstatus():
    ## MPD object instance
    client = MPDClient()
    if mpdConnect(client, CON_ID):
        print 'Got connected!'
    else:
        print 'fail to connect MPD server.'
        sys.exit(1)

    # Auth if password is set non False
    if PASSWORD:
        if mpdAuth(client, PASSWORD):
            print 'Pass auth!'
        else:
            print 'Error trying to pass auth.'
            client.disconnect()
            sys.exit(2)

    ## Fancy output
    # pp = pprint.PrettyPrinter(indent=4)

    ## Print out MPD stats & disconnect
    output = client.list('file') #stats()

    # pp.pprint(client.stats())

    client.disconnect()
    return output
		#sys.exit(0)


#
# Get root
#
def get_deviceinfo():

#	conn = sqlite3.connect('/tmp/test.db')

	#	conn.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')	
	
#	for row in conn.execute("SELECT * FROM devices"):
#		print row[1]
	
#	conn.commit()
#	conn.close()

	with open('/proc/uptime', 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
		uptime_string = str(timedelta(seconds = uptime_seconds))

	result = {
		"links": [
			{ "rel": "me", "href": "localhost" },
			{ "rel": "actuators", "href": "/actuators" },
			{ "rel": "sensors", "href": "/sensors" } 
		],
		"uptime": uptime_string,
		"sensors": [
			{ "id": 1234, "name": "temperature" }	
		] 
	}	
	return result

def post_sensor():
	return "200 Created"

def get_sensor():
	return "get sensor"








def application(environ, start_response):
	 
	#	output = '<html><head><link style="text/css" rel="stylesheet" href="css/bootstrap.css"></head><body><h2>Hello</h2></body></html>'
	output = { "path": environ['PATH_INFO'] } 

	path_info = environ['PATH_INFO']
	request_method = environ['REQUEST_METHOD']

	matched = re.match(r"/(?P<resource>\w+)/(?P<id>\w+)", path_info)


	if matched:
		matches = matched.groupdict()
	
		if matches["resource"] == "devices":
			if request_method == "POST":
				output = "bla"
			elif request_method == "GET":
				output = "get device"
		elif matches["resource"] == "music":
			if matches["id"] == "files":
				output = getstatus() 

		elif matches["resource"] == "sensors":
			if request_method == "POST":
				output = "sensors"
			elif request_method == "GET":
				output = get_deviceinfo()
 	else:
		output = get_deviceinfo() #"cannot route"

	headers = [('Content-type', 'application/json')]
	start_response('200 OK', headers)
	return [json.dumps(output)]





	
