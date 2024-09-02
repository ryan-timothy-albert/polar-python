"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productupdate import ProductUpdate, ProductUpdateTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class ProductsUpdateRequestTypedDict(TypedDict):
    id: str
    product_update: ProductUpdateTypedDict
    

class ProductsUpdateRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    product_update: Annotated[ProductUpdate, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    