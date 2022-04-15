from flask import current_app as app
from flask import request

from .views.home_view import HomeView


@app.route("/", methods=["GET"])
def home():
    home_view = HomeView()

    if request.method == 'GET':
        return home_view.get()
