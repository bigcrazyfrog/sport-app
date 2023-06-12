from typing import List

from ninja import Schema
from pydantic import Field


class AllergenOut(Schema):
    id: int
    name: str = Field(max_length=255)


class AllergenFilters(Schema):
    allergens: List[int] | None
