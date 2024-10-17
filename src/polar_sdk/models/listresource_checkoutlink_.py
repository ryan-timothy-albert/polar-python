"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .checkoutlink import CheckoutLink, CheckoutLinkTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListResourceCheckoutLinkTypedDict(TypedDict):
    items: List[CheckoutLinkTypedDict]
    pagination: PaginationTypedDict


class ListResourceCheckoutLink(BaseModel):
    items: List[CheckoutLink]

    pagination: Pagination
