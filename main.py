from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Room(BaseModel):
    id: int
    number: str
    type: str
    price: float

class Customer(BaseModel):
    id: int
    name: str
    email: str

class Reservation(BaseModel):
    id: int
    room_id: int
    customer_id: int
    check_in: str
    check_out: str

rooms = []
customers = []
reservations = []

@app.post("/rooms/", response_model=Room)
def create_room(room: Room):
    rooms.append(room)
    return room

@app.get("/rooms/", response_model=List[Room])
def get_rooms():
    return rooms

@app.post("/customers/", response_model=Customer)
def create_customer(customer: Customer):
    customers.append(customer)
    return customer

@app.get("/customers/", response_model=List[Customer])
def get_customers():
    return customers

@app.post("/reservations/", response_model=Reservation)
def create_reservation(reservation: Reservation):
    # Check if the room is already booked
    for existing_reservation in reservations:
        if (
            existing_reservation.room_id == reservation.room_id
            and existing_reservation.check_out >= reservation.check_in
            and existing_reservation.check_in <= reservation.check_out
        ):
            raise HTTPException(status_code=400, detail="Room is already booked for the specified dates")

    # If not booked, create the reservation
    reservations.append(reservation)
    return reservation

@app.get("/reservations/", response_model=List[Reservation])
def get_reservations():
    return reservations

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
