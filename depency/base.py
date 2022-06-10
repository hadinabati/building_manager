from pydantic import BaseModel, Field, BaseSettings
from typing import Optional, List
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from bson import ObjectId as BaseObjectId
from bson.errors import InvalidId
import secrets
from database import database_file as db
from jose import jwt, JWTError, ExpiredSignatureError


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_hex()


class user_model(BaseModel):
    name: str = Field(default='name')
    passwords: str = Field(default='passwords')
    role: str = Field(default='')
    number: int = Field(default=0)


class ObjectId(str):
    @classmethod
    def validate(cls, value):
        try:
            return BaseObjectId(str(value))

        except InvalidId as e:
            raise ValueError("Not a valid ObjectId") from e


@classmethod
def __get_validators__(cls):
    yield cls.validate


class user_show(BaseModel):
    id: Optional[ObjectId] = Field()
    username: Optional[str] = Field()
    role: Optional[list] = Field()


class Credentials(BaseModel):
    username: str
    password: str


async def basic_authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    credentials = Credentials(
        username=form_data.username,
        password=form_data.password
    )
    user = db.user_collection.find_one(
        {'username': credentials.username, 'password': credentials.password}
    )
    if user is not None:
        user_back = user_show()
        user_back.id = user['_id']
        user_back.role = user['role']
        user_back.username = user['username']
        return user_back
    else:
        raise HTTPException(status_code=404, detail='user not found')


class TokenData(BaseModel):
    id: ObjectId
    username: str
    role: Optional[List[str]]


class Token(BaseModel):
    access_token: Optional[str]
    refresh_token: Optional[str]
    token_type: str
    is_new_user: Optional[bool]


def create_access_token(
        data: dict,
) -> str:
    to_encode = data.copy()
    secrect_key = secrets.token_hex()
    print(secrect_key)
    encoded_jwt = jwt.encode(to_encode, str(secrect_key), algorithm='HS256')
    return encoded_jwt


def decode_access_token(
        token: str,
):
    login_credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid access token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    refresh_credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Access token expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(str(token), key=secrets.token_hex(), options={"verify_signature": False})
    except ExpiredSignatureError:
        raise refresh_credentials_exception
    except JWTError:
        raise login_credentials_exception
    return TokenData(
        id=payload.get("sub"),
        username=payload.get("username"),
        role=payload.get("scope")
    )


oauth2_schema = OAuth2PasswordBearer(tokenUrl='http://127.0.0.1:8000/login')


def get_current_user(token: str = Depends(oauth2_schema)):
    token_data = decode_access_token(token=token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if (token_data.username or token_data.id) is None:
        raise credentials_exception
    data = token_data.dict()
    return user_show.parse_obj({**data})


def permissions(permissions_list: List[str]):
    async def user_permission_checker(user: user_show = Depends(get_current_user)):
        permision_list = permissions_list
        user_permision = user.role
        check = False
        for item in permissions_list:
            if item != 'authenticated' and item in user_permision:
                check = True
                break

        if "authenticated" in permissions_list and "authenticated" not in user.role:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="login",
            )
        elif check:
            pass
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have access to this endpoint!",
            )

        return user

    return user_permission_checker
