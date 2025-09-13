"""
Path: src/interface_adapters/controller/ad_account_http_controller.py
"""



class AdAccountHttpController:
    """
    Controlador HTTP para la entidad AdAccount.
    Orquesta la obtención de información y la presentación en formato JSON.
    """
    def __init__(self, use_case, presenter):
        self.use_case = use_case
        self.presenter = presenter

    def get_account_info(self, account_id):
        " Orquesta la obtención de información de la cuenta publicitaria y la presenta en JSON."
        try:
            ad_account = self.use_case.execute(account_id)
            return self.presenter.present(ad_account)
        except (ValueError, KeyError) as e:
            return self.presenter.present_error(str(e))
