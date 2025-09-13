"""
Path: src/interface_adapters/presenter/ad_account_json_presenter.py
"""

class AdAccountJsonPresenter:
    "Presenta la entidad AdAccount en formato JSON serializable."
    @staticmethod
    def present(ad_account):
        " Presenta la entidad AdAccount en formato JSON serializable."
        if ad_account is None:
            return {"error": "AdAccount not found"}
        return {
            "id": ad_account.id,
            "name": ad_account.name,
            "status": ad_account.status,
        }

    @staticmethod
    def present_error(message):
        " Presenta un mensaje de error en formato JSON."
        return {"error": message}
