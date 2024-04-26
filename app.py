from flask import Flask, request, jsonify

app = Flask(__name__)

from models.db_models import *
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
