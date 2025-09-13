"""
Path: src/use_cases/ports/ad_account_gateway_port.py
"""

from abc import ABC, abstractmethod

class AdAccountGatewayPort(ABC):
    "Puerto de interfaz para el gateway de la cuenta publicitaria."
    @abstractmethod
    def get_ad_account_info(self, account_id: str) -> dict:
        """
        Obtiene la información de una cuenta publicitaria por su ID.
        :param account_id: ID de la cuenta publicitaria
        :return: Diccionario con la información de la cuenta
        """
        pass # pylint: disable=unnecessary-pass
