# FastAPI Starter Project

This is a minimal FastAPI application written in Python. It provides basic GET and POST API endpoints and uses Pydantic for data validation.

To run the app, follow these steps:

1. Make sure you have Python 3.8 or newer installed.

2. Install the required packages:
   pip install fastapi uvicorn

3. Run the app using:
   python main.py

The server will start on http://127.0.0.1:8000/

Available endpoints:

- GET / : Returns a welcome message.
- GET /items/{item_id} : Fetches an item by ID (with optional query).
- POST /items/ : Creates an item using JSON input:
  {
    "name": "Item name",
    "description": "Optional description",
    "price": 9.99,
    "in_stock": true
  }

Interactive API documentation is available at:
http://127.0.0.1:8000/docs

This project is ideal as a starting point for building REST APIs with FastAPI.
