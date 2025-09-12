"""
Path: src/interface_adapters/controller/ad_account_controller.py
"""

from src.use_cases.get_ad_account_info import GetAdAccountInfoUseCase
from src.interface_adapters.gateway.facebook_gateway import FacebookGatewayError

class AdAccountController:
    "Controlador para orquestar el caso de uso de obtención de información de la cuenta publicitaria."
    def __init__(self, get_account_info_use_case: GetAdAccountInfoUseCase):
        self.get_account_info_use_case = get_account_info_use_case

    def get_account_info(self):
        """
        Orquesta la obtención de información de la cuenta publicitaria.
        Devuelve la entidad AdAccount o None si hay error.
        """
        try:
            return self.get_account_info_use_case.execute()
        except FacebookGatewayError:
            # El caso de uso ya loguea el error, aquí solo se puede propagar o adaptar la respuesta
            return None
