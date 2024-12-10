"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitadsupdate import BenefitAdsUpdate, BenefitAdsUpdateTypedDict
from .benefitcustomupdate import BenefitCustomUpdate, BenefitCustomUpdateTypedDict
from .benefitdiscordupdate import BenefitDiscordUpdate, BenefitDiscordUpdateTypedDict
from .benefitdownloadablesupdate import (
    BenefitDownloadablesUpdate,
    BenefitDownloadablesUpdateTypedDict,
)
from .benefitgithubrepositoryupdate import (
    BenefitGitHubRepositoryUpdate,
    BenefitGitHubRepositoryUpdateTypedDict,
)
from .benefitlicensekeysupdate import (
    BenefitLicenseKeysUpdate,
    BenefitLicenseKeysUpdateTypedDict,
)
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


BenefitsUpdateBenefitUpdateTypedDict = TypeAliasType(
    "BenefitsUpdateBenefitUpdateTypedDict",
    Union[
        BenefitAdsUpdateTypedDict,
        BenefitCustomUpdateTypedDict,
        BenefitDiscordUpdateTypedDict,
        BenefitGitHubRepositoryUpdateTypedDict,
        BenefitDownloadablesUpdateTypedDict,
        BenefitLicenseKeysUpdateTypedDict,
    ],
)


BenefitsUpdateBenefitUpdate = TypeAliasType(
    "BenefitsUpdateBenefitUpdate",
    Union[
        BenefitAdsUpdate,
        BenefitCustomUpdate,
        BenefitDiscordUpdate,
        BenefitGitHubRepositoryUpdate,
        BenefitDownloadablesUpdate,
        BenefitLicenseKeysUpdate,
    ],
)


class BenefitsUpdateRequestTypedDict(TypedDict):
    id: str
    request_body: BenefitsUpdateBenefitUpdateTypedDict


class BenefitsUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        BenefitsUpdateBenefitUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
