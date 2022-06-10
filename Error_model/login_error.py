from  pydantic import  BaseModel , Field
from typing import  Optional

class user_create_Error(BaseModel):
    Error_number : Optional[int]  = Field()
    Error_message : Optional[str] = Field()

