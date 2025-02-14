"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscription import Subscription, SubscriptionTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class WebhookSubscriptionActivePayloadType(str, Enum):
    SUBSCRIPTION_ACTIVE = "subscription.active"


class WebhookSubscriptionActivePayloadTypedDict(TypedDict):
    r"""Sent when a subscription becomes active,
    whether because it's a new paid subscription or because payment was recovered.

    **Discord & Slack support:** Full
    """

    data: SubscriptionTypedDict
    type: WebhookSubscriptionActivePayloadType


class WebhookSubscriptionActivePayload(BaseModel):
    r"""Sent when a subscription becomes active,
    whether because it's a new paid subscription or because payment was recovered.

    **Discord & Slack support:** Full
    """

    data: Subscription

    TYPE: Annotated[
        Annotated[
            WebhookSubscriptionActivePayloadType,
            AfterValidator(
                validate_const(WebhookSubscriptionActivePayloadType.SUBSCRIPTION_ACTIVE)
            ),
        ],
        pydantic.Field(alias="type"),
    ] = WebhookSubscriptionActivePayloadType.SUBSCRIPTION_ACTIVE
