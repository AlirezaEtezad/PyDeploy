# Redis Python Tasks

This repository contains a Python script that demonstrates various Redis tasks using the redis Python client. Each task focuses on a specific use case, ranging from simple key-value storage to advanced use cases like rate limiting and leaderboards.

### Prerequisites

    Python 3.7 or above
    Redis server (Running locally or via Docker)
    Install the required Python package:
```
pip install redis
```
If using Docker, start a Redis container:

    docker run -d -p 6379:6379 redis

Tasks Implemented
### 1. Setup Redis Server

Verifies the Redis server connection by using the PING command.

    Method: setup_redis_server()

### 2. Hello World with Redis

Stores a simple key-value pair and retrieves it.

    Methods: hello_world_redis()
    Output: Prints "Hello World: world"

### 3. Store User Session Information

Stores session data (e.g., user ID and last login) in Redis hashes.

    Methods:
        store_session(user_id, last_login)
        retrieve_session(user_id)
    Example:

    store_session("123", "2024-09-15 10:00:00")
    retrieve_session("123")

### 4. Expire Keys

Stores a one-time password (OTP) with a 60-second expiration and verifies its availability.

    Methods:
        store_otp(user_id, otp, ttl=60)
        verify_otp_expiration(user_id)
    Example:

    store_otp("123", "987654")
    verify_otp_expiration("123")
    time.sleep(65)
    verify_otp_expiration("123")

### 5. Rate Limiter

Implements a rate limiter that restricts a user to 5 requests per minute. If the limit is exceeded, it prints a "Rate limit exceeded" message.

    Method: rate_limiter(user_id, limit, window_seconds)
    Example:

    for i in range(6):
        rate_limiter("user1", limit=5, window_seconds=60)

### 6. Leaderboard Implementation

Uses Redis sorted sets to implement a leaderboard for a game.

    Methods:
        add_user_score(leaderboard_name, user_id, score)
        get_top_users(leaderboard_name, top_n)
    Example:

    add_user_score("game_leaderboard", "user_1", 150)
    add_user_score("game_leaderboard", "user_2", 300)
    get_top_users("game_leaderboard", 3)

### 7. Batch User Data Updates with Redis Pipelines

Uses Redis pipelines to batch-insert user data efficiently. The data includes user ID, age, and score.

    Methods:
        store_users_data(users_data)
        retrieve_users_data(users_data)
    Example:

    users_data = [
        {"user_id": "user_1", "age": 25, "score": 85.5},
        {"user_id": "user_2", "age": 30, "score": 90.0},
        {"user_id": "user_3", "age": 22, "score": 76.4},
    ]
    store_users_data(users_data)
    retrieve_users_data(users_data)

How to Run the Script

    Ensure Redis is running:
        Local Redis server.
        Or, start a Redis Docker container:
```
    docker run -d -p 6379:6379 redis
```

Clone the repository or save the script locally.

Install the required Python library:
```
pip install redis
```
Run the script:

    python r_tasks.py

Script Workflow

The script performs the following:

    Verifies Redis server connection.
    Demonstrates a simple key-value store with Redis.
    Stores and retrieves user session data in Redis hashes.
    Stores a temporary OTP with expiration and verifies its availability.
    Implements a rate limiter for user requests.
    Uses Redis sorted sets to maintain a game leaderboard.
    Batch-inserts user data with Redis pipelines and retrieves it.

License

This project is licensed under the MIT License. Feel free to use and modify it as needed.