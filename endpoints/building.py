from fastapi import APIRouter, HTTPException
from fastapi import Depends
from depency.base import user_show, permissions
from shemas.building_model import create_building
from database import database_file as db
from Error_model.building_Error import Error_create
import datetime
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz

router = APIRouter()

today_date = JalaliDate(JalaliDate.today()).strftime("%Y_%m_%d")
date_spilted = today_date.split('_')
hour = datetime.datetime.now().hour
miniute = datetime.datetime.now().minute
times = '{}:{}'.format(hour, miniute)
prz = JalaliDateTime(int(date_spilted[0]), int(date_spilted[1]), int(date_spilted[2]), hour, miniute, 0, 0,
                     pytz.utc).strftime("%c")
name_of_day = prz.split(' ')[0]


@router.post("/create_building",tags=['building'])
async def create_building(
        *,
        # current_user: user_show = Depends(permissions(["admin"])),
        item: create_building
):
    try:
        name = item.building_name
        query = {'name': name}
        counter = db.building_collection.count_documents(query)
        if counter < 1:
            # item['user_created'] = current_user.id
            item = item.dict()
            item['time_created'] = today_date
            item['user_updated'] = ''
            item['time_updated'] = ''
            db.building_collection.insert_one(item)
            item['done'] = True
            item['_id'] = str(item['_id'])
            return {
                'data': item
            }
        else:
            Error = Error_create()
            Error.Error_message = 'the apartement exsist'
            Error.Error_number = 1
            return Error
    except Exception as e:
        Error = Error_create()
        Error.Error_message = e
        Error.Error_number = 2
        return Error




@router.get("/building/list", tags=['building'])
async def building_list(
        # current_user: user_show = Depends(permissions(["admin"])),
):
    try:

        data = db.building_collection.find()
        return_list = []
        for item in data:
            return_list.append({
                'id': str(item['_id']),
                'name': item['building_name']
            })
        return {
            'done' : True ,
            'data':return_list
        }
    except Exception as e:
        Error = Error_create()
        Error.Error_message = e
        Error.Error_number = 2
        return Error


