"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class ProductSortProperty(str, Enum):
    CREATED_AT = "created_at"
    MINUS_CREATED_AT = "-created_at"
    NAME = "name"
    MINUS_NAME = "-name"
    PRICE_TYPE = "price_type"
    MINUS_PRICE_TYPE = "-price_type"
    PRICE_AMOUNT_TYPE = "price_amount_type"
    MINUS_PRICE_AMOUNT_TYPE = "-price_amount_type"
    PRICE_AMOUNT = "price_amount"
    MINUS_PRICE_AMOUNT = "-price_amount"