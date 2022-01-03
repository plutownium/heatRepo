from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event

Base = declarative_base()


class Viewer(Base):
    __tablename__ = 'viewer'
    id = Column(Integer, primary_key=True)


class Session(Base):
    __tablename__ = "session"
    session_id = Column(Integer, primary_key=True),
    user_id = Column(ForeignKey("user_account.user_id")),
    ip = Column(String(30)),
    height = Column(Integer)
    width = Column(Integer)


class XYCoord(Base):
    __tablename__ = "xyCoords"
    session_id = Column(ForeignKey("session.session_id"))
    user_id = Column(Integer, primary_key=True)
    ip = Column(String(30))
    x = Column(Integer)
    y = Column(Integer)


class ScrollEvent(Base):
    __tablename__ = "scroll_event"
    session_id = Column(ForeignKey("session.session_id"))
    user_id = Column(Integer, primary_key=True)
    ip = Column(String(30))
    location = Column(Integer)


class CaptureTouch(Base):
    __tablename__ = "capture_touch"
    session_id = Column(ForeignKey("session.session_id"))
    user_id = Column(Integer, primary_key=True)
    location = Column(Integer)


class LogScreenDimensions(Base):
    __tablename__ = "screen_dimensions_log"
    session_id = Column(ForeignKey("session.session_id"))
    user_id = Column(Integer, primary_key=True)
    height = Column(Integer)
    width = Column(Integer)


class InactiveSession(Base):
    __tablename__ = "inactive_session"
    session_id = Column(ForeignKey("session.session_id"))
    user_id = Column(Integer, primary_key=True)
    height = Column(Integer)
    width = Column(Integer)


class ConversionEvent(Base):
    __tablename__ = "conversion_event"
    session_id = Column(ForeignKey("session.session_id"))
    conversion_id = Column(Integer)
