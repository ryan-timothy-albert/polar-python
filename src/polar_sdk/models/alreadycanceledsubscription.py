"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk import utils
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated


class AlreadyCanceledSubscriptionError(str, Enum):
    ALREADY_CANCELED_SUBSCRIPTION = "AlreadyCanceledSubscription"


class AlreadyCanceledSubscriptionData(BaseModel):
    detail: str

    ERROR: Annotated[
        Annotated[
            AlreadyCanceledSubscriptionError,
            AfterValidator(
                validate_const(
                    AlreadyCanceledSubscriptionError.ALREADY_CANCELED_SUBSCRIPTION
                )
            ),
        ],
        pydantic.Field(alias="error"),
    ] = AlreadyCanceledSubscriptionError.ALREADY_CANCELED_SUBSCRIPTION


class AlreadyCanceledSubscription(Exception):
    data: AlreadyCanceledSubscriptionData

    def __init__(self, data: AlreadyCanceledSubscriptionData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, AlreadyCanceledSubscriptionData)
