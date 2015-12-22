from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *

import json
from builtins import print

# Home Page 
def home(request):
    return render_to_response('app/homepage.html')

# Function for rendering the  firstpage
def firstpage(request):
    if request.method == "GET":
        return render(request, 'app/firstpage.html')
    elif request.method == "POST":
        return HttpResponseRedirect("/home")

# Function for saving coordinates from the first page
def savecoordinates(request):   
    if request.method == "POST":
        try:
            requestBody = json.loads(request.body.decode('utf-8'))
            guestName = requestBody['guestName']
            coordinates = requestBody['coordinates']

            guest = Guest(guest_name = guestName)
            guest.save()
            guestId = Guest.objects.get(id=guest.id)

            for coordinate in coordinates:
                coordinates = Coordinates(lat_value = coordinate['lat'], lng_value = coordinate['long'], id_guest = guestId)
                coordinates.save()

            return HttpResponse(guest.id)

        except Exception as e:
            return HttpResponse(status=400)
        
# Function for rendering the second page
def secondpage(request):
    return render_to_response('app/secondpage.html')

# Function for getting the last saved coordinates and showing them on the second page
def getcoordinates(request, id):   
    if request.method == "GET":

        guest = Guest.objects.get(pk = id)
        coordinateList = []
        coordinates = Coordinates.objects.filter(id_guest = id)   

        for coordinate in coordinates:
            coordinatePair = [coordinate.lat_value, coordinate.lng_value]
            coordinateList.append(coordinatePair)
  
        return HttpResponse(json.dumps(coordinateList), content_type="application/json")