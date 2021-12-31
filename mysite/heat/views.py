from django.shortcuts import render
from django.http import HttpResponse


def xyCoord(request, xCoord, yCoord):
    # log x and y to session document
    return HttpResponse("ok")


def startSession(request, ip):
    # generate a unique id for the client
    # log their ip to server, cookie them.
    return HttpResponse("ok")


def scrollEvent(request, location):
    return HttpResponse("ok")
def captureTouch(request, location):
    return HttpResponse("ok")

# xyCoord, scrollEvent, captureTouch, screenHeightWidth, inactive, conversionEvent
def logScreenHeightWidth(request, height, width):
    # do what the function says
    return HttpResponse("ok")

def inactiveSession(request, inactiveAt):
    # log what time they went inactive
    return HttpResponse()


def logConversionEvent(request, event):
    # log it to the server
    return HttpResponse()


