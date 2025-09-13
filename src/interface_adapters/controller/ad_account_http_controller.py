"""
Path: src/interface_adapters/controller/ad_account_http_controller.py
"""

from src.use_cases.get_ad_account_info import GetAdAccountInfoUseCase
from src.interface_adapters.presenter.ad_account_json_presenter import AdAccountJsonPresenter

class AdAccountHttpController:
    """
    Controlador HTTP para la entidad AdAccount.
    Orquesta la obtención de información y la presentación en formato JSON.
    """
    def __init__(self, ad_account_gateway):
        self.use_case = GetAdAccountInfoUseCase(ad_account_gateway)
        self.presenter = AdAccountJsonPresenter

    def get_account_info(self, _account_id):
        " Orquesta la obtención de información de la cuenta publicitaria y la presenta en JSON."
        try:
            ad_account = self.use_case.execute()
            return self.presenter.present(ad_account)
        except (ValueError, KeyError) as e:
            return self.presenter.present_error(str(e))
