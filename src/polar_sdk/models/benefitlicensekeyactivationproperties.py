"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class BenefitLicenseKeyActivationPropertiesTypedDict(TypedDict):
    limit: int
    enable_customer_admin: bool


class BenefitLicenseKeyActivationProperties(BaseModel):
    limit: int

    enable_customer_admin: bool
