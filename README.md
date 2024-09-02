Hotel Management System:

This project is a simple hotel management system built with FastAPI for the backend and Streamlit for the frontend. It allows you to manage rooms, customers, and reservations.

Features:

-Rooms Management: Add and view rooms.
-Customers Management: Add and view customers.
-Reservations Management**: Add and view reservations with validation to check if a room is already booked.

Requirements:

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic
- Requests
- Streamlit
you can use the cmd:
pip install -r requirements.txt


Installation:
Start the FastAPI backend:

>>>uvicorn main:app --reload

Start the Streamlit frontend:

>>>streamlit run app.py
