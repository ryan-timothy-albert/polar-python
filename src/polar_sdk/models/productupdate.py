"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .attachedcustomfieldcreate import (
    AttachedCustomFieldCreate,
    AttachedCustomFieldCreateTypedDict,
)
from .existingproductprice import ExistingProductPrice, ExistingProductPriceTypedDict
from .productpriceonetimecustomcreate import (
    ProductPriceOneTimeCustomCreate,
    ProductPriceOneTimeCustomCreateTypedDict,
)
from .productpriceonetimefixedcreate import (
    ProductPriceOneTimeFixedCreate,
    ProductPriceOneTimeFixedCreateTypedDict,
)
from .productpriceonetimefreecreate import (
    ProductPriceOneTimeFreeCreate,
    ProductPriceOneTimeFreeCreateTypedDict,
)
from .productpricerecurringfixedcreate import (
    ProductPriceRecurringFixedCreate,
    ProductPriceRecurringFixedCreateTypedDict,
)
from .productpricerecurringfreecreate import (
    ProductPriceRecurringFreeCreate,
    ProductPriceRecurringFreeCreateTypedDict,
)
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Union
from typing_extensions import NotRequired, TypedDict


ProductUpdatePricesTypedDict = Union[
    ExistingProductPriceTypedDict,
    ProductPriceOneTimeFreeCreateTypedDict,
    ProductPriceRecurringFreeCreateTypedDict,
    ProductPriceOneTimeFixedCreateTypedDict,
    ProductPriceRecurringFixedCreateTypedDict,
    ProductPriceOneTimeCustomCreateTypedDict,
]


ProductUpdatePrices = Union[
    ExistingProductPrice,
    ProductPriceOneTimeFreeCreate,
    ProductPriceRecurringFreeCreate,
    ProductPriceOneTimeFixedCreate,
    ProductPriceRecurringFixedCreate,
    ProductPriceOneTimeCustomCreate,
]


class ProductUpdateTypedDict(TypedDict):
    r"""Schema to update a product."""

    name: NotRequired[Nullable[str]]
    description: NotRequired[Nullable[str]]
    r"""The description of the product."""
    is_archived: NotRequired[Nullable[bool]]
    r"""Whether the product is archived. If `true`, the product won't be available for purchase anymore. Existing customers will still have access to their benefits, and subscriptions will continue normally."""
    prices: NotRequired[Nullable[List[ProductUpdatePricesTypedDict]]]
    r"""List of available prices for this product. If you want to keep existing prices, include them in the list as an `ExistingProductPrice` object."""
    medias: NotRequired[Nullable[List[str]]]
    r"""List of file IDs. Each one must be on the same organization as the product, of type `product_media` and correctly uploaded."""
    attached_custom_fields: NotRequired[
        Nullable[List[AttachedCustomFieldCreateTypedDict]]
    ]


class ProductUpdate(BaseModel):
    r"""Schema to update a product."""

    name: OptionalNullable[str] = UNSET

    description: OptionalNullable[str] = UNSET
    r"""The description of the product."""

    is_archived: OptionalNullable[bool] = UNSET
    r"""Whether the product is archived. If `true`, the product won't be available for purchase anymore. Existing customers will still have access to their benefits, and subscriptions will continue normally."""

    prices: OptionalNullable[List[ProductUpdatePrices]] = UNSET
    r"""List of available prices for this product. If you want to keep existing prices, include them in the list as an `ExistingProductPrice` object."""

    medias: OptionalNullable[List[str]] = UNSET
    r"""List of file IDs. Each one must be on the same organization as the product, of type `product_media` and correctly uploaded."""

    attached_custom_fields: OptionalNullable[List[AttachedCustomFieldCreate]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "description",
            "is_archived",
            "prices",
            "medias",
            "attached_custom_fields",
        ]
        nullable_fields = [
            "name",
            "description",
            "is_archived",
            "prices",
            "medias",
            "attached_custom_fields",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
