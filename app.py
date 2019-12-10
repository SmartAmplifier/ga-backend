import sys
from flask import Flask
from flask import request as r
import requests
import jwt

def main():
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def route():
        try:
            request = r.get_json(silent=True)
            volume = request['queryResult']['parameters']['percentage'][:-1]
            email = jwt.decode(request['originalDetectIntentRequest']['payload']['user']['idToken'], verify=False)['email']

            l = requests.post('http://smart-amplifier-api.radimkozak.com/change/volume/by/email', {'email': email, 'volume': volume})

            if l.status_code == 200:
                return {'fulfillmentText': 'Volume was changed to {} %'.format(volume)}, 200
            
            return {'fulfillmentText': 'Error while setting volume. Pair your account with amplifier'}, 200
        except Exception:
            return {'fulfillmentText': 'Error while setting volume'}, 200

        print(volume)

        return 'neco'
    app.run('0.0.0.0', '8080')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)