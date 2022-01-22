from . import models,schemas
from sqlalchemy.orm import Session

def get_user(db:Session,user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def fetch_user_by_email(db:Session,email:str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_bookings(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Booking).offset(skip).limit(limit).all()

def create_new_user(db:Session,user:schemas.UserCreate):
    testing_hashed = user.password + "test"
    db_user = models.User(email=user.email,hashed_password=testing_hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_booking(db: Session, booking: schemas.BookingCreate, user_id: int):
    db_item = models.Booking(**booking.dict(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
