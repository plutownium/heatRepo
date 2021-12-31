from django.shortcuts import render
from django.http import HttpResponse
# import pymongo as p

from "../idealRouting" import database as db

db = None  # fixme


# Note: No need to log in any users to collect userIds, just keep their ip

def xyCoord(request, userId, url, xCoord, yCoord, sessionId, ):
    # log x and y to session document
    locationLog = {"user": userId,
                   "webpageURI": url,
                   "location": [xCoord, yCoord],
                   "sessionId": sessionId,
                   }
    logs = db.locationLogs
    post_id = logs.insert_one(locationLog).inserted_id
    # TODO: maybe add in a feature where, the software logs also what sentence or image the mouse was over.
    return HttpResponse("ok")


def startSession(request, userId, ip, url, width, height):
    # generate a unique id for the client
    # log their ip to server, cookie them.
    sessionLog = {
        "id": None,  # TODO: let mongodb make up the id
        "user": userId,
        "ip": ip,
        "webpageURI": url,
        "viewportWidth": width,
        "viewportHeight": height,
    }
    logs = db.sessionLogs
    post_id = logs.insert_one(sessionLog).inserted_id
    return HttpResponse("ok")


def scrollEvent(request, userId, location):
    scrollLog = {"userId": userId, "location": location}
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


