"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class AdvertisementSortProperty(str, Enum):
    CREATED_AT = "created_at"
    MINUS_CREATED_AT = "-created_at"
    GRANTED_AT = "granted_at"
    MINUS_GRANTED_AT = "-granted_at"
    VIEWS = "views"
    MINUS_VIEWS = "-views"
    CLICKS = "clicks"
    MINUS_CLICKS = "-clicks"
