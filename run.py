"""
Path: run.py
"""

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.exceptions import FacebookRequestError
from src.shared.config import get_facebook_credentials
from src.shared.logger import get_logger

logger = get_logger()

# Obtener credenciales desde variables de entorno
creds = get_facebook_credentials()

# Inicializar API
FacebookAdsApi.init(
    creds["app_id"],
    creds["app_secret"],
    creds["access_token"]
)

# Obtener información básica de la cuenta publicitaria con manejo de errores
try:
    account = AdAccount(creds["ad_account_id"])
    response = account.api_get()
    logger.info("Respuesta de la API de Facebook:")
    logger.info(response)
except FacebookRequestError as e:
    logger.error("Error en la solicitud a la API de Facebook:")
    logger.error("Mensaje: %s", e.body().get('error', {}).get('message'))
    logger.error("Código: %s", e.body().get('error', {}).get('code'))
    logger.error("Tipo: %s", e.body().get('error', {}).get('type'))
    logger.error("Más detalles: %s", e.body())
except KeyError as ex:
    logger.error("Falta una clave en las credenciales o en la respuesta:")
    logger.error(str(ex))
except TypeError as ex:
    logger.error("Error de tipo de dato:")
    logger.error(str(ex))
