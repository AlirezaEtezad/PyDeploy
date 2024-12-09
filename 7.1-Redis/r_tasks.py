import redis
import time

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)


# 1. Setup Redis Server (Verified connection)
def setup_redis_server():
    print(redis_client.ping())  # Should print True

# 2. Hello World with Redis and Python
def hello_world_redis():
    redis_client.set("hello", "world")
    print("Hello World:", redis_client.get("hello"))  # Outputs: world

# 3. Store User Session Information

def store_session(user_id, last_login):
    """
    Stores user session information in Redis.
    
    :param user_id: User ID
    :param last_login: Last login time
    """
    session_key = f"session:{user_id}"
    session_data = {
        "user_id": user_id,
        "last_login": last_login
    }
    redis_client.hset(session_key, mapping=session_data)
    print(f"Session stored for user {user_id}: {session_data}")

def retrieve_session(user_id):
    """
    Retrieves user session information from Redis.
    
    :param user_id: User ID
    :return: Session data as a dictionary
    """
    session_key = f"session:{user_id}"
    session_data = redis_client.hgetall(session_key)
    if session_data:
        print(f"Session retrieved for user {user_id}: {session_data}")
    else:
        print(f"No session data found for user {user_id}")
    return session_data


# 4. Expire Keys
def store_otp(user_id, otp, ttl=60):
    """
    Stores a one-time password (OTP) for a user with a specific expiration time.
    
    :param user_id: User ID
    :param otp: OTP to store
    :param ttl: Time-to-live for the OTP in seconds (default is 60 seconds)
    """
    otp_key = f"otp:{user_id}"
    redis_client.setex(otp_key, ttl, otp)
    print(f"OTP '{otp}' for user '{user_id}' stored with a TTL of {ttl} seconds.")

def verify_otp_expiration(user_id):
    """
    Verifies if the OTP for the user still exists in Redis.
    
    :param user_id: User ID
    :return: True if the OTP exists, False otherwise
    """
    otp_key = f"otp:{user_id}"
    otp = redis_client.get(otp_key)
    if otp:
        print(f"OTP for user '{user_id}' is still available: {otp}")
        return True
    else:
        print(f"OTP for user '{user_id}' has expired or does not exist.")
        return False
    


# 5. Rate Limiter
def rate_limiter(user_id, limit, window_seconds):
    key = f"rate:{user_id}"
    current_count = redis_client.incr(key)
    if current_count == 1:
        redis_client.expire(key, window_seconds)
    if current_count > limit:
        print("Rate limit exceeded")
        return False
    print(f"Request allowed. Current count: {current_count}")
    return True

# 6. Leaderboard Implementation
def add_user_score(leaderboard_name, user_id, score):
    """
    Adds a user and their score to the leaderboard.
    
    :param leaderboard_name: Name of the leaderboard
    :param user_id: User ID
    :param score: User's score
    """
    redis_client.zadd(leaderboard_name, {user_id: score})
    print(f"Added user '{user_id}' with score {score} to leaderboard '{leaderboard_name}'.")

def get_top_users(leaderboard_name, top_n):
    """
    Retrieves the top N users from the leaderboard.
    
    :param leaderboard_name: Name of the leaderboard
    :param top_n: Number of top users to retrieve
    :return: List of tuples containing user IDs and their scores
    """
    top_users = redis_client.zrevrange(leaderboard_name, 0, top_n - 1, withscores=True)
    print(f"Top {top_n} users from leaderboard '{leaderboard_name}':")
    for rank, (user, score) in enumerate(top_users, start=1):
        print(f"{rank}. {user} - {score}")
    return top_users

# 7. Batch User Data Updates with Redis Pipelines
def store_users_data(users_data):
    """
    Stores a list of user data in Redis using a pipeline for efficiency.
    
    :param users_data: List of dictionaries, each containing 'user_id', 'age', and 'score'
    """
    pipeline = redis_client.pipeline()
    
    for user in users_data:
        user_key = f"user:{user['user_id']}"
        pipeline.hmset(user_key, {"age": user["age"], "score": user["score"]})
    
    # Execute the pipeline
    pipeline.execute()
    print("User data stored successfully.")

def retrieve_users_data(users_data):
    """
    Retrieves and prints user data from Redis.
    
    :param users_data: List of dictionaries, each containing 'user_id', 'age', and 'score'
    """
    for user in users_data:
        user_key = f"user:{user['user_id']}"
        user_data = redis_client.hgetall(user_key)
        print(f"Data for {user['user_id']}: {user_data}")




# Run the tasks
if __name__ == "__main__":
    user_id = "123"
    last_login = "2024-09-15 10:00:00"
    otp = "987654"
    #1
    setup_redis_server()
    #2
    hello_world_redis()
    #3  
    store_session(user_id, last_login)
    retrieve_session(user_id)
    #4
    store_otp(user_id, otp)
    # Verify OTP before expiration
    verify_otp_expiration(user_id)
    # Wait 65 seconds to ensure the OTP expires
    print("Waiting for 65 seconds...")
    time.sleep(65)
    # Verify OTP after expiration
    verify_otp_expiration(user_id)

    #5
    # set_key_with_expiry("temp_key", "temp_value", 10)
    for i in range(9):  # Simulate 5 requests
        rate_limiter("user1", limit=5, window_seconds=10)

    #6
    leaderboard = "game_leaderboard"
    
    # Add users and their scores
    add_user_score(leaderboard, "user_1", 150)
    add_user_score(leaderboard, "user_2", 300)
    add_user_score(leaderboard, "user_3", 200)
    add_user_score(leaderboard, "user_4", 250)
    
    # Retrieve and print the top 3 users
    get_top_users(leaderboard, 3)
   

   #7
    users_data = [
        {"user_id": "user_1", "age": 25, "score": 85.5},
        {"user_id": "user_2", "age": 30, "score": 90.0},
        {"user_id": "user_3", "age": 22, "score": 76.4},
    ]
    
    store_users_data(users_data)
    retrieve_users_data(users_data)
