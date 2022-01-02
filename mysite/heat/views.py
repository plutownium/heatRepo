from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from sqlalchemy import insert
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy import Table, Column, Integer, String

from random import randint

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)  # fixme

# Note: No need to log in any users to collect userIds, just keep their ip


# def index(request):
#     print(16)
#     with engine.connect() as conn:
#         result = conn.execute(text("hello world"))
#         print(result)
#         return HttpResponse(result)
#     # return HttpResponse("ok")

# def index2(request):
#     stmt = insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants")
#     return HttpResponse(user_table.c.keys())


# def index3(request):
#
#     return HttpResponse
#


userData = MetaData()
userTable = Table("userAccount", userData, Column("userId", Integer, primary_key=True))

@csrf_exempt
def createUser(request):
    # Create a user to hold sessions.
    userId = randint(0, 100000)
    stmt = insert(userTable).values(userId=userId)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
    return HttpResponse("user created! {}".format(result.inserted_primary_key))


metaDataObjForSession = MetaData()
sessionTable = Table("session", metaDataObjForSession,
                     Column("sessionId", Integer, primary_key=True),
                      Column("userId", Integer, ForeignKey="userAccount.userId"),
                      Column("ip", String(30)),
                      Column("width", Integer),
                      Column("height", Integer))


@csrf_exempt
def startSession(request, userId, ip, width, height):
    # get URL from request body, as it will never fit in a URL argument
    print(get_client_ip(request))
    if request.method == "POST":
        url = request.body.decode("utf-8")
        print(userId, ip, url, width, height)
        sessionId = randint(0, 100000)
        stmt = insert(sessionTable).values(sessionId=sessionId, ip=ip, width=width, height=height)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return HttpResponse("Posted! {}".format(result.inserted_primary_key))
    else:
        return HttpResponse("wrong request method")
    # generate a unique id for the client
    # log their ip to server, cookie them.
    # sessionLog = {
    #     "id": None,  # TODO: let mongodb make up the id
    #     "user": userId,
    #     "ip": ip,
    #     "webpageURI": url,
    #     "viewportWidth": width,
    #     "viewportHeight": height,
    # }
    # logs = db.sessionLogs
    # post_id = logs.insert_one(sessionLog).inserted_id
    # return HttpResponse("ok")


metaDataObjForXYCoord = MetaData()
xyCoordTable = Table("xyCoordRecording", metaDataObjForXYCoord,
                     Column("sessionId", Integer, ForeignKey("session.sessionId")),
                      Column("userId", Integer, primary_key=True),
                      Column("ip", String(30)),
                      Column("xCoord", Integer),
                      Column("yCoord", Integer))


def logXYCoord(request, userId, xCoord, yCoord):
    url = request.body.decode("utf-8")
    print(get_client_ip(request))
    if request.method == "POST":
        url = request.body.decode("utf-8")
        print(userId, url, xCoord, yCoord)
        sessionId = randint(0, 100000)
        stmt = insert(sessionTable).values(userId=userId, xCoord=width, height=height)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return HttpResponse("Posted! {}".format(result.inserted_primary_key))
    else:
        return HttpResponse("wrong request method")
    # # log x and y to session document
    # # locationLog = {"user": userId,
    # #                "webpageURI": url,
    # #                "location": [xCoord, yCoord],
    # #                "sessionId": sessionId,
    # #                }
    # stmtLocationLog = (
    #     insert(eventLog).values(user=userId, webpageURI=url, location=[xCoord, yCoord], sessionId=sessionId)
    # )
    # logs = db.eventLogs
    # post_id = logs.insert_one(locationLog).inserted_id
    # # TODO: maybe add in a feature where, the software logs also what sentence or image the mouse was over.
    # return HttpResponse("hey, {}, {}".format(xCoord, yCoord))


metaDataObjForScrollEvent = MetaData()
scrollEventTable = Table("scrollEvent", metaDataObjForScrollEvent,
                     Column("sessionId", Integer, ForeignKey="session.sessionId"),
                      Column("userId", Integer, primary_key=True),
                      Column("ip", String(30)),
                      Column("location", Integer))


def scrollEvent(request, userId, location):
    scrollLog = {"userId": userId, "location": location}
    logs = db.eventLogs
    scrollEventId = logs.insert_one(scrollLog).inserted_id
    return HttpResponse("ok")


metaDataForCaptureTouch = MetaData()
captureTouchTable = Table("captureTouch", metaDataForCaptureTouch,
                          Column("sessionId", Integer, ForeignKey="session.sessionId"),
                          Column("userId", Integer, primary_key=True),
                          Column("location", Integer))


def captureTouch(request, userId, location):
    touchLog = {
        "userId": userId, "touchLocation": location}
    logs = db.eventLogs
    touchEventId = logs.insert_one(touchLog).inserted_id
    return HttpResponse("ok")


metaDataForLogScreenDimensions = MetaData()
screenDimensionsTable = Table("screenDimensionsLog", metaDataForLogScreenDimensions,
                          Column("sessionId", Integer, ForeignKey="session.sessionId"),
                          Column("userId", Integer, primary_key=True),
                          Column("height", Integer),
                          Column("width", Integer))

# xyCoord, scrollEvent, captureTouch, screenHeightWidth, inactive, conversionEvent
def logScreenHeightWidth(request, userId, height, width):
    heightWidthLog = {
        "userId": userId, "height": height, "width": width}
    logs = db.eventLogs
    touchEventId = logs.insert_one(heightWidthLog).inserted_id
    return HttpResponse("ok")


metaDataForInactiveSession = MetaData()
inactiveSessionTable = Table("inactiveSession", metaDataForLogScreenDimensions,
                          Column("sessionId", Integer, ForeignKey=("session.sessionId")),
                          Column("userId", Integer, primary_key=True),
                          Column("height", Integer),
                          Column("width", Integer))


def inactiveSession(request, userId, inactiveAt):
    """
    :param request:
    :param userId:
    :param inactiveAt: the time from that ms since UTC epoch format
    :return:
    """
    # log what time they went inactive
    inactivityLog = {
        "userId": userId, "inactiveAt": inactiveAt}
    logs = db.eventLogs
    touchEventId = logs.insert_one(inactivityLog).inserted_id
    return HttpResponse("ok")


metaDataForConversionEvent = MetaData()
conversionEventTable = Table("conversionEvent", metaDataForConversionEvent,
                             Column("sessionId", Integer, ForeignKey=("session.sessionId")),
                             Column("conversionId", Integer))


def logConversionEvent(request, userId, conversionId):
    # log it to the server
    conversion = {
        "userId": userId, "conversionId": conversionId}
    logs = db.eventLogs
    touchEventId = logs.insert_one(conversion).inserted_id
    return HttpResponse(touchEventId)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # could also be [1]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

