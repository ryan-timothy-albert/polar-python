"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict


class MetaTypedDict(TypedDict):
    pass
    

class Meta(BaseModel):
    pass
    

class LicenseKeyActivationBaseTypedDict(TypedDict):
    id: str
    license_key_id: str
    label: str
    meta: MetaTypedDict
    created_at: datetime
    modified_at: Nullable[datetime]
    

class LicenseKeyActivationBase(BaseModel):
    id: str
    license_key_id: str
    label: str
    meta: Meta
    created_at: datetime
    modified_at: Nullable[datetime]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at"]
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
        
