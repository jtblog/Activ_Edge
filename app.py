
from flask import Flask, request, Response, jsonify
from flask_mongoengine import MongoEngine
import datetime
import json
#from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db' : 'stocks',
    'host' : 'localhost',
    'port' : 27017
}
#app.config['MONGODB_SETTINGS'] = {
#    'host' : 'mongodb://localhost/audio'
#}

db = MongoEngine()
db.init_app(app)

class cDateTimeField(db.DateTimeField):
    def validate(self, value):
        super(cDateTimeField, self).validate(value)
        if(value < datetime.datetime.utcnow()):
            self.error('DateTime cannot be in the past')

class Stocks(db.DynamicDocument):
    id = db.IntField(required = True, unique = True)
    name = db.StringField(required = True, max_length = 100)
    currentPrice = db.IntField(required = True, min_value = 1)
    createDate = cDateTimeField(required = True, default = datetime.datetime.utcnow())
    lastUpdate = cDateTimeField(required = True, default = datetime.datetime.utcnow())

@app.route('/api/stocks', methods = ['POST'])
def create():
    body = request.get_json(force=True)
    dt = {}
    dt["id"] = body['id']
    dt["name"] = body['name']
    dt["currentPrice"] = body['currentPrice']
    dt["createDate"] = body['createDate']
    dt["lastUpdate"] = body['lastUpdate']

    #fmd['upload_time'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
    stock = Stocks(**dt)
    stock.save()

    return jsonify(stock)

'''
@app.route('/api/delete/<audioFileType>/<audioFileID>', methods =['DELETE'])
def delete(audioFileType, audioFileID):
    audio = Audio.objects.filter(audioFileMetadata__id = audioFileID).first()
    audio.delete()
    return jsonify({"audioFileID": str(audioFileID), "audioFileType": str(audioFileType)}), 200
'''

@app.route('/api/stocks/<id>', methods =['PUT'])
def update(id):
    body = request.get_json(force=True)
    dt = {}
    dt["id"] = id
    dt["name"] = body['name']
    dt["currentPrice"] = body['currentPrice']
    dt["createDate"] = body['createDate']
    dt["lastUpdate"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)

    #fmd['upload_time'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)

    stock = Stocks.objects.filter(id = id).first()
    stock.update(currentPrice = data["currentPrice"], lastUpdate = stock["lastUpdate"])

    return jsonify(stock), 200
    
@app.route('/api/stocks/<id>', methods =['GET'])
def get(id):
    stock = Stocks.objects.filter(id = id)
    return jsonify(stock), 200

@app.route('/api/stocks/', methods =['GET'])
def _get():
    stock = Stocks.objects()
    return jsonify(stock), 200
