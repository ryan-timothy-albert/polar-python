"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .product_input import ProductInput, ProductInputTypedDict
from enum import Enum
from polar_sh.types import BaseModel
import pydantic
from typing import Final, TypedDict
from typing_extensions import Annotated


class WebhookProductCreatedPayloadType(str, Enum):
    PRODUCT_CREATED = "product.created"

class WebhookProductCreatedPayloadTypedDict(TypedDict):
    r"""Sent when a new product is created.

    **Discord & Slack support:** Basic
    """
    
    data: ProductInputTypedDict
    r"""A product."""
    

class WebhookProductCreatedPayload(BaseModel):
    r"""Sent when a new product is created.

    **Discord & Slack support:** Basic
    """
    
    data: ProductInput
    r"""A product."""
    TYPE: Annotated[Final[WebhookProductCreatedPayloadType], pydantic.Field(alias="type")] = WebhookProductCreatedPayloadType.PRODUCT_CREATED # type: ignore
    
