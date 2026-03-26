from flask import Flask
#from redis import Redis

app = Flask (__name__)
#redis = Redis(host='redis', port=6379)

@app.route("/")
def home():
    #count = redis.incr('visits')
    #return f"This page has been visited {count} times."
    return "API is LIVE!"

@app.route("/welcome")
def welcome():
    return "Welcome to the API!"

@app.route("/health")
def health():
    return "App Health is running OK!"

@app.route("/1")
def route1():
    return "This is route 1"

@app.route("/2")
def route2():
    return "This is route 2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)