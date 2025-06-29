#!/usr/bin/env python3
# encoding: utf-8
import os
from flask import Flask, jsonify
from redis import Redis


# Get Redis connection details from environment variables
redis_host = os.getenv('REDIS_HOST', 'redis') # localhost for local testing
redis_port = int(os.getenv('REDIS_PORT', '6379'))

redis = Redis(host=redis_host, port=redis_port)
app = Flask(__name__)

@app.route('/')
def index():
    """Count and display no of page hits"""
    # inc the value of key by amount, if no key exists, the value will be initialized
    redis.incr('hits')
    counter =  str(redis.get('hits'),'utf-8')
    return f'<br> <center><p><b>🗳️ View no :{counter}</b></p></center>'

@app.route('/test',methods=['GET'])
def test():
    """Endpoint for unittesting"""
    return jsonify({"message": "Test endpoint..."})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)