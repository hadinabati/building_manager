from fastapi import APIRouter
from fastapi import Depends
from depency.base import user_show, basic_authenticate, create_access_token, Token , permissions
from shemas.User_Model import create_user
from database import  database_file as db
from Error_model.login_error import user_create_Error

router = APIRouter()


@router.post('/login', tags=['login'])
async def Login(
        current_user: user_show = Depends(basic_authenticate)
):
    data = {
        "sub": str(current_user.id),
        "username": current_user.username,
        "scope": [*current_user.role, "authenticated"]
    }
    access_token = create_access_token(
        data
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post('/register', tags=['login'])
async def register(item: create_user):
    try:
        data = item.dict()
        query = {'username' : item.username}
        counter=db.user_collection.count_documents(query)
        if counter <1 :
            data['role']=item.role.value
            db.user_collection.insert_one(data)
            return data
        else:
            Error = user_create_Error()
            Error.Error_number = 1
            Error.Error_message = 'the counter is more than one'
            return Error.dict()
    except Exception as e :
        Error = user_create_Error()
        Error.Error_number = 2
        Error.Error_message = e
        return Error.dict()



@router.post("/create_appartement")
async def say_hello(
        current_user: user_show = Depends(permissions(["admin"])),
):
    pass


