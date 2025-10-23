#!/usr/bin/env python3
# encoding: utf-8
import os
from flask import Flask, jsonify
from redis import Redis


# Get Redis connection details from environment variables
redis_host = os.getenv('REDIS_HOST', 'redis') # localhost for local testing
redis_port = int(os.getenv('REDIS_PORT', '6379'))

# Get secret from environment variable, default to 'secret_default_value' if not set
my_secret = os.getenv('MY_SECRET', 'secret_default_value')
print(f"Application secret: {my_secret}")
print("STAAAART")
try:
    redis = Redis(host=redis_host, port=redis_port)
    # https://redis.io/docs/latest/commands/ping/, test connection
    redis.ping()
except Exception as e:
    redis = None
    print(f"Warning: Redis connection failed. Exception: {e}")

app = Flask(__name__)

@app.route('/')
def index():
    """Count and display no of page hits"""
    if redis:
        try:
            # inc the value of key by amount, if no key exists, the value will be initialized
            redis.incr('hits')
            counter = str(redis.get('hits'), 'utf-8')
            return f'<br> <center><p><b>🗳️ View no :{counter}</b></p></center>'
        except Exception as e:
            return f'<br> <center><p><b>Redis error: {e}</b></p></center>', 500
    else:
        return '<br> <center><p><b>Redis is unavailable. Please check the connection.</b></p></center>', 500

@app.route('/test',methods=['GET'])
def test():
    """Endpoint for unittesting"""
    return jsonify({"message": "Test endpoint..."})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
