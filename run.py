"""
Path: run.py
"""

from src.shared.config import get_facebook_credentials
from src.shared.logger import get_logger
from src.interface_adapters.gateway.facebook_gateway import FacebookGateway
from src.use_cases.get_ad_account_info import GetAdAccountInfoUseCase
from src.interface_adapters.controller.ad_account_controller import AdAccountController

logger = get_logger()

# Obtener credenciales desde variables de entorno
creds = get_facebook_credentials()


gateway = FacebookGateway(
    access_token=creds["access_token"],
    app_id=creds["app_id"],
    app_secret=creds["app_secret"],
    account_id=creds["ad_account_id"]
)


# Instanciar el caso de uso y el controlador
get_account_info_use_case = GetAdAccountInfoUseCase(gateway)
ad_account_controller = AdAccountController(get_account_info_use_case)


# Usar el controlador para obtener la información
response = ad_account_controller.get_account_info()
if response:
    logger.info("Respuesta de la API de Facebook:")
    logger.info(response)
else:
    logger.error("No se pudo obtener la información de la cuenta publicitaria.")
