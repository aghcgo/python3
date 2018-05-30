from flask import Flask
from werkzeug import DispatcherMiddleware
 
app1 = Flask(__name__)
app2 = Flask(__name__)
app = Flask(__name__)
 
@app1.route('/')
def index():
    return "This is app1!"
 
@app2.route('/')
def index():
    return "This is app2!"
 
@app.route('/')
def index():
    return "This is app!"
 
app = DispatcherMiddleware(app, {
            '/app1':        app1,
            '/app2':        app2
        })
 
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('192.168.1.99',5000, app)
