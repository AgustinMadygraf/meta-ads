"""
Path: src/use_cases/get_ad_account_info.py
"""


from src.interface_adapters.gateway.facebook_gateway import FacebookGateway, FacebookGatewayError
from src.shared.logger import get_logger


class GetAdAccountInfoUseCase:
    "Caso de uso para obtener información de la cuenta publicitaria."
    def __init__(self, gateway: FacebookGateway):
        self.gateway = gateway
        self.logger = get_logger()

    def execute(self):
        """
        Orquesta la obtención de información de la cuenta publicitaria.
        Aquí se pueden agregar validaciones o lógica de negocio adicional.
        """
        try:
            return self.gateway.get_account_info()
        except FacebookGatewayError as e:
            self.logger.error("Error al obtener información de la cuenta publicitaria: %s", e)
            if hasattr(e, 'details') and e.details:
                for k, v in e.details.items():
                    self.logger.error("%s: %s", k, v)
            return None
