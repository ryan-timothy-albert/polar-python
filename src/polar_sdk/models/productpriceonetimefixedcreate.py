"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk.types import BaseModel
import pydantic
from typing import Final, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ProductPriceOneTimeFixedCreateType(str, Enum):
    ONE_TIME = "one_time"


class ProductPriceOneTimeFixedCreateTypedDict(TypedDict):
    r"""Schema to create a one-time product price."""

    price_amount: int
    r"""The price in cents."""
    price_currency: NotRequired[str]
    r"""The currency. Currently, only `usd` is supported."""


class ProductPriceOneTimeFixedCreate(BaseModel):
    r"""Schema to create a one-time product price."""

    price_amount: int
    r"""The price in cents."""

    # fmt: off
    TYPE: Annotated[Final[ProductPriceOneTimeFixedCreateType], pydantic.Field(alias="type")] = ProductPriceOneTimeFixedCreateType.ONE_TIME # type: ignore
    # fmt: on

    price_currency: Optional[str] = "usd"
    r"""The currency. Currently, only `usd` is supported."""