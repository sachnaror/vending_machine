from fastapi import FastAPI
from .routes import products, vending

app = FastAPI(title="In-Memory Vending Machine API")

app.include_router(products.router, tags=["Products"])
app.include_router(vending.router, tags=["Vending"])
