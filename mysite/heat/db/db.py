import pymongo as p

f = open("mongoConnect.txt", "r").read().split("=")[1]

db = client.test_database
# alt db = client['test-database'] if there's a req for dict method

collection = db.test_collection

# db design: a user has sessions, a session has logs