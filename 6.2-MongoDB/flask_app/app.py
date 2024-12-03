from flask import Flask, request, jsonify
from database import User, House
import requests  # For calling the ONNX microservice

app = Flask(__name__)

# Example ONNX microservice URL (change if needed)
ONNX_SERVICE_URL = "http://onnx-service:8000/predict"


@app.route('/', methods=['GET'])
def route():
    return jsonify({'Welcome': 'This is a RealEstate API'})


@app.route('/signup', methods=['POST'])
def signup():
    data = request.args  # Use query params
    if User.objects(username=data.get('username')).first():
        return jsonify({'message': 'User already exists'}), 400
    User(username=data.get('username'), password=data.get('password')).save()
    return jsonify({'message': 'Signup successful'}), 201


@app.route('/signin', methods=['POST'])
def signin():
    data = request.args  # Use query params
    user = User.objects(username=data.get('username')).first()
    if user and user.password == data.get('password'):
        # Generate a token (for simplicity, return the username as token)
        token = user.username
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/add', methods=['POST'])
def add_house():
    token = request.args.get('token')
    district = request.args.get('district')
    area = request.args.get('area')
    rooms = request.args.get('rooms')

    # Validate the token
    
    if not token or not User.objects(username=token).first():
        
        return jsonify({'message': 'Unauthorized'}), 401

    # Validate district
    valid_districts = ['downtown', 'uptown', 'suburb', 'countryside', 'industrial', 'residential']
    if district not in valid_districts:
        return jsonify({'message': f'Invalid district. Valid districts: {", ".join(valid_districts)}'}), 400

    # Check required fields
    if not all([district, area, rooms]):
        return jsonify({'message': 'Missing required parameters'}), 400

    # Save house to database
    house = House(district=district, area=int(area), rooms=int(rooms))
    house.save()

    return jsonify({
        'message': 'House added successfully',
        'house_id': str(house.id)
    }), 201



@app.route('/predict', methods=['POST'])
def predict_price():
    # Extract token and house_id from query parameters
    token = request.args.get('token')
    house_id = request.args.get('house_id')

    # Validate the token
    if not token or not User.objects(username=token).first():
        return jsonify({'message': 'Unauthorized'}), 401

    # Validate the house_id
    if not house_id:
        return jsonify({'message': 'house_id is required'}), 400

    # Fetch house details from the database
    house = House.objects(id=house_id).first()
    if not house:
        return jsonify({'message': 'House not found'}), 404

    # Prepare data for prediction
    prediction_payload = {
        "district": house.district,
        "area": house.area,
        "rooms": house.rooms
    }

    # Call the ONNX prediction microservice
    try:
        response = requests.post("http://onnx-service:8000/predict", json=prediction_payload)
        response.raise_for_status()
        predicted_price = response.json().get("predicted_price")
    except requests.exceptions.RequestException as e:
        return jsonify({'message': f'Error calling prediction service: {str(e)}'}), 500

    return jsonify({
        'house_id': str(house.id),
        'predicted_price': predicted_price
    }), 200

@app.route('/houses', methods=['GET'])
def get_all_houses():
    token = request.args.get('token')

    # Validate the token
    if not token or not User.objects(username=token).first():
        return jsonify({'message': 'Unauthorized'}), 401

    # Fetch all houses
    houses = House.objects()
    houses_list = [{
        'id': str(house.id),
        'district': house.district,
        'area': house.area,
        'rooms': house.rooms
    } for house in houses]

    return jsonify(houses_list), 200


@app.route('/house/<house_id>', methods=['GET'])
def get_house(house_id):
    token = request.args.get('token')

    # Validate the token
    if not token or not User.objects(username=token).first():
        return jsonify({'message': 'Unauthorized'}), 401

    # Fetch the house by ID
    house = House.objects(id=house_id).first()
    if not house:
        return jsonify({'message': 'House not found'}), 404

    return jsonify({
        'id': str(house.id),
        'district': house.district,
        'area': house.area,
        'rooms': house.rooms
    }), 200

@app.route('/users', methods=['GET'])
def get_all_users():
    # Fetch all users
    users = User.objects()
    users_list = [{'username': user.username} for user in users]

    return jsonify(users_list), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
