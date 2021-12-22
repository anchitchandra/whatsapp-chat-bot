import random
import requests


def get_headers():
    headers = {'Cache-Control': 'no-cache',
               'Content-Type': 'application/x-www-form-urlencoded',
               'apikey': "djpazg6jitckayc4hemviksudrdshzoj"}
    return headers


def get_request_body(phone):
    databody = {
        'channel': 'whatsapp',
        'source': "917834811114",
        'destination': phone,
        'message': None,
        'src.name': 'bcetbot'}
    return databody


def make_post_request(databody):
    response = requests.post(
        url="https://api.gupshup.io/sm/api/v1/msg",
        data=databody,
        headers=get_headers())
    return response


def send_text_message_whatsapp(phone, message):

    message_body = {
        "type": "text",
        "text": message
    }
    databody = get_request_body(phone)
    databody['message'] = str(message_body)
    return make_post_request(databody)


def send_image_message_whatsapp(phone, caption, image):

    prew = ["https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg","https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample02.jpg","https://www.buildquickbots.com/whatsapp/media/sample/png/sample02.png","https://www.buildquickbots.com/whatsapp/media/sample/png/sample01.png"]
    image = random.choice(prew)

    message_body = {
        'type': 'image',
        'originalUrl': image,
        'previewUrl': image,
        'caption': caption
    }
    databody = get_request_body(phone)
    databody['message'] = str(message_body)

    return make_post_request(databody)

def send_pdf_message_whatsapp(phone, caption, image):

    image = 'http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf'

    message_body = {
        'type': 'file',
        'url': image
    }
    databody = get_request_body(phone)
    databody['message'] = str(message_body)
    print(databody)
    return make_post_request(databody)