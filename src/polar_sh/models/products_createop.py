"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productonetimecreate import ProductOneTimeCreate, ProductOneTimeCreateTypedDict
from .productrecurringcreate import ProductRecurringCreate, ProductRecurringCreateTypedDict
from polar_sh.types import BaseModel
from polar_sh.utils import FieldMetadata, SecurityMetadata
from typing import Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class ProductsCreateSecurityTypedDict(TypedDict):
    open_id_connect: NotRequired[str]
    http_bearer: NotRequired[str]
    

class ProductsCreateSecurity(BaseModel):
    open_id_connect: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="openIdConnect", field_name="Authorization"))] = None
    http_bearer: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    

ProductsCreateProductCreateTypedDict = Union[ProductOneTimeCreateTypedDict, ProductRecurringCreateTypedDict]


ProductsCreateProductCreate = Union[ProductOneTimeCreate, ProductRecurringCreate]

