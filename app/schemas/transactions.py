
from datetime import datetime
from decimal import Decimal
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    account_id: str = Field(min_length=1, max_length=50)
    merchant: str = Field(min_length=1, max_length=100)
    amount: Decimal = Field(
        gt=0,
        max_digits=12,
        decimal_places=2
    )
    currency: Literal["USD"] = "USD"


class TransactionResponse(TransactionCreate):
    id: UUID
    created_at: datetime
