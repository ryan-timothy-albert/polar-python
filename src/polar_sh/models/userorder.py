"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productprice_output import ProductPriceOutput, ProductPriceOutputTypedDict
from .userorderproduct import UserOrderProduct, UserOrderProductTypedDict
from .userordersubscription import UserOrderSubscription, UserOrderSubscriptionTypedDict
from datetime import datetime
from polar_sh.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict


class UserOrderTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    amount: int
    tax_amount: int
    currency: str
    user_id: str
    product_id: str
    product_price_id: str
    subscription_id: Nullable[str]
    product: UserOrderProductTypedDict
    product_price: ProductPriceOutputTypedDict
    subscription: Nullable[UserOrderSubscriptionTypedDict]
    

class UserOrder(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    amount: int
    tax_amount: int
    currency: str
    user_id: str
    product_id: str
    product_price_id: str
    subscription_id: Nullable[str]
    product: UserOrderProduct
    product_price: ProductPriceOutput
    subscription: Nullable[UserOrderSubscription]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at", "subscription_id", "subscription"]
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
        
