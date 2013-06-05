# Create your views here.

import json

from datetime import timedelta

from django.http import HttpResponse

def index(request):
    
    if request.method == 'POST':
        response = HttpResponse("Test")
        response['Content-Type'] = 'application/json'
        response.status_code = 201
        
    else:
        response = HttpResponse("Test")
        response['Content-Type'] = 'application/json'
        response.status_code = 200
        
    return response
    
def sensors_detail(request, number):
        
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
            
        response = HttpResponse(json.dumps(result))
        response['Content-Type'] = 'application/json'

        return response   
 
def sensors(request):
    
    if request.method == 'GET':
        response = HttpResponse("15,4")
        return response
    
    
    sensor = []
    
    try:
        sensor = json.loads(request.body)
        msg = "success"
    except:
        msg = "error"
    
    if 'name' in sensor:
        response = HttpResponse(sensor['name'])
        response['Content-Type'] = 'application/json'
        response.status_code = 200
    else: 
        response = HttpResponse("error")
        response['Content-Type'] = 'application/json'
        response.status_code = 400
        
    return response
