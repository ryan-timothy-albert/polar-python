"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sh.types import BaseModel
from polar_sh.utils import FieldMetadata, PathParamMetadata, SecurityMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TransactionsGetPayoutCsvSecurityTypedDict(TypedDict):
    open_id_connect: NotRequired[str]
    http_bearer: NotRequired[str]
    

class TransactionsGetPayoutCsvSecurity(BaseModel):
    open_id_connect: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="openIdConnect", field_name="Authorization"))] = None
    http_bearer: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    

class TransactionsGetPayoutCsvRequestTypedDict(TypedDict):
    id: str
    

class TransactionsGetPayoutCsvRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    
