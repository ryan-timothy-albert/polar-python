"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_repository_ import (
    ListResourceRepository,
    ListResourceRepositoryTypedDict,
)
from .platforms import Platforms
from .repositorysortproperty import RepositorySortProperty
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


QueryParamPlatformFilterTypedDict = TypeAliasType(
    "QueryParamPlatformFilterTypedDict", Union[Platforms, List[Platforms]]
)
r"""Filter by platform."""


QueryParamPlatformFilter = TypeAliasType(
    "QueryParamPlatformFilter", Union[Platforms, List[Platforms]]
)
r"""Filter by platform."""


QueryParamRepositoryNameFilterTypedDict = TypeAliasType(
    "QueryParamRepositoryNameFilterTypedDict", Union[str, List[str]]
)
r"""Filter by name."""


QueryParamRepositoryNameFilter = TypeAliasType(
    "QueryParamRepositoryNameFilter", Union[str, List[str]]
)
r"""Filter by name."""


ExternalOrganizationNameFilterTypedDict = TypeAliasType(
    "ExternalOrganizationNameFilterTypedDict", Union[str, List[str]]
)
r"""Filter by external organization name."""


ExternalOrganizationNameFilter = TypeAliasType(
    "ExternalOrganizationNameFilter", Union[str, List[str]]
)
r"""Filter by external organization name."""


QueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "QueryParamOrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


QueryParamOrganizationIDFilter = TypeAliasType(
    "QueryParamOrganizationIDFilter", Union[str, List[str]]
)
r"""Filter by organization ID."""


class RepositoriesListRequestTypedDict(TypedDict):
    platform: NotRequired[Nullable[QueryParamPlatformFilterTypedDict]]
    r"""Filter by platform."""
    name: NotRequired[Nullable[QueryParamRepositoryNameFilterTypedDict]]
    r"""Filter by name."""
    external_organization_name: NotRequired[
        Nullable[ExternalOrganizationNameFilterTypedDict]
    ]
    r"""Filter by external organization name."""
    is_private: NotRequired[Nullable[bool]]
    r"""Filter by private status."""
    organization_id: NotRequired[Nullable[QueryParamOrganizationIDFilterTypedDict]]
    r"""Filter by organization ID."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[RepositorySortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""


class RepositoriesListRequest(BaseModel):
    platform: Annotated[
        OptionalNullable[QueryParamPlatformFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by platform."""

    name: Annotated[
        OptionalNullable[QueryParamRepositoryNameFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by name."""

    external_organization_name: Annotated[
        OptionalNullable[ExternalOrganizationNameFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by external organization name."""

    is_private: Annotated[
        OptionalNullable[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by private status."""

    organization_id: Annotated[
        OptionalNullable[QueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number, defaults to 1."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""

    sorting: Annotated[
        OptionalNullable[List[RepositorySortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "platform",
            "name",
            "external_organization_name",
            "is_private",
            "organization_id",
            "page",
            "limit",
            "sorting",
        ]
        nullable_fields = [
            "platform",
            "name",
            "external_organization_name",
            "is_private",
            "organization_id",
            "sorting",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class RepositoriesListResponseTypedDict(TypedDict):
    result: ListResourceRepositoryTypedDict


class RepositoriesListResponse(BaseModel):
    next: Callable[[], Optional[RepositoriesListResponse]]

    result: ListResourceRepository
