from  pydantic import  BaseModel , Field
from typing import  Optional



class Error_create(BaseModel):
    Error_number: Optional[int] = Field()
    Error_message: Optional[str] = Field()

