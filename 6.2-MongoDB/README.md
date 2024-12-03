# RealEstate API

This is a Real Estate API built with Flask that provides various endpoints for managing users, houses, and predicting house prices using an ONNX model.

## Features

- User signup and signin with token-based authentication.
- Add, retrieve, and list houses in the real estate system.
- Predict house prices using an ONNX machine learning model.
- Fetch all users in the system.

## Endpoints
URL: http://127.0.0.1:5000

### 1. **GET /** - Welcome Message
Returns a simple welcome message.

### 2. **POST /** signup - User Signup
Allows a user to sign up by providing a username and password.

Keys:
username, password

### 3. **POST /** signin - User Sign In
Allows a user to sign in and receive a token.

Keys:
username, password

### 4. **POST /** add - Add House
Adds a house to the database. Requires a valid token and house details.

Keys:
token, district, area, rooms

### 5. **POST /** predict - Predict House Price
Predicts the price of a house using the ONNX model. Requires a valid token and house ID.

Keys:
token, house_id

### **6. GET /** houses - List All Houses
Fetches all houses in the database. Requires a valid token.

Keys:
token

### 7. **GET /** house/<house_id> - Get House Details
Fetches details of a specific house by its ID. Requires a valid token.

Keys:
token

### 8. **GET /** users - List All Users
Fetches a list of all users in the system.

## Dockerized
Simply run:
```
docker-compuse up
```

