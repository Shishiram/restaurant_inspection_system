from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to store restaurants
# This should be replaced with actual Database.
restaurants = {}

@app.route('/', methods=['GET'])
def main_page():
    return "Welcome to Restaurant Inspection System"

# An API which will be exposed for the restaurant inspectors to update the new 
# restaurant information on Database
@app.route('/api/restaurants', methods=['POST'])
def create_restaurant():
    data = request.json
    business_id = data.get('business_id')
    if business_id in restaurants:
        return jsonify({'error': 'Restaurant already exists'}), 400

    restaurants[business_id] = data
    return jsonify(data), 201

# An API which will be exposed for the restaurant inspectors to update the new 
# restaurant information on Database
@app.route('/api/restaurants/<business_id>', methods=['GET'])
def get_restaurant(business_id):
    restaurant = restaurants.get(business_id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    return jsonify(restaurant)

# An API which will be exposed for the restaurant inspectors to update the existing
# restaurant information on Database
@app.route('/api/restaurants/<business_id>', methods=['PUT'])
def update_restaurant(business_id):
    data = request.json
    if business_id not in restaurants:
        return jsonify({'error': 'Restaurant not found'}), 404

    restaurants[business_id] = data
    return jsonify(data)

# An API which will be exposed for the restaurant inspectors to delete the existing
# restaurant information on Database
@app.route('/api/restaurants/<business_id>', methods=['DELETE'])
def delete_restaurant(business_id):
    if business_id not in restaurants:
        return jsonify({'error': 'Restaurant not found'}), 404

    del restaurants[business_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
