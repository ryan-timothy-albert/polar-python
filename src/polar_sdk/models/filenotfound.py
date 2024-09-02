"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk import utils
from polar_sdk.types import BaseModel
import pydantic
from typing import Final
from typing_extensions import Annotated


class FileNotFoundType(str, Enum):
    FILE_NOT_FOUND = "FileNotFound"
class FileNotFoundData(BaseModel):
    detail: str
    TYPE: Annotated[Final[FileNotFoundType], pydantic.Field(alias="type")] = FileNotFoundType.FILE_NOT_FOUND # type: ignore
    


class FileNotFound(Exception):
    data: FileNotFoundData

    def __init__(self, data: FileNotFoundData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, FileNotFoundData)
