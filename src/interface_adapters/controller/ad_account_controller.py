"""
Path: src/interface_adapters/controller/ad_account_controller.py
"""

from src.use_cases.get_ad_account_info import GetAdAccountInfoUseCase


class AdAccountController:
    "Controlador para orquestar el caso de uso de obtención de información de la cuenta publicitaria."
    def __init__(self, get_account_info_use_case: GetAdAccountInfoUseCase):
        self.get_account_info_use_case = get_account_info_use_case

    def get_account_info(self, account_id):
        """
        Orquesta la obtención de información de la cuenta publicitaria.
        Devuelve la entidad AdAccount o None si hay error.
        """
        return self.get_account_info_use_case.execute(account_id)
