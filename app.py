#app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello_world'

@app.route('/abc')
def deleteform(num):
    return 'hello_abc'

if __name__=='__main__':
    app.run('0.0.0.0')