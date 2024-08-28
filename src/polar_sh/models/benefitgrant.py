"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitgrantproperties import BenefitGrantProperties, BenefitGrantPropertiesTypedDict
from datetime import datetime
from polar_sh.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class BenefitGrantTypedDict(TypedDict):
    r"""A grant of a benefit to a user."""
    
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the grant."""
    is_granted: bool
    r"""Whether the benefit is granted."""
    is_revoked: bool
    r"""Whether the benefit is revoked."""
    properties: BenefitGrantPropertiesTypedDict
    r"""The properties of the grant."""
    subscription_id: Nullable[str]
    r"""The ID of the subscription that granted this benefit."""
    order_id: Nullable[str]
    r"""The ID of the order that granted this benefit."""
    user_id: str
    r"""The ID of the user concerned by this grant."""
    benefit_id: str
    r"""The ID of the benefit concerned by this grant."""
    granted_at: NotRequired[Nullable[datetime]]
    r"""The timestamp when the benefit was granted. If `None`, the benefit is not granted."""
    revoked_at: NotRequired[Nullable[datetime]]
    r"""The timestamp when the benefit was revoked. If `None`, the benefit is not revoked."""
    

class BenefitGrant(BaseModel):
    r"""A grant of a benefit to a user."""
    
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the grant."""
    is_granted: bool
    r"""Whether the benefit is granted."""
    is_revoked: bool
    r"""Whether the benefit is revoked."""
    properties: BenefitGrantProperties
    r"""The properties of the grant."""
    subscription_id: Nullable[str]
    r"""The ID of the subscription that granted this benefit."""
    order_id: Nullable[str]
    r"""The ID of the order that granted this benefit."""
    user_id: str
    r"""The ID of the user concerned by this grant."""
    benefit_id: str
    r"""The ID of the benefit concerned by this grant."""
    granted_at: OptionalNullable[datetime] = UNSET
    r"""The timestamp when the benefit was granted. If `None`, the benefit is not granted."""
    revoked_at: OptionalNullable[datetime] = UNSET
    r"""The timestamp when the benefit was revoked. If `None`, the benefit is not revoked."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["granted_at", "revoked_at"]
        nullable_fields = ["modified_at", "subscription_id", "order_id", "granted_at", "revoked_at"]
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
        
