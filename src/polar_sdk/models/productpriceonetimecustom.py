"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class ProductPriceOneTimeCustomAmountType(str, Enum):
    CUSTOM = "custom"


class ProductPriceOneTimeCustomType(str, Enum):
    r"""The type of the price."""

    ONE_TIME = "one_time"


class ProductPriceOneTimeCustomTypedDict(TypedDict):
    r"""A pay-what-you-want price for a one-time product."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the price."""
    is_archived: bool
    r"""Whether the price is archived and no longer available."""
    product_id: str
    r"""The ID of the product owning the price."""
    price_currency: str
    r"""The currency."""
    minimum_amount: Nullable[int]
    r"""The minimum amount the customer can pay."""
    maximum_amount: Nullable[int]
    r"""The maximum amount the customer can pay."""
    preset_amount: Nullable[int]
    r"""The initial amount shown to the customer."""
    amount_type: ProductPriceOneTimeCustomAmountType
    type: ProductPriceOneTimeCustomType
    r"""The type of the price."""


class ProductPriceOneTimeCustom(BaseModel):
    r"""A pay-what-you-want price for a one-time product."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the price."""

    is_archived: bool
    r"""Whether the price is archived and no longer available."""

    product_id: str
    r"""The ID of the product owning the price."""

    price_currency: str
    r"""The currency."""

    minimum_amount: Nullable[int]
    r"""The minimum amount the customer can pay."""

    maximum_amount: Nullable[int]
    r"""The maximum amount the customer can pay."""

    preset_amount: Nullable[int]
    r"""The initial amount shown to the customer."""

    AMOUNT_TYPE: Annotated[
        Annotated[
            ProductPriceOneTimeCustomAmountType,
            AfterValidator(validate_const(ProductPriceOneTimeCustomAmountType.CUSTOM)),
        ],
        pydantic.Field(alias="amount_type"),
    ] = ProductPriceOneTimeCustomAmountType.CUSTOM

    TYPE: Annotated[
        Annotated[
            ProductPriceOneTimeCustomType,
            AfterValidator(validate_const(ProductPriceOneTimeCustomType.ONE_TIME)),
        ],
        pydantic.Field(alias="type"),
    ] = ProductPriceOneTimeCustomType.ONE_TIME
    r"""The type of the price."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "modified_at",
            "minimum_amount",
            "maximum_amount",
            "preset_amount",
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
