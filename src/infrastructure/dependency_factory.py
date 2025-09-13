"""
Path: src/infrastructure/dependency_factory.py
"""

from typing import Optional, Dict

from src.shared.config import get_facebook_credentials
from src.infrastructure.facebook_gateway import FacebookGateway
from src.interface_adapters.controller.ad_account_http_controller import AdAccountHttpController

def build_ad_account_controller(
    creds: Optional[Dict[str, str]] = None
) -> AdAccountHttpController:
    "Factory function to build AdAccountHttpController with FacebookGateway."
    if creds is None:
        creds = get_facebook_credentials()
    access_token = creds["access_token"]
    app_id = creds["app_id"]
    app_secret = creds["app_secret"]
    account_id = creds["ad_account_id"]

    gateway = FacebookGateway(access_token, app_id, app_secret, account_id)
    from src.use_cases.get_ad_account_info import GetAdAccountInfoUseCase
    from src.interface_adapters.presenter.ad_account_json_presenter import AdAccountJsonPresenter
    use_case = GetAdAccountInfoUseCase(gateway)
    presenter = AdAccountJsonPresenter
    return AdAccountHttpController(use_case, presenter)
