import streamlit as st
import requests

backend_url = "http://localhost:8000"

st.title("Hotel Management System")

# Rooms
st.header("Rooms")
room_number = st.text_input("Room Number")
room_type = st.text_input("Room Type")
room_price = st.number_input("Room Price", min_value=0.0, format="%.2f")
if st.button("Add Room"):
    response = requests.post(f"{backend_url}/rooms/", json={
        "id": len(requests.get(f"{backend_url}/rooms/").json()) + 1,
        "number": room_number,
        "type": room_type,
        "price": room_price
    })
    st.write(response.json())

rooms = requests.get(f"{backend_url}/rooms/").json()
st.write(rooms)

# Customers
st.header("Customers")
customer_name = st.text_input("Customer Name")
customer_email = st.text_input("Customer Email")
if st.button("Add Customer"):
    response = requests.post(f"{backend_url}/customers/", json={
        "id": len(requests.get(f"{backend_url}/customers/").json()) + 1,
        "name": customer_name,
        "email": customer_email
    })
    st.write(response.json())

customers = requests.get(f"{backend_url}/customers/").json()
st.write(customers)

# Reservations
st.header("Reservations")
reservation_room_id = st.number_input("Room ID", min_value=1)
reservation_customer_id = st.number_input("Customer ID", min_value=1)
check_in = st.date_input("Check-in Date")
check_out = st.date_input("Check-out Date")
if st.button("Add Reservation"):
    response = requests.post(f"{backend_url}/reservations/", json={
        "id": len(requests.get(f"{backend_url}/reservations/").json()) + 1,
        "room_id": reservation_room_id,
        "customer_id": reservation_customer_id,
        "check_in": check_in.isoformat(),
        "check_out": check_out.isoformat()
    })
    st.write(response.json())

reservations = requests.get(f"{backend_url}/reservations/").json()
st.write(reservations)
