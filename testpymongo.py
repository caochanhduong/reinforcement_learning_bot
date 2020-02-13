from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import re
app = Flask(__name__)
CORS(app)
from bson.objectid import ObjectId

app.config["MONGO_URI"] = "mongodb://caochanhduong:bikhungha1@ds261626.mlab.com:61626/activity?retryWrites=false"
mongo = PyMongo(app)
pat = re.compile(r"bình.*",re.I)
dict = {"_id":ObjectId("5e4101e21a1246342baedb57")}
values = mongo.db.activities.find_one(dict)
print(values)
# for value in values:
#     print(value['_id'])