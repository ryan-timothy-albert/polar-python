"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitads import BenefitAds, BenefitAdsTypedDict
from .benefitarticles import BenefitArticles, BenefitArticlesTypedDict
from .benefitcustom import BenefitCustom, BenefitCustomTypedDict
from .benefitdiscord_input import BenefitDiscordInput, BenefitDiscordInputTypedDict
from .benefitdownloadables import BenefitDownloadables, BenefitDownloadablesTypedDict
from .benefitgithubrepository import BenefitGitHubRepository, BenefitGitHubRepositoryTypedDict
from enum import Enum
from polar_sh.types import BaseModel
import pydantic
from typing import Final, TypedDict, Union
from typing_extensions import Annotated


class WebhookBenefitUpdatedPayloadType(str, Enum):
    BENEFIT_UPDATED = "benefit.updated"

WebhookBenefitUpdatedPayloadDataTypedDict = Union[BenefitArticlesTypedDict, BenefitAdsTypedDict, BenefitDiscordInputTypedDict, BenefitGitHubRepositoryTypedDict, BenefitDownloadablesTypedDict, BenefitCustomTypedDict]


WebhookBenefitUpdatedPayloadData = Union[BenefitArticles, BenefitAds, BenefitDiscordInput, BenefitGitHubRepository, BenefitDownloadables, BenefitCustom]


class WebhookBenefitUpdatedPayloadTypedDict(TypedDict):
    r"""Sent when a benefit is updated.

    **Discord & Slack support:** Basic
    """
    
    data: WebhookBenefitUpdatedPayloadDataTypedDict
    

class WebhookBenefitUpdatedPayload(BaseModel):
    r"""Sent when a benefit is updated.

    **Discord & Slack support:** Basic
    """
    
    data: WebhookBenefitUpdatedPayloadData
    TYPE: Annotated[Final[WebhookBenefitUpdatedPayloadType], pydantic.Field(alias="type")] = WebhookBenefitUpdatedPayloadType.BENEFIT_UPDATED # type: ignore
    
