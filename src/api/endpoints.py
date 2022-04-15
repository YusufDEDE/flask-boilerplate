from flask import current_app as app, request, jsonify

from .controllers.home_controller import HomeController
from utils.base_definitions import API_PREFIX


@app.route(f'{API_PREFIX}/', methods=['GET'])
def home_api():
    home_controller = HomeController()

    if request.method == 'GET':
        return home_controller.get()

    return jsonify({'status': False, 'message': 'Method Not Allowed! ... [GET] only REQUEST ACCEPTABLE!'}), 405
