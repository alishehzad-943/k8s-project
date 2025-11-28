from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """Hi, Ali Shehzad is here! 
            I am a DevOps Engineer working on a Flask application running on Kubernetes with KIND. 
            This project demonstrates containerized deployment and orchestration in a lightweight Kubernetes environment."""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
