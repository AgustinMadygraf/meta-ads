"""
Path: src/shared/config.py
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def get_facebook_credentials():
    "Obtener credenciales de Facebook desde variables de entorno."
    return {
        "app_id": os.getenv("FACEBOOK_APP_ID"),
        "app_secret": os.getenv("FACEBOOK_APP_SECRET"),
        "access_token": os.getenv("FACEBOOK_ACCESS_TOKEN"),
        "ad_account_id": os.getenv("AD_ACCOUNT_ID"),
    }
