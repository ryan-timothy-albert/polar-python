"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pagination import Pagination, PaginationTypedDict
from .publicdonation import PublicDonation, PublicDonationTypedDict
from polar_sh.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class ListResourcePublicDonationTypedDict(TypedDict):
    pagination: PaginationTypedDict
    items: NotRequired[List[PublicDonationTypedDict]]
    

class ListResourcePublicDonation(BaseModel):
    pagination: Pagination
    items: Optional[List[PublicDonation]] = None
    
