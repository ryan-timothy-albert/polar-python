"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar.types import BaseModel
from polar.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class ArticlesDeleteRequestTypedDict(TypedDict):
    id: str
    

class ArticlesDeleteRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    