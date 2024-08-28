"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organizationfeaturesettings import OrganizationFeatureSettings, OrganizationFeatureSettingsTypedDict
from .organizationprofilesettings import OrganizationProfileSettings, OrganizationProfileSettingsTypedDict
from datetime import datetime
from polar_sh.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict


class OrganizationOutputTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The organization ID."""
    name: str
    slug: str
    avatar_url: Nullable[str]
    bio: Nullable[str]
    company: Nullable[str]
    blog: Nullable[str]
    location: Nullable[str]
    email: Nullable[str]
    twitter_username: Nullable[str]
    pledge_minimum_amount: int
    pledge_badge_show_amount: bool
    default_upfront_split_to_contributors: Nullable[int]
    donations_enabled: bool
    r"""If this organizations accepts donations"""
    profile_settings: Nullable[OrganizationProfileSettingsTypedDict]
    r"""Settings for the organization profile"""
    feature_settings: Nullable[OrganizationFeatureSettingsTypedDict]
    r"""Settings for the organization features"""
    

class OrganizationOutput(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The organization ID."""
    name: str
    slug: str
    avatar_url: Nullable[str]
    bio: Nullable[str]
    company: Nullable[str]
    blog: Nullable[str]
    location: Nullable[str]
    email: Nullable[str]
    twitter_username: Nullable[str]
    pledge_minimum_amount: int
    pledge_badge_show_amount: bool
    default_upfront_split_to_contributors: Nullable[int]
    donations_enabled: bool
    r"""If this organizations accepts donations"""
    profile_settings: Nullable[OrganizationProfileSettings]
    r"""Settings for the organization profile"""
    feature_settings: Nullable[OrganizationFeatureSettings]
    r"""Settings for the organization features"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at", "avatar_url", "bio", "company", "blog", "location", "email", "twitter_username", "default_upfront_split_to_contributors", "profile_settings", "feature_settings"]
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
        
