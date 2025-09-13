"""
Path: run.py
"""

import sys

from src.shared.config import get_facebook_credentials
from src.shared.logger import get_logger

from src.infrastructure.facebook_gateway import FacebookGateway, FacebookGatewayError
from src.interface_adapters.controller.ad_account_controller import AdAccountController
from src.interface_adapters.presenter.ad_account_presenter import AdAccountPresenter
from src.use_cases.get_ad_account_info import GetAdAccountInfoUseCase

def main():
    " Punto de entrada principal para ejecutar la obtención de información de la cuenta publicitaria."
    logger = get_logger()
    creds = get_facebook_credentials()
    app_id = creds.get("app_id")
    if not app_id or app_id.strip() == "":
        logger.warning("FACEBOOK_APP_ID: ❌ No definido o vacío en .env")
    else:
        logger.info("FACEBOOK_APP_ID: ✅ '%s' (OK)", app_id)
    access_token = creds.get("access_token")
    if not access_token or access_token.strip() == "":
        logger.warning("FACEBOOK_ACCESS_TOKEN: ❌ No definido o vacío en .env")
    else:
        masked_token = f"{access_token[:4]}...{access_token[-4:]}" if len(access_token) > 8 else access_token
        logger.info("FACEBOOK_ACCESS_TOKEN: ✅ '%s' (OK)", masked_token)


    # Validación explícita de AD_ACCOUNT_ID
    ad_account_id = creds.get("ad_account_id")
    if not ad_account_id or ad_account_id.strip() == "":
        logger.warning("AD_ACCOUNT_ID: ❌ No definido o vacío en .env")
    else:
        logger.info("AD_ACCOUNT_ID: ✅ '%s' (OK)", ad_account_id)

    # Validación explícita de FACEBOOK_APP_SECRET
    app_secret = creds.get("app_secret")
    if not app_secret or app_secret.strip() == "":
        logger.warning("FACEBOOK_APP_SECRET: ❌ No definido o vacío en .env")
    else:
        masked = f"{app_secret[:4]}...{app_secret[-4:]}" if len(app_secret) > 8 else app_secret
        logger.info("FACEBOOK_APP_SECRET: ✅ '%s' (OK)", masked)

    gateway = FacebookGateway(
        access_token=creds["access_token"],
        app_id=creds["app_id"],
        app_secret=creds["app_secret"],
        account_id=ad_account_id
    )
    get_account_info_use_case = GetAdAccountInfoUseCase(gateway)
    ad_account_controller = AdAccountController(get_account_info_use_case)
    try:
        ad_account = ad_account_controller.get_account_info(ad_account_id)
        output = AdAccountPresenter.to_cli_string(ad_account)
        logger.info(output)
    except FacebookGatewayError as e:
        logger.error("Facebook API: %s", e)
        if hasattr(e, 'details') and e.details:
            for k, v in e.details.items():
                logger.error("  %s: %s", k, v)
    except (KeyError, TypeError, ValueError) as e:
        logger.error("Error inesperado: %s", e)

if __name__ == "__main__":
    if "--flask" in sys.argv:
        from src.infrastructure.flask_app import app
        app.run(debug=True)
    else:
        main()
