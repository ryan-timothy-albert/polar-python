"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class OrderSortProperty(str, Enum):
    CREATED_AT = "created_at"
    MINUS_CREATED_AT = "-created_at"
    AMOUNT = "amount"
    MINUS_AMOUNT = "-amount"
    USER = "user"
    MINUS_USER = "-user"
    PRODUCT = "product"
    MINUS_PRODUCT = "-product"
    SUBSCRIPTION = "subscription"
    MINUS_SUBSCRIPTION = "-subscription"
