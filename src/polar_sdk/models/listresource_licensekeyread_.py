"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .licensekeyread import LicenseKeyRead, LicenseKeyReadTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar_sdk.types import BaseModel
from typing import List, TypedDict


class ListResourceLicenseKeyReadTypedDict(TypedDict):
    items: List[LicenseKeyReadTypedDict]
    pagination: PaginationTypedDict
    

class ListResourceLicenseKeyRead(BaseModel):
    items: List[LicenseKeyRead]
    pagination: Pagination
    
