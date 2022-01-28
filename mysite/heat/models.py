from django.db import models
from django.db.models import CharField, IntegerField, PositiveIntegerField, ForeignKey

# Create your models here.

class Viewer(models.Model):
    __tablename__ = 'viewer'
    id = PositiveIntegerField(primary_key=True)


class Session(models.Model):
    __tablename__ = "session"
    session_id = PositiveIntegerField(primary_key=True),
    viewer_id = ForeignKey(Viewer, on_delete=models.CASCADE)
    ip = CharField(max_length=30),
    height = IntegerField()
    width = IntegerField()


class XYCoord(models.Model):
    __tablename__ = "xyCoords"
    session_id = ForeignKey(Session, on_delete=models.CASCADE)
    user_id = PositiveIntegerField(primary_key=True)
    ip = CharField(max_length=30)
    x = IntegerField()
    y = IntegerField()


class ScrollEvent(models.Model):
    __tablename__ = "scroll_event"
    session_id = ForeignKey(Session, on_delete=models.CASCADE)
    user_id = PositiveIntegerField(primary_key=True)
    ip = CharField(max_length=30)
    location = IntegerField()


class CaptureTouch(models.Model):
    __tablename__ = "capture_touch"
    session_id = ForeignKey(Session, on_delete=models.CASCADE)
    user_id = PositiveIntegerField(primary_key=True)
    location = IntegerField()


class LogScreenDimensions(models.Model):
    __tablename__ = "screen_dimensions_log"
    session_id = ForeignKey(Session, on_delete=models.CASCADE)
    user_id = PositiveIntegerField(primary_key=True)
    height = IntegerField()
    width = IntegerField()


class InactiveSession(models.Model):
    __tablename__ = "inactive_session"
    session_id = ForeignKey(Session, on_delete=models.CASCADE)
    user_id = PositiveIntegerField(primary_key=True)
    height = IntegerField()
    width = IntegerField()


class ConversionEvent(models.Model):
    __tablename__ = "conversion_event"
    session_id = ForeignKey(Session, on_delete=models.CASCADE)
    conversion_id = IntegerField()

