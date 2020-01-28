from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'Zackam',
        'items': [
            {
            'name': 'baseball bat',
            'price': 19.99
            },
            {
            'name': 'left airpod',
            'price': 99.97
            }
        ]
    },
    {
        'name': 'Eins',
        'items': [
            {
            'name': 'used mascara',
            'price': 3.25
            },
            {
            'name': 'depleted lozenge bag',
            'price': 1.75
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stores', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/stores/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/stores/<string:name>/items', methods=['POST'])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'something went wrong'})

@app.route('/stores/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'no items found for store'})

@app.route('/stores/<string:name>/items/<string:item>')
def get_item_in_store(name, item):
    print(item)
    for store in stores:
        if store['name'] == name:
            for thing in store['items']:
                print(thing)
                if thing['name'] == item:
                    return jsonify(thing)
    return jsonify({'message': 'item not found'})

app.run(port=5000)