"""
Path: run.py
"""

from src.shared.config import get_facebook_credentials
from src.shared.logger import get_logger
from src.interface_adapters.gateway.facebook_gateway import FacebookGateway, FacebookGatewayError

logger = get_logger()

# Obtener credenciales desde variables de entorno
creds = get_facebook_credentials()

gateway = FacebookGateway(
    access_token=creds["access_token"],
    app_id=creds["app_id"],
    app_secret=creds["app_secret"],
    account_id=creds["ad_account_id"]
)

try:
    response = gateway.get_account_info()
    logger.info("Respuesta de la API de Facebook:")
    logger.info(response)
except FacebookGatewayError as e:
    logger.error("Error en la API de Facebook: %s", e)
    if hasattr(e, 'details') and e.details:
        for k, v in e.details.items():
            logger.error("%s: %s", k, v)
