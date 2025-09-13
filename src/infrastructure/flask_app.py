"""
Path: src/infrastructure/flask_app.py
"""

from flask import Flask, jsonify

from src.shared.config import get_facebook_credentials

from src.infrastructure.facebook_gateway import FacebookGateway
from src.interface_adapters.controller.ad_account_http_controller import AdAccountHttpController

app = Flask(__name__)

def build_ad_account_controller():
    "Builds the AdAccountHttpController with necessary dependencies."
    creds = get_facebook_credentials()
    access_token = creds["access_token"]
    app_id = creds["app_id"]
    app_secret = creds["app_secret"]
    account_id = creds["ad_account_id"]

    gateway = FacebookGateway(access_token, app_id, app_secret, account_id)
    return AdAccountHttpController(gateway)

ad_account_controller = build_ad_account_controller()

@app.route('/ad_account/<account_id>', methods=['GET'])
def get_ad_account(account_id):
    "Fetches ad account information."
    result = ad_account_controller.get_account_info(account_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
