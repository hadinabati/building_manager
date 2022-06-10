from fastapi import FastAPI
from  endpoints import login , building
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(building.router)
