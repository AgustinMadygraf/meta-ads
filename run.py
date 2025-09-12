"""
Path: run.py
"""

from src.shared.config import get_facebook_credentials
from src.interface_adapters.gateway.facebook_gateway import FacebookGateway
from src.use_cases.get_ad_account_info import GetAdAccountInfoUseCase
from src.interface_adapters.controller.ad_account_controller import AdAccountController
from src.interface_adapters.presenter.ad_account_presenter import AdAccountPresenter

def main():
    " Punto de entrada principal para ejecutar la obtención de información de la cuenta publicitaria."
    creds = get_facebook_credentials()
    gateway = FacebookGateway(
        access_token=creds["access_token"],
        app_id=creds["app_id"],
        app_secret=creds["app_secret"],
        account_id=creds["ad_account_id"]
    )
    get_account_info_use_case = GetAdAccountInfoUseCase(gateway)
    ad_account_controller = AdAccountController(get_account_info_use_case)
    ad_account = ad_account_controller.get_account_info()
    output = AdAccountPresenter.to_cli_string(ad_account)
    print(output)

if __name__ == "__main__":
    main()
