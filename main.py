
from time import time
from flask import Flask, request, jsonify
from pymongo import collation
from sqlalchemy.sql.expression import update
from chat_functions import msg
from db.connect import redis_client
from chat_functions.msg import *
from api_connect.gupshup_api import send_image_message_whatsapp, send_text_message_whatsapp, send_pdf_message_whatsapp
from user_function.user_fun import get_user, update_user, reset_user
import redis
import pymongo
from pymongo import MongoClient

# initilize flask app 
app = Flask(__name__)
app.config['SECRET_KEY'] = "QWE123-EER-23-AWDDE-2234-SDFE3"

import certifi
ca = certifi.where()

cluster = MongoClient("mongodb+srv://anchitA:1234@cluster0.uqcp3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)

# mongo db initilize 
db = cluster['bot']
collections = db['bot']


# hook function 
@app.route('/bot', methods=['POST', 'GET'])
def Index():
    print(request.json)
    if request.json['payload']['type'] == 'opted-in':
        phone = request.json['payload']['phone']
        reset_user(phone, redis_client)
        user = get_user(phone, redis_client)
        return '', 200
    
    if request.json['payload']['type'] in ['sandbox-start', 'SANDBOX_START']:
        return greet, 200

    if request.json['payload']['type'] == 'text':
        phone = request.json['payload']['sender']['phone']
        timestamp = f'{request.json["timestamp"]}'
        if not collections.find_one({'_id': phone}):
            
            collections.insert_one({
                "_id": phone,
                timestamp : "" 
            }
            )
        user = get_user(phone, redis_client)
    
        if request.json['payload']['payload']['text'].lower() in ['hi', 'hello'] and user['pvalue'] == '0':
            user['pvalue'] = '1'
            update_user(phone, user, redis_client)
            # mssg = []
            # x = collections.find_one({'_id':phone})
            # # mssg.append(x[msg])
            # mssg.append(request.json['payload']['payload']['text'] )
            collections.update_one({"_id":phone}, {"$set":{timestamp : request.json['payload']['payload']['text'] }})
            return msg_1, 200
       

        if request.json['payload']['payload']['text'] == "1" and user['pvalue'] == '1':
            user['pvalue'] = '2'
            update_user(phone, user, redis_client)
            collections.update_one({"_id":phone}, {"$set":{timestamp : request.json['payload']['payload']['text'] }})
            return "This is a text", 200

        if request.json['payload']['payload']['text'] == "2" and user['pvalue'] == '1':
            user['pvalue'] = '2'
            update_user(phone, user, redis_client)
            send_image_message_whatsapp(phone, caption="Image", image=None)
            collections.update_one({"_id":phone}, {"$set":{timestamp: request.json['payload']['payload']['text'] }})
            return "", 200
        
        if request.json['payload']['payload']['text'] == "3" and user['pvalue'] == '1':
            user['pvalue'] = '2'
            update_user(phone, user, redis_client)
            #send_pdf_message_whatsapp(phone, caption="pdf", image=None)
            collections.update_one({"_id":phone}, {"$set":{timestamp : request.json['payload']['payload']['text'] }})
            return "in development **"

        if request.json['payload']['payload']['text'] == "4" and user['pvalue'] == '1':
            user['pvalue'] = '2'
            update_user(phone, user, redis_client)
            x ="['l', 'i', 's', 't']"
            collections.update_one({"_id":phone}, {"$set":{timestamp : request.json['payload']['payload']['text'] }})
            return x, 200

        if request.json['payload']['payload']['text'] == "5" and user['pvalue'] == '1':
            user['pvalue'] = '2'
            update_user(phone, user, redis_client)
            collections.update_one({"_id":phone}, {"$set":{timestamp : request.json['payload']['payload']['text'] }})
            return 'Not sure how to send buttons', 200

        if request.json['payload']['payload']['text'] == "quit":
            user['pvalue'] = '0'
            update_user(phone, user, redis_client)
            collections.update_one({"_id":phone}, {"$set":{timestamp : request.json['payload']['payload']['text'] }})
            return 'Thankyou for intracting', 200

    return "Please type a valid Input", 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)