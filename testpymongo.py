from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import re
app = Flask(__name__)
CORS(app)


app.config["MONGO_URI"] = "mongodb://caochanhduong:bikhungha1@ds261626.mlab.com:61626/activity?retryWrites=false"
mongo = PyMongo(app)
pat = re.compile(r"bình.*",re.I)
dict = {"district":"bình thạnh", "ward":"hưng thạnh"}
values = mongo.db.activities.find(dict)
# print(values)
for value in values:
    print(value['_id'])