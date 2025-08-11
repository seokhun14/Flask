from flask import Flask
from flask_smorest import Api
from my_books.api import blp as BookBlueprint

def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "Book Management API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)
    api.register_blueprint(BookBlueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
