"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitlicensekeysproperties import BenefitLicenseKeysProperties, BenefitLicenseKeysPropertiesTypedDict
from datetime import datetime
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Final, TypedDict
from typing_extensions import Annotated


class BenefitLicenseKeysOutputType(str, Enum):
    LICENSE_KEYS = "license_keys"

class BenefitLicenseKeysOutputTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the benefit."""
    description: str
    r"""The description of the benefit."""
    selectable: bool
    r"""Whether the benefit is selectable when creating a product."""
    deletable: bool
    r"""Whether the benefit is deletable."""
    organization_id: str
    r"""The ID of the organization owning the benefit."""
    properties: BenefitLicenseKeysPropertiesTypedDict
    

class BenefitLicenseKeysOutput(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the benefit."""
    description: str
    r"""The description of the benefit."""
    selectable: bool
    r"""Whether the benefit is selectable when creating a product."""
    deletable: bool
    r"""Whether the benefit is deletable."""
    organization_id: str
    r"""The ID of the organization owning the benefit."""
    properties: BenefitLicenseKeysProperties
    TYPE: Annotated[Final[BenefitLicenseKeysOutputType], pydantic.Field(alias="type")] = BenefitLicenseKeysOutputType.LICENSE_KEYS # type: ignore
    
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
        
