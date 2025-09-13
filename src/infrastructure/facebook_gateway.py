"""
Path: src/infrastructure/facebook_gateway.py
"""

from facebook_business.exceptions import FacebookRequestError
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from src.use_cases.ports.ad_account_gateway_port import AdAccountGatewayPort

# Excepción personalizada para el gateway
class FacebookGatewayError(Exception):
    """Errores relacionados con la comunicación con Facebook desde el gateway."""
    def __init__(self, message, details=None):
        super().__init__(message)
        self.details = details

class FacebookGateway(AdAccountGatewayPort):
    """Adaptador para interactuar con la API de Facebook Ads."""
    def __init__(self, access_token: str, app_id: str, app_secret: str, account_id: str):
        self.access_token = access_token
        self.app_id = app_id
        self.app_secret = app_secret
        self.account_id = account_id
        self._api = None

    def initialize(self):
        "Inicializa la API de Facebook."
        self._api = FacebookAdsApi.init(
            self.app_id,
            self.app_secret,
            self.access_token
        )

    def get_account_info(self):
        "Obtiene información básica de la cuenta publicitaria."
        if not self._api:
            self.initialize()
        try:
            account = AdAccount(f'act_{self.account_id}')
            fields = [
                'id',
                'name',
                'account_status',
                'currency',
                'amount_spent',
            ]
            return account.api_get(fields=fields)
        except FacebookRequestError as e:
            error_body = e.body().get('error', {})
            details = {
                'message': error_body.get('message', str(e)),
                'code': error_body.get('code', 'N/A'),
                'type': error_body.get('type', 'N/A'),
                'fbtrace_id': error_body.get('fbtrace_id', 'N/A'),
            }
            raise FacebookGatewayError('Error en la API de Facebook', details) from e
        except Exception as e:
            raise FacebookGatewayError('Error inesperado en el gateway de Facebook',
                                       {'exception': str(e)}) from e

    def get_ad_account_info(self, account_id: str) -> dict:
        """
        Implementación del puerto. Permite obtener la información de una cuenta publicitaria por su ID.
        """
        original_account_id = self.account_id
        self.account_id = account_id
        try:
            info = self.get_account_info()
        finally:
            self.account_id = original_account_id
        return info
