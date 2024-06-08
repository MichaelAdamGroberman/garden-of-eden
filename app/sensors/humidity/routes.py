from flask import Blueprint, jsonify
from app.lib.lib import check_sensor_guard
from .humidity import humidity_sensor

humidity_blueprint = Blueprint('humidity', __name__)
check_sensor = check_sensor_guard(sensor=humidity_sensor, sensor_name='Humidity')

@humidity_blueprint.route('', methods=['GET'])
@check_sensor
def get_humidity():
    return jsonify(humidity='{:.2f}'.format(humidity_sensor.read()))
