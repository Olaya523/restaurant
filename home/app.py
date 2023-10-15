
from flask import Flask, request, jsonify, render_template


app = Flask(__name__, static_folder='templates', static_url_path='/static')

@app.route('/home')
def hola_mundo():
    return render_template('index.html')
