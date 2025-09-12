from fastapi import APIRouter
from typing import List
from ..models import Product

router = APIRouter()

# In-memory inventory seeded on startup
inventory: List[Product] = [
    Product(id=1, name="Chocolate", price=5, quantity=10),
    Product(id=2, name="Chips", price=10, quantity=5),
    Product(id=3, name="Soda", price=15, quantity=8),
]

@router.get("/products/", response_model=List[Product])
def list_products() -> List[Product]:
    return inventory

@router.get("/inventory/", response_model=List[Product])
def get_inventory() -> List[Product]:
    return inventory
