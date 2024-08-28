"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .externalorganizationsortproperty import ExternalOrganizationSortProperty
from .listresource_externalorganization_ import ListResourceExternalOrganization, ListResourceExternalOrganizationTypedDict
from .platforms import Platforms
from polar_sh.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sh.utils import FieldMetadata, QueryParamMetadata, SecurityMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class ExternalOrganizationsListSecurityTypedDict(TypedDict):
    open_id_connect: NotRequired[str]
    http_bearer: NotRequired[str]
    

class ExternalOrganizationsListSecurity(BaseModel):
    open_id_connect: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="openIdConnect", field_name="Authorization"))] = None
    http_bearer: Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="bearer", field_name="Authorization"))] = None
    

PlatformFilterTypedDict = Union[Platforms, List[Platforms]]
r"""Filter by platform."""


PlatformFilter = Union[Platforms, List[Platforms]]
r"""Filter by platform."""


RepositoryNameFilterTypedDict = Union[str, List[str]]
r"""Filter by name."""


RepositoryNameFilter = Union[str, List[str]]
r"""Filter by name."""


ExternalOrganizationsListQueryParamOrganizationIDFilterTypedDict = Union[str, List[str]]
r"""Filter by organization ID."""


ExternalOrganizationsListQueryParamOrganizationIDFilter = Union[str, List[str]]
r"""Filter by organization ID."""


class ExternalOrganizationsListRequestTypedDict(TypedDict):
    platform: NotRequired[Nullable[PlatformFilterTypedDict]]
    r"""Filter by platform."""
    name: NotRequired[Nullable[RepositoryNameFilterTypedDict]]
    r"""Filter by name."""
    organization_id: NotRequired[Nullable[ExternalOrganizationsListQueryParamOrganizationIDFilterTypedDict]]
    r"""Filter by organization ID."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[ExternalOrganizationSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    

class ExternalOrganizationsListRequest(BaseModel):
    platform: Annotated[OptionalNullable[PlatformFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by platform."""
    name: Annotated[OptionalNullable[RepositoryNameFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by name."""
    organization_id: Annotated[OptionalNullable[ExternalOrganizationsListQueryParamOrganizationIDFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by organization ID."""
    page: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 1
    r"""Page number, defaults to 1."""
    limit: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: Annotated[OptionalNullable[List[ExternalOrganizationSortProperty]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["platform", "name", "organization_id", "page", "limit", "sorting"]
        nullable_fields = ["platform", "name", "organization_id", "sorting"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class ExternalOrganizationsListResponseTypedDict(TypedDict):
    result: ListResourceExternalOrganizationTypedDict
    

class ExternalOrganizationsListResponse(BaseModel):
    next: Callable[[], Optional[ExternalOrganizationsListResponse]]
    
    result: ListResourceExternalOrganization
    
