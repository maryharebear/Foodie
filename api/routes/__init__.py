from http import HTTPStatus
from flask import Blueprint, render_template
from flasgger import swag_from

from api.schema.pages import PagesSchema

home_api = Blueprint('api', __name__)

@home_api.route('/', methods=["GET"])
@home_api.route('/index', methods=["GET"])
@home_api.route('/login', methods=["GET"])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Login Page',
            'schema': PagesSchema
        }
    }
})
def loginPage():
    return render_template('login.html')


