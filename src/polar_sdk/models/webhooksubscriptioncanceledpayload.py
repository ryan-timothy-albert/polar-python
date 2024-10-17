"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscription_input import SubscriptionInput, SubscriptionInputTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class WebhookSubscriptionCanceledPayloadType(str, Enum):
    SUBSCRIPTION_CANCELED = "subscription.canceled"


class WebhookSubscriptionCanceledPayloadTypedDict(TypedDict):
    r"""Sent when a subscription is canceled by the user.
    They might still have access until the end of the current period.

    **Discord & Slack support:** Full
    """

    data: SubscriptionInputTypedDict
    type: WebhookSubscriptionCanceledPayloadType


class WebhookSubscriptionCanceledPayload(BaseModel):
    r"""Sent when a subscription is canceled by the user.
    They might still have access until the end of the current period.

    **Discord & Slack support:** Full
    """

    data: SubscriptionInput

    TYPE: Annotated[
        Annotated[
            WebhookSubscriptionCanceledPayloadType,
            AfterValidator(
                validate_const(
                    WebhookSubscriptionCanceledPayloadType.SUBSCRIPTION_CANCELED
                )
            ),
        ],
        pydantic.Field(alias="type"),
    ] = WebhookSubscriptionCanceledPayloadType.SUBSCRIPTION_CANCELED