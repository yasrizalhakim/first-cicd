from flask import Flask

app = Flask (__name__)

@app.route("/")
def home():
    return "hello from my CI/CD pipeline!"

@app.route("/health")
def health():
    return "App is running fine!"

@app.route("/well")
def well():
    return "App API is ONLINE!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)