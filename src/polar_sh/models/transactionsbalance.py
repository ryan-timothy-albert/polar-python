"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sh.types import BaseModel
from typing import TypedDict


class TransactionsBalanceTypedDict(TypedDict):
    currency: str
    amount: int
    account_currency: str
    account_amount: int
    

class TransactionsBalance(BaseModel):
    currency: str
    amount: int
    account_currency: str
    account_amount: int
    
