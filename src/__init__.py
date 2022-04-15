from flask import Flask, jsonify
from flask_cors import CORS


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder='web_site/templates/',
        static_folder='web_site/static/'
    )
    app.config.from_object("config.Config")

    CORS(app)  # add CORS

    with app.app_context():
        from .web_site import routes  # Import routes
        from .api import endpoints

        @app.errorhandler(404)
        def page_not_found(e):
            # note that we set the 404 status explicitly
            return jsonify({
                "status": False,
                "message": f"Not found route! | {e}"
            }), 404

        return app
