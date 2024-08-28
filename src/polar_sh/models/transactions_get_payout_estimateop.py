"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sh.types import BaseModel
from polar_sh.utils import FieldMetadata, QueryParamMetadata, SecurityMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TransactionsGetPayoutEstimateSecurityTypedDict(TypedDict):
    open_id_connect: NotRequired[str]
    http_bearer: NotRequired[str]
    

class TransactionsGetPayoutEstimateSecurity(BaseModel):
    open_id_connect: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="openIdConnect", field_name="Authorization"))] = None
    http_bearer: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    

class TransactionsGetPayoutEstimateRequestTypedDict(TypedDict):
    account_id: str
    

class TransactionsGetPayoutEstimateRequest(BaseModel):
    account_id: Annotated[str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    
