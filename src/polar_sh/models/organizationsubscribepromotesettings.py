"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sh.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class OrganizationSubscribePromoteSettingsTypedDict(TypedDict):
    promote: NotRequired[bool]
    r"""Promote email subscription (free)"""
    show_count: NotRequired[bool]
    r"""Show subscription count publicly"""
    count_free: NotRequired[bool]
    r"""Include free subscribers in total count"""
    

class OrganizationSubscribePromoteSettings(BaseModel):
    promote: Optional[bool] = True
    r"""Promote email subscription (free)"""
    show_count: Optional[bool] = True
    r"""Show subscription count publicly"""
    count_free: Optional[bool] = True
    r"""Include free subscribers in total count"""
    
