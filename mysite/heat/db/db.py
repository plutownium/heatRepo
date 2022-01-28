from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event

import sqlalchemy as db

# engine = db.create_engine('dialect+driver://user:pass@host:port/db')

# fixme: dialect + driver user:pass

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()

Base = declarative_base()
