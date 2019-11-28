from io import BytesIO
from flask import Flask, request
from services.geolocator_service import GeoLocatorService
from libs.utilites.coordinator_decorator import CoordinateDecorator
from libs.exceptions.geo_exception import GeoException

app = Flask(__name__)
geo_locator_service = GeoLocatorService()


@app.route('/api/address/', methods=['GET'])
@CoordinateDecorator.validate_address_request
def to_coordinate_route():
    try:
        address = request.args.get('address')
        coordinates, code = geo_locator_service.convert_address_to_coordinates(address)
        return {"data": coordinates}, code

    except GeoException as ge:
        ge.to_dict()

    except Exception as e:
        return {"data": repr(e)}, 500


@app.route('/api/coordinates/', methods=['GET'])
@CoordinateDecorator.validate_coordinate_request
def to_address_route():
    try:
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        address, code = geo_locator_service.convert_coordinates_to_address(latitude, longitude)
        return {'data': str(address)}, 200

    except GeoException as ge:
        return ge.to_dict()

    except Exception as e:
        return {"data": repr(e)}, 500


if __name__ == '__main__':
    app.run(debug=True, port=1989, host='0.0.0.0')
