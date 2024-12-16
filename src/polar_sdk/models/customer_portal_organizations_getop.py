"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class CustomerPortalOrganizationsGetRequestTypedDict(TypedDict):
    slug: str
    r"""The organization slug."""


class CustomerPortalOrganizationsGetRequest(BaseModel):
    slug: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The organization slug."""
