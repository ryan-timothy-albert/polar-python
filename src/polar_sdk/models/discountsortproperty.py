"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class DiscountSortProperty(str, Enum):
    CREATED_AT = "created_at"
    MINUS_CREATED_AT = "-created_at"
    NAME = "name"
    MINUS_NAME = "-name"
    CODE = "code"
    MINUS_CODE = "-code"
    REDEMPTIONS_COUNT = "redemptions_count"
    MINUS_REDEMPTIONS_COUNT = "-redemptions_count"