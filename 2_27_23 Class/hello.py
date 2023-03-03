''' hello.py is a simple webserver '''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def hello_world():
    return "<p>About Page</p>"

@app.route("/profile")
def hello_world():
    return "<p>Anna Kolb 2/27/23</p>"

if __name__=='__main__':
    app.run(debug=True,port=5001)