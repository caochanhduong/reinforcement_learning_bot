from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://caochanhduong:bikhungha1@ds261626.mlab.com:61626/activity?retryWrites=false"
mongo = PyMongo(app)


def msg(code, mess=None):
    if code == 200 and mess is None:
        return jsonify({"code": 200, "value": True})
    else:
        return jsonify({"code": code, "message": mess}), code


# In[14]:
@app.route('/')
def index():
    return """<h1>rLeT BOT</h1>"""


@app.errorhandler(404)
def url_error(e):
    print("---------------------")
    return msg(404, "cao chánh dương")


@app.errorhandler(500)
def server_error(e):
    return msg(500, "SERVER ERROR")


@app.route('/api/insert-activity', methods=['POST'])
def post_api():
    input_data = request.get_json(force=True)
    mongo.db.activities.insert_one(
        {"map_time_to_work":None,"is_children_of":None,"is_parent_of":None,"name_activity": [input_data["name_activity"]], "type_activity": [input_data["type_activity"]], "holder": [input_data["holder"]], "time": [input_data["time"]], "city": [input_data["city"]], "district": [input_data["district"]], "ward": [input_data["ward"]], "name_place": [input_data["name_place"]], "street": [input_data["street"]], "reward": [input_data["reward"]], "contact": [input_data["contact"]], "register": [input_data["register"]], "works": [input_data["works"]], "joiner": [input_data["joiner"]]})
        
    return jsonify({"code": 200, "message": "insert successed!"})
    
@app.route('/api/dictionary', methods=['POST'])
def post_api_dictionary():
    input_data = request.get_json(force=True)
    mongo.db.dictionary.insert_one(
        {"orther": ["not available", "movie assistant number", "movie booking service", "search theater", "cannot book", "servicing tickets", "rotten tomatoes", "pub serves good burgers", "serves seafood", "date", "scary", "restaurant", "beer", "mexican restaurant", "best restaurant", "japanese restaurant", "thats odd", "crossed", "little late", "pub", "number 1", "switch cities", "name", "unable to book movies", "I cannot understand your reply", "purchase tickets", "look up date", "increased functionality", "functionality", "Master User", "master user", "two", "another preference", "no", "check again", "new release", "new releases", "place that serves seafood", "favorite part", "worth watching", "subtitiles", "subtitles", "many many theaters", "different selection of movies", "search for a theater", "latest showing", "Italian restaurant", "restaurant booking service", "online ticketing", "I cant remember", "cant think of", "search theaters", "cheapest", "do not know", "date night", "disney", "search by movie or movie theater", "indian restaurant", " movie purchasing service", "movie ticket buying service", "early in the day", "safeco field", "many", "pizza place", "restaurant reservations", "pizza restaurant", "restaurant service", "laughable", "english and chinese subtitles", "matinee", " matinee", "good restaurant", "currently", "george on the riverwak", "purchase", "odd", "got crossed", "29 movies", "I can bring my cat to", "I can order beer in", "closed", "serve alcohol", "restaurants", "book movie tickets", "before dinner"],"greeting": ["hey", "hello", "good morning", "hi", "there", "hello there", "happy to", "good evening", "hi welcome", "hey there", "hi there"],"map_time_to_work":None,"is_children_of":None,"is_parent_of":None,"name_activity": input_data["name_activity"], "type_activity": input_data["type_activity"], "holder": input_data["holder"], "time": input_data["time"], "city": input_data["city"], "district": input_data["district"], "ward": input_data["ward"], "name_place": input_data["name_place"], "street": input_data["street"], "reward": input_data["reward"], "contact": input_data["contact"], "register": input_data["register"], "works": input_data["works"], "joiner": input_data["joiner"]})
        
    return jsonify({"code": 200, "message": "insert successed!"})

@app.route('/api/all-activities', methods=['GET'])
def get_api_all_activity():
    # input_data = request.get_json(force=True)
    # mongo.db.dictionary.insert_one(
    #     {"orther": ["not available", "movie assistant number", "movie booking service", "search theater", "cannot book", "servicing tickets", "rotten tomatoes", "pub serves good burgers", "serves seafood", "date", "scary", "restaurant", "beer", "mexican restaurant", "best restaurant", "japanese restaurant", "thats odd", "crossed", "little late", "pub", "number 1", "switch cities", "name", "unable to book movies", "I cannot understand your reply", "purchase tickets", "look up date", "increased functionality", "functionality", "Master User", "master user", "two", "another preference", "no", "check again", "new release", "new releases", "place that serves seafood", "favorite part", "worth watching", "subtitiles", "subtitles", "many many theaters", "different selection of movies", "search for a theater", "latest showing", "Italian restaurant", "restaurant booking service", "online ticketing", "I cant remember", "cant think of", "search theaters", "cheapest", "do not know", "date night", "disney", "search by movie or movie theater", "indian restaurant", " movie purchasing service", "movie ticket buying service", "early in the day", "safeco field", "many", "pizza place", "restaurant reservations", "pizza restaurant", "restaurant service", "laughable", "english and chinese subtitles", "matinee", " matinee", "good restaurant", "currently", "george on the riverwak", "purchase", "odd", "got crossed", "29 movies", "I can bring my cat to", "I can order beer in", "closed", "serve alcohol", "restaurants", "book movie tickets", "before dinner"],"greeting": ["hey", "hello", "good morning", "hi", "there", "hello there", "happy to", "good evening", "hi welcome", "hey there", "hi there"],"map_time_to_work":None,"is_children_of":None,"is_parent_of":None,"name_activity": input_data["name_activity"], "type_activity": input_data["type_activity"], "holder": input_data["holder"], "time": input_data["time"], "city": input_data["city"], "district": input_data["district"], "ward": input_data["ward"], "name_place": input_data["name_place"], "street": input_data["street"], "reward": input_data["reward"], "contact": input_data["contact"], "register": input_data["register"], "works": input_data["works"], "joiner": input_data["joiner"]})
    list_all_activity=[]
    for item in mongo.db.activities.find({}):
        print(type(item))
        list_all_activity.append(item)
        break
    # print(mongo.db.activities.find({}))
    return {"code":200,"data":list_all_activity}

if __name__ == '__main__':
    app.run()