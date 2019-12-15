from app_settings import app
from flask import request
from services.geolocator_service import GeoLocatorService
from libs.utilites.coordinator_decorator import CoordinateDecorator
from libs.exceptions.geo_exception import GeoException
from libs.utilites.config import Config


geo_locator = GeoLocatorService()

config = Config()


@app.route('/api/address/', methods=['GET'])
@CoordinateDecorator.validate_address_request
def to_coordinate_route():
    try:
        address = request.args.get('address')
        coordinates_data = geo_locator.convert_address_to_coordinates(address)
        if 'error' not in coordinates_data:
            return {"data": coordinates_data}, 200
        return coordinates_data, 404

    except GeoException as ge:
        ge.to_dict(), 500

    except Exception as e:
        return {"data": repr(e)}, 500


@app.route('/api/coordinates/', methods=['GET'])
@CoordinateDecorator.validate_coordinate_request
def to_address_route():
    try:
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        address = geo_locator.convert_coordinates_to_address(latitude, longitude)
        if 'error' not in address:
            return {'data': str(address)}, 200

        return address, 404

    except GeoException as ge:
        return {"error": ge.to_dict()}

    except Exception as e:
        return {"error": repr(e)}, 500


if __name__ == '__main__':
    app.run(debug=True, host=config.storage.get('HOST'), port=config.storage.get('PORT'))
