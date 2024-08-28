"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sh.types import BaseModel
from typing import TypedDict


class AssigneeTypedDict(TypedDict):
    id: int
    login: str
    html_url: str
    avatar_url: str
    

class Assignee(BaseModel):
    id: int
    login: str
    html_url: str
    avatar_url: str
    
