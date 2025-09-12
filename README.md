# Vending Machine API (In-Memory FastAPI)

A minimal, production-ready **in-memory** FastAPI app for a vending machine.
No database is used; products and transactions are kept in process memory
and seeded at startup for an instant demo.

## Features
- List full inventory with price and quantity
- Buy product with amount inserted; returns change
- Track transactions
- Show total revenue collected

## Tech
- FastAPI
- Pydantic
- Uvicorn
- No external DB

## Quickstart (Local)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the docs:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### Example Calls
- List products: `GET /products/`
- Buy product: `POST /buy/?product_id=1&amount_paid=10`
- Revenue: `GET /revenue/`
- Transactions: `GET /transactions/`

## Docker

Build:
```bash
docker build -t vending-api .
```

Run:
```bash
docker run -p 8000:8000 --name vending vending-api
```

Now open:
- http://localhost:8000/docs




## Project Layout

```
vending_machine/
  app/
    __init__.py
    main.py
    models.py
    routes/
      __init__.py
      products.py
      vending.py
  requirements.txt
  Dockerfile
  .dockerignore
  README.md
```

## Notes
- This is an in-memory demo. Restarting the server resets inventory and revenue.
- For persistence, swap to SQLite or Postgres and add SQLAlchemy/CRUD layers.


```

├── vending_machine/
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── README.md
│   ├── .dockerignore
│   ├── app/
│   │   ├── models.py
│   │   └── main.py
│   │   ├── routes/
│   │   │   ├── vending.py
│   │   │   └── products.py

```

## 📩 Contact

| Name              | Details                                                           |
|-------------------|-------------------------------------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                                                      |
| **📧 Email**      | [sachnaror@gmail.com](mailto:sachnaror@gmail.com)                 |
| **📍 Location**   | Noida, India                                                      |
| **📂 GitHub**     | [github.com/sachinarora](https://github.com/sachinarora)          |
| **🌐 Youtube**    | [YouTube (@sachnaror4841)](https://www.youtube.com/@sachnaror4841/videos) |
| **🌐 Blog**       | [medium.com/@sachnaror](https://medium.com/@sachnaror)            |
| **🌐 Website**    | [about.me/sachin-arora](https://about.me/sachin-arora)            |
| **🌐 Twitter**    | [@sachinhep](https://twitter.com/sachinhep)                       |
| **📱 Phone**      | [+91 9560330483](tel:+919560330483)                               |






## Screenshot

<img width="714" height="659" alt="Screenshot 2025-09-13 at 5 14 51 AM" src="https://github.com/user-attachments/assets/e2c4d723-23aa-4968-960e-3f49ea491a52" />

<img width="1454" height="906" alt="image" src="https://github.com/user-attachments/assets/fea5abb0-e55a-4bfa-a184-e7d736b79439" />


