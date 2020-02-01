from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister, UserList
import create_tables

app = Flask(__name__)
app.secret_key = 'notreallysecret'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class ItemList(Resource):
    def get(self):
        return {"items": items}

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="'price' field cannot be left blank")    

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message": "'{}' already exists.".format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if not item:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted.'}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/userlist')

app.run(port=5000, debug=True)