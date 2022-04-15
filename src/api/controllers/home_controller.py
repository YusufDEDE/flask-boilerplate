from flask import jsonify


class HomeController:
    def __init__(self):
        pass

    def get(self):
        return jsonify({
            "status": True,
            "message": "Welcome Home Controller!"
        }), 200
