"""
Path: src/infrastructure/flask_app.py
"""

import os
from typing import Optional
from flask import Flask, jsonify, request, make_response, send_from_directory
from werkzeug.exceptions import HTTPException

from src.infrastructure.dependency_factory import build_ad_account_controller

# Ajusta el path a la carpeta static
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../static'))
app = Flask(__name__, static_folder=static_dir, static_url_path='/static')

def get_ad_account_controller(controller: Optional[object] = None):
    "Obtains the ad account controller, either from DI or by building a new one."
    return controller or build_ad_account_controller()

ad_account_controller = get_ad_account_controller()


@app.route('/ad_account/<account_id>', methods=['GET'])
def get_ad_account(account_id):
    "Fetches ad account information."
    try:
        result = ad_account_controller.get_account_info(account_id)
        return jsonify(result)
    except (KeyError, ValueError, TypeError) as e:
        return handle_exception(e)


@app.route('/', methods=['GET'])
def home():
    "Serve static index.html as home."
    return send_from_directory(static_dir, 'index.html')

@app.route('/ad_account', methods=['POST'])
def get_ad_account_post():
    "Fetches ad account information via POST with JSON body."
    try:
        if request.is_json:
            data = request.get_json()
            account_id = data.get('account_id')
        else:
            account_id = request.form.get('account_id')
        if not account_id:
            raise ValueError("Falta el parámetro account_id")
        result = ad_account_controller.get_account_info(account_id)
        return jsonify(result)
    except (KeyError, ValueError, TypeError) as e:
        return handle_exception(e)


# Manejo global de errores especializado
@app.errorhandler(Exception)
def handle_exception(e):
    "Manejo global de errores para la aplicación Flask."
    if isinstance(e, KeyError):
        return make_response(jsonify({"error": f"Missing key: {str(e)}"}), 400)
    if isinstance(e, (ValueError, TypeError)):
        return make_response(jsonify({"error": str(e)}), 400)
    if isinstance(e, HTTPException):
        return make_response(jsonify({"error": e.description}), e.code)
    return make_response(jsonify({"error": str(e)}), 500)

if __name__ == '__main__':
    app.run(debug=True)
