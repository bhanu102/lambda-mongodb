#When there are large dependencies
try:
  import unzip_requirements
except ImportError:
  pass

import json
import random
from pymongo import MongoClient

def addSensorType(event, context):
    # TODO implement
    content = json.loads(event.get('body'))
    sensorName = content['sensorName']
    groupId = random.randrange(1000000000,9999999999)
    cluster = MongoClient("mongodb+srv://admin:PASSWORD@cluster0.ABCDEF.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["mytodos"]
    collection = db["todos"]
    collection.insert_one({"sensorName": sensorName, "groupId": groupId})
    return {
        'statusCode': 200,
        'body': json.dumps({"sensorName": sensorName, "groupId": groupId})
    }

def deleteSensorType(event, context):
    input_groupId = event["pathParameters"]["id"]
    cluster = MongoClient("mongodb+srv://admin:PASSWORD@cluster0.ABCDEF.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["mytodos"]
    collection = db["todos"]
    collection.delete_one({"groupId" : input_groupId})
    return {
        'statusCode': 200,
        'body': "document deleted successfully"
    }
