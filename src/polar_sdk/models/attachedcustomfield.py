"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customfield import CustomField, CustomFieldTypedDict
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class AttachedCustomFieldTypedDict(TypedDict):
    r"""Schema of a custom field attached to a resource."""

    custom_field_id: str
    r"""ID of the custom field."""
    custom_field: CustomFieldTypedDict
    order: int
    r"""Order of the custom field in the resource."""
    required: bool
    r"""Whether the value is required for this custom field."""


class AttachedCustomField(BaseModel):
    r"""Schema of a custom field attached to a resource."""

    custom_field_id: str
    r"""ID of the custom field."""

    custom_field: CustomField

    order: int
    r"""Order of the custom field in the resource."""

    required: bool
    r"""Whether the value is required for this custom field."""