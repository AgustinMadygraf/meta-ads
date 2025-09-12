"""
Path: src/interface_adapters/presenter/ad_account_presenter.py
"""

from src.entities.ad_account import AdAccount

class AdAccountPresenter:
    " Presentador para formatear la entidad AdAccount para la salida en CLI"
    @staticmethod
    def to_cli_string(ad_account: AdAccount) -> str:
        "Formatea la entidad AdAccount para su presentación en la CLI."
        if not ad_account:
            return "No se pudo obtener la información de la cuenta publicitaria."
        return (
            f"\n=== Cuenta Publicitaria ===\n"
            f"ID: {ad_account.id}\n"
            f"Nombre: {ad_account.name or '-'}\n"
            f"Estado: {ad_account.account_status}\n"
            f"Moneda: {ad_account.currency or '-'}\n"
            f"Gasto acumulado: {ad_account.amount_spent or '-'}\n"
        )
