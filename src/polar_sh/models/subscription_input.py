"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .product_input import ProductInput, ProductInputTypedDict
from .productprice_input import ProductPriceInput, ProductPriceInputTypedDict
from .subscriptionstatus import SubscriptionStatus
from .subscriptionuser import SubscriptionUser, SubscriptionUserTypedDict
from datetime import datetime
from polar_sh.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict


class SubscriptionInputTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    status: SubscriptionStatus
    current_period_start: datetime
    current_period_end: Nullable[datetime]
    cancel_at_period_end: bool
    started_at: Nullable[datetime]
    ended_at: Nullable[datetime]
    user_id: str
    product_id: str
    price_id: Nullable[str]
    user: SubscriptionUserTypedDict
    product: ProductInputTypedDict
    r"""A product."""
    price: Nullable[ProductPriceInputTypedDict]
    

class SubscriptionInput(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    status: SubscriptionStatus
    current_period_start: datetime
    current_period_end: Nullable[datetime]
    cancel_at_period_end: bool
    started_at: Nullable[datetime]
    ended_at: Nullable[datetime]
    user_id: str
    product_id: str
    price_id: Nullable[str]
    user: SubscriptionUser
    product: ProductInput
    r"""A product."""
    price: Nullable[ProductPriceInput]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at", "current_period_end", "started_at", "ended_at", "price_id", "price"]
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
        
