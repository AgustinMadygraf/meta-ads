"""
Entidad de dominio: AdAccount (Cuenta Publicitaria)
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class AdAccount:
    " Entidad que representa una cuenta publicitaria de Facebook."
    id: str
    name: Optional[str] = None
    account_status: Optional[int] = None
    currency: Optional[str] = None
    amount_spent: Optional[str] = None
