import sys
from flask import Flask
from flask import request as r
import requests
import jwt

def text_response(text):
    return {'fulfillmentText': text}

def intent_handler_pair(request):
    email = jwt.decode(request['originalDetectIntentRequest']['payload']['user']['idToken'], verify=False)['email']
    id = request['queryResult']['parameters']['any']

    l = requests.post('http://smart-amplifier-api.radimkozak.com/pair/new/amplifier', {'email': email, 'amplifier': id})

    if l.status_code == 200:
        return text_response('You amplifier with id {} was paired to your email'.format(id)), 200

    return text_response('Error pairing amplifier with id {}. Make sure it is valid and registred amplifier'.format(id)), 200

def intent_handler_volume(request):
    volume = request['queryResult']['parameters']['percentage'][:-1]
    email = jwt.decode(request['originalDetectIntentRequest']['payload']['user']['idToken'], verify=False)['email']

    l = requests.post('http://smart-amplifier-api.radimkozak.com/change/volume/by/email', {'email': email, 'volume': volume})

    if l.status_code == 200:
        return text_response('Volume was changed to {} %'.format(volume)), 200

    return text_response('Error while setting volume. Did you pair your amplifier. You can do it by saying or texting "Pair new amplifier <id>"'), 200

def main():
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def route():
        try:
            request = r.get_json(silent=True)
            intent = request['queryResult']['intent']['displayName']

            if intent == 'Volume':
                return intent_handler_volume(request)

            if intent == 'Pair new amplifier':
                return intent_handler_pair(request)

            return text_response('Error while setting volume. Pair your account with amplifier'), 200
        except Exception:
            return text_response('Error while setting volume'), 200
    
    app.run('0.0.0.0', '8080')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)