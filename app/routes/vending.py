from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import List
from ..models import Transaction
from .products import inventory

router = APIRouter()

transactions: List[Transaction] = []

@router.post("/buy/", response_model=Transaction)
def buy_product(product_id: int, amount_paid: int) -> Transaction:
    product = next((p for p in inventory if p.id == product_id), None)
    if not product or product.quantity <= 0:
        raise HTTPException(status_code=404, detail="Product not available")

    if amount_paid < product.price:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    change = amount_paid - product.price
    product.quantity -= 1

    transaction = Transaction(
        product_id=product.id,
        amount_paid=amount_paid,
        change_returned=change,
        timestamp=datetime.utcnow(),
    )
    transactions.append(transaction)
    return transaction

@router.get("/revenue/")
def get_revenue():
    total_collected = sum((t.amount_paid - t.change_returned) for t in transactions)
    return {"total_revenue": total_collected}

@router.get("/transactions/", response_model=List[Transaction])
def get_transactions() -> List[Transaction]:
    return transactions
