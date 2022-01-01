import sqlalchemy as db
# engine = db.create_engine('dialect+driver://user:pass@host:port/db')

# fixme: dialect + driver user:pass

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)