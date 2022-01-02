from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from sqlalchemy import insert
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy import Table, Column, Integer, String

from random import randint

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)  # fixme

# Note: No need to log in any users to collect user_ids, just keep their ip


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
userTable = Table("user_account", userData, Column("user_id", Integer, primary_key=True))


@csrf_exempt
def create_user(request):
    # Create a user to hold sessions.
    user_id = randint(0, 100000)
    stmt = insert(userTable).values(user_id=user_id)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
    return HttpResponse("user created! {}".format(result.inserted_primary_key))


metaDataObjForSession = MetaData()
sessionTable = Table("session", metaDataObjForSession,
                     Column("session_id", Integer, primary_key=True),
                     Column("user_id", ForeignKey("user_account.user_id")),
                     Column("ip", String(30)),
                     Column("width", Integer),
                     Column("height", Integer))


@csrf_exempt
def start_session(request, user_id, ip, width, height):
    # get URL from request body, as it will never fit in a URL argument
    print(get_client_ip(request))
    if request.method == "POST":
        url = request.body.decode("utf-8")
        print(user_id, ip, url, width, height)
        session_id = randint(0, 100000)
        stmt = insert(sessionTable).values(session_id=session_id, ip=ip, width=width, height=height)
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
    #     "user": user_id,
    #     "ip": ip,
    #     "webpageURI": url,
    #     "viewportWidth": width,
    #     "viewportHeight": height,
    # }
    # logs = db.sessionLogs
    # post_id = logs.insert_one(sessionLog).inserted_id
    # return HttpResponse("ok")


metadata_for_x_y_coord = MetaData()
x_y_coord_table = Table("x_y_coord_recording", metadata_for_x_y_coord,
                        Column("session_id", ForeignKey("session.session_id")),
                        Column("user_id", Integer, primary_key=True),
                        Column("ip", String(30)),
                        Column("xCoord", Integer),
                        Column("yCoord", Integer))


def log_x_y_coord(request, user_id, xCoord, yCoord):
    url = request.body.decode("utf-8")
    print(get_client_ip(request))
    if request.method == "POST":
        url = request.body.decode("utf-8")
        print(user_id, url, xCoord, yCoord)
        session_id = randint(0, 100000)
        stmt = insert(sessionTable).values(user_id=user_id, xCoord=xCoord, yCoord=yCoord)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return HttpResponse("Posted! {}".format(result.inserted_primary_key))
    else:
        return HttpResponse("wrong request method")
    # # log x and y to session document
    # # locationLog = {"user": user_id,
    # #                "webpageURI": url,
    # #                "location": [xCoord, yCoord],
    # #                "session_id": session_id,
    # #                }
    # stmtLocationLog = (
    #     insert(eventLog).values(user=user_id, webpageURI=url, location=[xCoord, yCoord], session_id=session_id)
    # )
    # logs = db.eventLogs
    # post_id = logs.insert_one(locationLog).inserted_id
    # # TODO: maybe add in a feature where, the software logs also what sentence or image the mouse was over.
    # return HttpResponse("hey, {}, {}".format(xCoord, yCoord))


metadata_for_scroll_event = MetaData()
scroll_event_table = Table("scroll_event", metadata_for_scroll_event,
                           Column("session_id", ForeignKey("session.session_id")),
                           Column("user_id", Integer, primary_key=True),
                           Column("ip", String(30)),
                           Column("location", Integer))


def scroll_event(request, user_id, location):
    if request.method == "POST":
        url = request.body.decode("utf-8")
        print(user_id, url, location)
        stmt = insert(sessionTable).values(user_id=user_id, location=location)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return HttpResponse("Posted! {}".format(result.inserted_primary_key))
    else:
        return HttpResponse("wrong request method")
    # scrollLog = {"user_id": user_id, "location": location}
    # logs = db.eventLogs
    # scrollEventId = logs.insert_one(scrollLog).inserted_id
    # return HttpResponse("ok")


metadata_for_capture_touch = MetaData()
capture_touch_table = Table("capture_touch", metadata_for_capture_touch,
                            Column("session_id", ForeignKey("session.session_id")),
                            Column("user_id", Integer, primary_key=True),
                            Column("location", Integer))


def capture_touch(request, user_id, location):
    if request.method == "POST":
        url = request.body.decode("utf-8")
        print(user_id, url, location)
        stmt = insert(sessionTable).values(user_id=user_id, location=location)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return HttpResponse("Posted! {}".format(result.inserted_primary_key))
    else:
        return HttpResponse("wrong request method")
    # touchLog = {
    #     "user_id": user_id, "touchLocation": location}
    # logs = db.eventLogs
    # touchEventId = logs.insert_one(touchLog).inserted_id
    # return HttpResponse("ok")


metaDataForLogScreenDimensions = MetaData()
screenDimensionsTable = Table("screen_dimensions_log", metaDataForLogScreenDimensions,
                              Column("session_id", ForeignKey("session.session_id")),
                              Column("user_id", Integer, primary_key=True),
                              Column("height", Integer),
                              Column("width", Integer))


def log_screen_height_width(request, height, width):
    if request.method == "POST":
        url = request.body.decode("utf-8")
        print(url, height, width)
        stmt = insert(sessionTable).values(height=height, width=width)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return HttpResponse("Posted! {}".format(result.inserted_primary_key))
    else:
        return HttpResponse("wrong request method")
    # heightWidthLog = {
    #     "user_id": user_id, "height": height, "width": width}
    # logs = db.eventLogs
    # touchEventId = logs.insert_one(heightWidthLog).inserted_id
    # return HttpResponse("ok")


metaDataForInactiveSession = MetaData()
inactiveSessionTable = Table("inactive_session", metaDataForLogScreenDimensions,
                          Column("session_id", ForeignKey("session.session_id")),
                          Column("user_id", Integer, primary_key=True),
                          Column("height", Integer),
                          Column("width", Integer))


def inactive_session(request, user_id, inactive_at):
    """
    :param request:
    :param user_id:
    :param inactive_at: the time from that ms since UTC epoch format
    :return:
    """
    # log what time they went inactive
    if request.method == "POST":
        url = request.body.decode("utf-8")
        print(user_id, url, inactive_at)
        stmt = insert(sessionTable).values(user_id=user_id, inactive_at=inactive_at)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return HttpResponse("Posted! {}".format(result.inserted_primary_key))
    else:
        return HttpResponse("wrong request method")
    # inactivityLog = {
    #     "user_id": user_id, "inactive_at": inactive_at}
    # logs = db.eventLogs
    # touchEventId = logs.insert_one(inactivityLog).inserted_id
    # return HttpResponse("ok")


metaDataForConversionEvent = MetaData()
conversionEventTable = Table("conversionEvent", metaDataForConversionEvent,
                             Column("session_id", ForeignKey("session.session_id")),
                             Column("conversion_id", Integer))


def log_conversion_event(request, user_id, conversion_id):
    # log it to the server
    conversion = {
        "user_id": user_id, "conversionId": conversion_id}
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

