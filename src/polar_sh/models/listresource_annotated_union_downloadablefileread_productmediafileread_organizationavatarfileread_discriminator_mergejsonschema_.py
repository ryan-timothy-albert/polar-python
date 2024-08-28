"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .downloadablefileread import DownloadableFileRead, DownloadableFileReadTypedDict
from .organizationavatarfileread import OrganizationAvatarFileRead, OrganizationAvatarFileReadTypedDict
from .pagination import Pagination, PaginationTypedDict
from .productmediafileread_output import ProductMediaFileReadOutput, ProductMediaFileReadOutputTypedDict
from polar_sh.types import BaseModel
from polar_sh.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


FileReadTypedDict = Union[DownloadableFileReadTypedDict, ProductMediaFileReadOutputTypedDict, OrganizationAvatarFileReadTypedDict]


FileRead = Annotated[Union[Annotated[DownloadableFileRead, Tag("downloadable")], Annotated[OrganizationAvatarFileRead, Tag("organization_avatar")], Annotated[ProductMediaFileReadOutput, Tag("product_media")]], Discriminator(lambda m: get_discriminator(m, "service", "service"))]


class ListResourceAnnotatedUnionDownloadableFileReadProductMediaFileReadOrganizationAvatarFileReadDiscriminatorMergeJSONSchemaTypedDict(TypedDict):
    pagination: PaginationTypedDict
    items: NotRequired[List[FileReadTypedDict]]
    

class ListResourceAnnotatedUnionDownloadableFileReadProductMediaFileReadOrganizationAvatarFileReadDiscriminatorMergeJSONSchema(BaseModel):
    pagination: Pagination
    items: Optional[List[FileRead]] = None
    
