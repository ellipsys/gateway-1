# Create your views here.

import json

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