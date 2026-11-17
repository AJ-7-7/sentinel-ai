
from datetime import datetime, timezone
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status

from app.schemas.transactions import (
    TransactionCreate,
    TransactionResponse,
)

router = APIRouter(
    prefix="/api/v1/transactions",
    tags=["Transactions"],
)

# Temporary in-memory storage.
# PostgreSQL will replace this later.
transactions: dict[UUID, TransactionResponse] = {}


@router.post(
    "",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_transaction(data: TransactionCreate):
    transaction = TransactionResponse(
        **data.model_dump(),
        id=uuid4(),
        created_at=datetime.now(timezone.utc),
    )

    transactions[transaction.id] = transaction

    return transaction


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse,
)
def get_transaction(transaction_id: UUID):
    transaction = transactions.get(transaction_id)

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found",
        )

    return transaction
