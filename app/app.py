from io import BytesIO
from flask import Flask, request
from flask import render_template, make_response
from services.geolocator_service import GeoLocatorService

app = Flask(__name__)


@app.route('/')
def index():
    return "hello World"


if __name__ == '__main__':
    app.run(debug=True, port=1989, host='0.0.0.0')