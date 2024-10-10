"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .checkoutconfirmstripe import CheckoutConfirmStripe, CheckoutConfirmStripeTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class CheckoutsCustomClientConfirmRequestTypedDict(TypedDict):
    client_secret: str
    r"""The checkout session client secret."""
    checkout_confirm_stripe: CheckoutConfirmStripeTypedDict


class CheckoutsCustomClientConfirmRequest(BaseModel):
    client_secret: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The checkout session client secret."""

    checkout_confirm_stripe: Annotated[
        CheckoutConfirmStripe,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]