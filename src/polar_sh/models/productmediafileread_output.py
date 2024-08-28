"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from polar_sh.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Final, TypedDict
from typing_extensions import Annotated


class Service(str, Enum):
    PRODUCT_MEDIA = "product_media"

class ProductMediaFileReadOutputTypedDict(TypedDict):
    r"""File to be used as a product media file."""
    
    id: str
    organization_id: str
    name: str
    path: str
    mime_type: str
    size: int
    storage_version: Nullable[str]
    checksum_etag: Nullable[str]
    checksum_sha256_base64: Nullable[str]
    checksum_sha256_hex: Nullable[str]
    last_modified_at: Nullable[datetime]
    version: Nullable[str]
    is_uploaded: bool
    created_at: datetime
    size_readable: str
    public_url: str
    

class ProductMediaFileReadOutput(BaseModel):
    r"""File to be used as a product media file."""
    
    id: str
    organization_id: str
    name: str
    path: str
    mime_type: str
    size: int
    storage_version: Nullable[str]
    checksum_etag: Nullable[str]
    checksum_sha256_base64: Nullable[str]
    checksum_sha256_hex: Nullable[str]
    last_modified_at: Nullable[datetime]
    version: Nullable[str]
    is_uploaded: bool
    created_at: datetime
    size_readable: str
    public_url: str
    SERVICE: Annotated[Final[Service], pydantic.Field(alias="service")] = Service.PRODUCT_MEDIA # type: ignore
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["storage_version", "checksum_etag", "checksum_sha256_base64", "checksum_sha256_hex", "last_modified_at", "version"]
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
        
