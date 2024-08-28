"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sh.types import BaseModel
from typing import TypedDict


class MetricsIntervalLimitTypedDict(TypedDict):
    r"""Date interval limit to get metrics for a given interval."""
    
    max_days: int
    r"""Maximum number of days for this interval."""
    

class MetricsIntervalLimit(BaseModel):
    r"""Date interval limit to get metrics for a given interval."""
    
    max_days: int
    r"""Maximum number of days for this interval."""
    
