from flask import Flask, abort, request
import json
import os


app = Flask(__name__)


POSSIBLE_ATTRIBUTES = {
    'id': (type(1),), 
    'directors': (type([1,1]),), 
    'genre': (type('1'),), 
    'year': (type(1)), 
    'name': (type('1'),)
}


with open(os.path.dirname(__file__) + '/books.json', 'r') as file:
    data = json.load(file)
    BOOKS = {int(key): value for key, value in data.items()}



def dump_data(data):
    with open(os.path.dirname(__file__) + '/books.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def validate_car(good):
    for key, value in good.items():
        if key not in POSSIBLE_ATTRIBUTES and not isinstance(value, POSSIBLE_ATTRIBUTES.get(key)):
            return False
    return len(POSSIBLE_ATTRIBUTES) == len(good)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/books', methods=['GET'])
def show_all():
    return BOOKS


@app.route('/books/<id>', methods=['GET'])
def show_one(id):
    return BOOKS.get(int(id)) if int(id) in BOOKS else abort(404)


@app.route('/books', methods=['POST'])
def store():
    recieved_data = request.get_json()

    if not validate_car(recieved_data):
        return 406

    if BOOKS.get(recieved_data['id']):
        return 409

    BOOKS[recieved_data['id']] = recieved_data

    dump_data(BOOKS)

    return BOOKS

def validate_modification(data):
    for key, value in data.items():
        if key not in POSSIBLE_ATTRIBUTES or not isinstance(value, POSSIBLE_ATTRIBUTES.get(key)):
            return False
    return True


@app.route('/books/<id>', methods=['PATCH'])
def modify_book(id):
    recieved_data = request.get_json()

    if not validate_modification(recieved_data):
        return 406

    print(BOOKS)

    print(id, type(id), '!!!')

    BOOKS[int(id)] = BOOKS[int(recieved_data['id'])] | recieved_data

    print(BOOKS)

    dump_data(BOOKS)

    return BOOKS[int(id)]


@app.route('/books/<id>', methods=['DELETE'])
def delete_books(id):
    try:
        BOOKS.pop(int(id))
        dump_data(BOOKS)
    except KeyError:
        return abort(404)


def run():
    app.run(debug=True)

        
if __name__ == '__main__':
    run()
