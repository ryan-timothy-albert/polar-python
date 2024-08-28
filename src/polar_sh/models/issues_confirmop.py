"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .confirmissue import ConfirmIssue, ConfirmIssueTypedDict
from polar_sh.types import BaseModel
from polar_sh.utils import FieldMetadata, PathParamMetadata, RequestMetadata, SecurityMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class IssuesConfirmSecurityTypedDict(TypedDict):
    open_id_connect: NotRequired[str]
    http_bearer: NotRequired[str]
    

class IssuesConfirmSecurity(BaseModel):
    open_id_connect: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="openIdConnect", field_name="Authorization"))] = None
    http_bearer: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    

class IssuesConfirmRequestTypedDict(TypedDict):
    id: str
    confirm_issue: ConfirmIssueTypedDict
    

class IssuesConfirmRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    confirm_issue: Annotated[ConfirmIssue, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
