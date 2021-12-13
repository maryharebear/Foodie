from flask import Flask
from flasgger import Swagger
def create_app():
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'Foodie',
    }
    swagger = Swagger(app)

    # Initialize Config
    app.config.from_pyfile('config.py')
    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
