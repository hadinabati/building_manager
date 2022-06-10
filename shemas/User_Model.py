import enum
from typing import  Optional
from pydantic import BaseModel , Field




class type_user(enum.Enum):
    admin = 'admin'
    normal = 'normal'


class create_user(BaseModel):
    name : Optional[str] = Field()
    family: Optional[str] = Field()
    number: Optional[str] = Field()
    apartement: Optional[str] = Field()
    username: Optional[str] = Field()
    password: Optional[str] = Field()
    role: Optional[type_user] = Field()


