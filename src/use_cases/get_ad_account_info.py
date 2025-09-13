"""
Path: src/use_cases/get_ad_account_info.py
"""

from src.shared.logger import get_logger

from src.use_cases.ports.ad_account_gateway_port import AdAccountGatewayPort
from src.entities.ad_account import AdAccount

class GetAdAccountInfoUseCase:
    "Caso de uso para obtener información de la cuenta publicitaria."
    def __init__(self, gateway: AdAccountGatewayPort):
        self.gateway = gateway
        self.logger = get_logger()

    def execute(self):
        """
        Orquesta la obtención de información de la cuenta publicitaria.
        Aquí se pueden agregar validaciones o lógica de negocio adicional.
        """
        try:
            data = self.gateway.get_account_info()
            # Mapear los datos crudos a la entidad de dominio
            return AdAccount(
                id=data.get('id'),
                name=data.get('name'),
                account_status=data.get('account_status'),
                currency=data.get('currency'),
                amount_spent=data.get('amount_spent'),
            )
        except (KeyError, ValueError) as e:
            self.logger.error("Error al obtener información de la cuenta publicitaria: %s", e)
            details = getattr(e, 'details', None)
            if details:
                for k, v in details.items():
                    self.logger.error("%s: %s", k, v)
            return None
