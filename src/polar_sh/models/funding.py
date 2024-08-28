"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .currencyamount import CurrencyAmount, CurrencyAmountTypedDict
from polar_sh.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class FundingTypedDict(TypedDict):
    funding_goal: NotRequired[Nullable[CurrencyAmountTypedDict]]
    pledges_sum: NotRequired[Nullable[CurrencyAmountTypedDict]]
    r"""Sum of pledges to this isuse (including currently open pledges and pledges that have been paid out). Always in USD."""
    

class Funding(BaseModel):
    funding_goal: OptionalNullable[CurrencyAmount] = UNSET
    pledges_sum: OptionalNullable[CurrencyAmount] = UNSET
    r"""Sum of pledges to this isuse (including currently open pledges and pledges that have been paid out). Always in USD."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["funding_goal", "pledges_sum"]
        nullable_fields = ["funding_goal", "pledges_sum"]
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
        
