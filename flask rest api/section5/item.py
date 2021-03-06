import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query).fetchall()
        connection.close()
        return {"items": result}, 200

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="'price' field cannot be left blank")    

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE item=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {"name": row[1], "price": row[2]}

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (NULL, ?, ?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE item=?"
        cursor.execute(query, (item["price"], item["name"]))
        connection.commit()
        connection.close()
        print(item["price"], item["name"])

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        user = current_identity
        print(user.password)
        if item:
            return item
        return {"message": "Item not found."}, 404

    def post(self, name):
        item = self.find_by_name(name)
        if item:
            return {"message": "Item already exists."}
        data = Item.parser.parse_args()
        item = {"name": name, "price": data['price']}
        try:
            self.insert(item)
        except:
            return {"message": "Something went wrong on our end. Sorry about that."}, 500
        return {"message": "Successfully added item.", "item": item}, 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = {"name": name, "price": data["price"]}
        try:
            if self.find_by_name(name):
                self.update(item)
            else:
                self.insert(item)
        except:
            return {"message": "Something went wrong internally. Sorry about that."}, 500
        return {"message": "Successfully updated item.", "item": item}, 201


    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE item=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted.'}