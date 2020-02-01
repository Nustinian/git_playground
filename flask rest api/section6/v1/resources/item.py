from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="'price' field cannot be left blank")    

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found."}, 404

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {"message": "Item already exists."}
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        print(item)
        try:
            item.save_to_db()
        except:
            return {"message": "Something went wrong on our end. Sorry about that."}, 500
        return {"message": "Successfully added item.", "item": item.json()}, 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        try:
            if item:
                item.price = data['price']
            else:
                item = ItemModel(name, data['price'])
            item.save_to_db()
        except:
            return {"message": "Something went wrong internally. Sorry about that."}, 500
        return {"message": "Successfully updated item.", "item": item.json()}, 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}