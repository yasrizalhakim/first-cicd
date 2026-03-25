from flask import Flask
from redis import Redis

app = Flask (__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def home():
    count = redis.incr('visits')
    return f"This page has been visited {count} times."

@app.route("/health")
def health():
    return "App is running fine!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)