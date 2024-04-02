from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class TripBase(BaseModel):
    destination: str
    start_date: str
    end_date: str


class TripCreate(TripBase):
    user_id: int


class Trip(TripBase):
    id: int

    class Config:
        orm_mode = True


class UserPasswordChange(BaseModel):
    old_password: str
    new_password: str


class OAuth2PasswordRequestForm(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None


class UserPasswordChange(BaseModel):
    old_password: str
    new_password: str


class PartnershipRequestBase(BaseModel):
    user_id: int
    trip_id: int


class PartnershipRequestCreate(PartnershipRequestBase):
    pass


class PartnershipRequest(PartnershipRequestBase):
    id: int

    class Config:
        orm_mode = True

