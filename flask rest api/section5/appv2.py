from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from security import authenticate, identity
from user import UserRegister, UserList
from item import Item, ItemList
import create_tables

app = Flask(__name__)
app.secret_key = 'notreallysecret'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['JWT_AUTH_USERNAME_KEY'] = 'uname'
jwt = JWT(app, authenticate, identity)

@jwt.auth_response_handler
def customized_response_handler(access_token, id):
    return jsonify({
            'access_token': access_token.decode('utf-8'),
            'user_id': id.id
        })

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/userlist')

if __name__ == '__main__':
    app.run(port=5000, debug=True)