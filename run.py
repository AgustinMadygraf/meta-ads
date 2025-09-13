"""
Path: run.py
"""

from src.shared.config import get_facebook_credentials
from src.shared.logger import get_logger
from src.infrastructure.facebook_gateway import FacebookGateway, FacebookGatewayError
from src.use_cases.get_ad_account_info import GetAdAccountInfoUseCase
from src.interface_adapters.controller.ad_account_controller import AdAccountController
from src.interface_adapters.presenter.ad_account_presenter import AdAccountPresenter


def main():
    " Punto de entrada principal para ejecutar la obtención de información de la cuenta publicitaria."
    logger = get_logger()
    creds = get_facebook_credentials()
    gateway = FacebookGateway(
        access_token=creds["access_token"],
        app_id=creds["app_id"],
        app_secret=creds["app_secret"],
        account_id=creds["ad_account_id"]
    )
    get_account_info_use_case = GetAdAccountInfoUseCase(gateway)
    ad_account_controller = AdAccountController(get_account_info_use_case)
    try:
        ad_account = ad_account_controller.get_account_info()
        output = AdAccountPresenter.to_cli_string(ad_account)
        logger.info(output)
    except FacebookGatewayError as e:
        logger.error("[ERROR] Facebook API: %s", e)
        if hasattr(e, 'details') and e.details:
            for k, v in e.details.items():
                logger.error("  %s: %s", k, v)
    except (KeyError, TypeError, ValueError) as e:
        logger.error("[ERROR] Error inesperado: %s", e)

if __name__ == "__main__":
    main()
