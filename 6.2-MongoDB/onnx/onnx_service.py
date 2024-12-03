from flask import Flask, request, jsonify
import onnxruntime as ort
import numpy as np

app = Flask(__name__)

# Load the ONNX model
session = ort.InferenceSession("model.onnx")


@app.route('/', methods=['GET'])
def root():
    return {"onnx_service": "running well."}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract all input features (district, area, rooms)
    district = data.get('district')
    area = data.get('area')
    rooms = data.get('rooms')

    # Check if all required features are provided
    if district is None or area is None or rooms is None:
        return jsonify({'message': 'district, area, and rooms are required'}), 400

    # Create input array for the model
    input_features = np.array([[district, area, rooms]], dtype=np.float32)

    # Run the model
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    predicted_price = session.run([output_name], {input_name: input_features})[0][0]

    return jsonify({'predicted_price': predicted_price}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
