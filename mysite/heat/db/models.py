from sqlalchemy import Table, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event

Base = declarative_base()

class MyDataClass(Base):
    __tablename__ = 'my_data'
    id = Column(Integer, primary_key=True)
    # data = Column(MutableDict.as_mutable(JSONEncodedDict))
    data = Column()


class Viewer(Base):
    __tablename__ = "viewer"
    id = Column(Integer, primary_key=True)
    data = Column()