from  pydantic import  BaseModel , Field
from typing import  Optional






class create_building(BaseModel):
    building_name : Optional[str] = Field()
    number_of_apartement: Optional[int] = Field()
    initial: Optional[int] = Field()
    name_of_manager: Optional[str] = Field()
    family_of_manager: Optional[str] = Field()



class creating_apartement(BaseModel):
    building_name: Optional[str] = Field()
    number : Optional[str] = Field()
    number_person: Optional[int] = Field()
    m2: Optional[str] = Field()
    type: Optional[str] = Field()
    mobile: Optional[str] = Field()

