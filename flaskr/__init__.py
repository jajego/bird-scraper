import os

from scraper import getImageUrls

from flask import Flask
from flask import request
from flask import jsonify

from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5001)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/', methods=("GET", "POST", "OPTIONS"))
    def getUrls():
        print('Hello from / route')
        if request.method == "GET":
            birds = [];
            print(request.args)
            for arg in request.args:
                birds.append(request.args.get(arg))        
            urls = getImageUrls(birds)
            return urls

    return app