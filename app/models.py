from pydantic import BaseModel
from datetime import datetime
from typing import List

class Product(BaseModel):
    id: int
    name: str
    price: int
    quantity: int

class Transaction(BaseModel):
    product_id: int
    amount_paid: int
    change_returned: int
    timestamp: datetime
