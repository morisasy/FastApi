from typing import List
from pydantic import BaseModel

##BOOKING
class BookingBase(BaseModel):
    name:str
    description:str = None

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id:int
    user_id:int

    class Config:
        orm_mode = True

##USER
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    bookings: List[Booking] = []

    class Config:
        orm_mode = True
