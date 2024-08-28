"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pagination import Pagination, PaginationTypedDict
from .useradvertisementcampaign import UserAdvertisementCampaign, UserAdvertisementCampaignTypedDict
from polar_sh.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class ListResourceUserAdvertisementCampaignTypedDict(TypedDict):
    pagination: PaginationTypedDict
    items: NotRequired[List[UserAdvertisementCampaignTypedDict]]
    

class ListResourceUserAdvertisementCampaign(BaseModel):
    pagination: Pagination
    items: Optional[List[UserAdvertisementCampaign]] = None
    
