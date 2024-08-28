"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sh.types import BaseModel
from typing import TypedDict


class ArticlePreviewTypedDict(TypedDict):
    email: str
    r"""Email address to send the preview to. The user must be registered on Polar."""
    

class ArticlePreview(BaseModel):
    email: str
    r"""Email address to send the preview to. The user must be registered on Polar."""
    
