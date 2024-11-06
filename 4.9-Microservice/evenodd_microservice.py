from flask import Flask, jsonify
import requests

app = Flask(__name__)

random_microservice_url = "http://127.0.0.1:8001/generate"

# Calling the random number generator microservice
def call_random_microservie():
	response = requests.get(random_microservice_url)
	return response.json().get("random_number")

@app.route("/check", methods=['GET'])
def check_even_odd():
	random_number = call_random_microservie()
	result = "even" if random_number % 2 == 0 else "odd"
	return jsonify({"random_number": random_number, "result": result})

if __name__ == "__main__":
	app.run(port=8002)
