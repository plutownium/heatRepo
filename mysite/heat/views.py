from django.shortcuts import render
from django.http import HttpResponse

from sqlalchemy import insert
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)  # fixme

# Note: No need to log in any users to collect userIds, just keep their ip

metadata_obj = MetaData()

def index(request):
    print(16)
    # with engine.connect() as conn:
        # result = conn.execute(text("hello world"))
        # print(result.all())
        # HttpResponse(result.all())
    return HttpResponse("ok")

def index2(request):
    user_table = Table("user_data", metadata_obj, Column("id", Integer, primary_key=True),
                           Column("name", String(30)),
                           Column("fullName", String))
    return HttpResponse(user_table.c.keys())


def index3(request):
    return HttpResponse("k")
    


def logXYCoord(request, userId, url, xCoord, yCoord, sessionId):
    # log x and y to session document
    # locationLog = {"user": userId,
    #                "webpageURI": url,
    #                "location": [xCoord, yCoord],
    #                "sessionId": sessionId,
    #                }
    stmtLocationLog = (
        insert(eventLog).values(user=userId, webpageURI=url, location=[xCoord, yCoord], sessionId=sessionId)
    )
    logs = db.eventLogs
    post_id = logs.insert_one(locationLog).inserted_id
    # TODO: maybe add in a feature where, the software logs also what sentence or image the mouse was over.
    return HttpResponse("hey, {}, {}".format(xCoord, yCoord))


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
    logs = db.eventLogs
    scrollEventId = logs.insert_one(scrollLog).inserted_id
    return HttpResponse("ok")


def captureTouch(request, userId, location):
    touchLog = {
        "userId": userId, "touchLocation": location}
    logs = db.eventLogs
    touchEventId = logs.insert_one(touchLog).inserted_id
    return HttpResponse("ok")


# xyCoord, scrollEvent, captureTouch, screenHeightWidth, inactive, conversionEvent
def logScreenHeightWidth(request, userId, height, width):
    heightWidthLog = {
        "userId": userId, "height": height, "width": width}
    logs = db.eventLogs
    touchEventId = logs.insert_one(heightWidthLog).inserted_id
    return HttpResponse("ok")

def inactiveSession(request, inactiveAt):
    # log what time they went inactive
    inactivityLog = {
        "userId": userId, "inactiveAt": inactiveAt}
    logs = db.eventLogs
    touchEventId = logs.insert_one(inactivityLog).inserted_id
    return HttpResponse("ok")


def logConversionEvent(request, userId, conversion):
    # log it to the server
    conversion = {
        "userId": userId, "conversion": conversion}
    logs = db.eventLogs
    touchEventId = logs.insert_one(conversion).inserted_id
    return HttpResponse(touchEventId)


