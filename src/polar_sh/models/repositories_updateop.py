"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .repositoryupdate import RepositoryUpdate, RepositoryUpdateTypedDict
from polar_sh.types import BaseModel
from polar_sh.utils import FieldMetadata, PathParamMetadata, RequestMetadata, SecurityMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RepositoriesUpdateSecurityTypedDict(TypedDict):
    open_id_connect: NotRequired[str]
    http_bearer: NotRequired[str]
    

class RepositoriesUpdateSecurity(BaseModel):
    open_id_connect: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="openIdConnect", field_name="Authorization"))] = None
    http_bearer: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    

class RepositoriesUpdateRequestTypedDict(TypedDict):
    id: str
    repository_update: RepositoryUpdateTypedDict
    

class RepositoriesUpdateRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    repository_update: Annotated[RepositoryUpdate, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
