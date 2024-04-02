from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    username: str
    email: str
    password: str  # Добавлено поле password для хранения пароля пользователя
    trips: List["Trip"] = Relationship(back_populates="user")
    first_name: str
    last_name: str
    age: int
    profile: Optional["UserProfile"] = Relationship(back_populates="user")
    reviews: List["TripReview"] = Relationship(back_populates="user")
    interests: List["UserInterest"] = Relationship(back_populates="user")


class UserProfile(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    about_me: str
    user: Optional[User] = Relationship(back_populates="profile")


class Trip(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    destination: str
    start_date: str
    end_date: str
    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="trips")
    reviews: List["TripReview"] = Relationship(back_populates="trip")


class TripReview(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    trip_id: int = Field(foreign_key="trip.id")
    user_id: int = Field(foreign_key="user.id")
    rating: int
    comment: str
    user: Optional[User] = Relationship(back_populates="reviews")
    trip: Optional[Trip] = Relationship(back_populates="reviews")


class Interest(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    users: List["UserInterest"] = Relationship(back_populates="interest")


class UserInterest(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    interest_id: int = Field(foreign_key="interest.id")
    user: Optional[User] = Relationship(back_populates="interests")
    interest: Optional[Interest] = Relationship(back_populates="users")
class PartnershipRequest(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    trip_id: int = Field(foreign_key="trip.id")
    user_id: int = Field(foreign_key="user.id")
    trip: Optional[Trip] = Relationship(back_populates="partnership_requests")
    user: Optional[User] = Relationship(back_populates="partnership_requests")

class Partnership(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    trip_id: int = Field(foreign_key="trip.id")
    partner_id: int = Field(foreign_key="user.id")
    trip: Optional[Trip] = Relationship(back_populates="partners")
    partner: Optional[User] = Relationship(back_populates="partners")