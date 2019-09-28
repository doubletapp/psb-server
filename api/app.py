import argparse

from flask import Flask
from flask_mongoengine import MongoEngine
from api.handler import api_blueprint

from settings import MONGODB_SETTINGS


def port2listen():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port', help=u'Number of port to listen', type=int, default=3000
    )
    args = parser.parse_args()
    return args.port


def build_app():

    app = Flask(__name__)
    app.debug = True
    app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
    db = MongoEngine(app)

    app.register_blueprint(api_blueprint)

    return app


application = build_app()

if __name__ == "__main__":
    server = application.run('', port2listen())

    print(server)
    server.serve_forever()

