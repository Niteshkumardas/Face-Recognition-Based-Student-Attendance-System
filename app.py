"""APP
FastAPI app definition, initialization and definition of routes
"""

# # Installed # #
# from Slr import Prediction
from fastapi import FastAPI
from attendence_api.routers import attendence

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000/",
]

# # Package # #




app = FastAPI(
    tags=['Model'],
    title="Face Recognition-api"
)


# attendence api
app.include_router(attendence.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def run():
#     """Run the API using Uvicorn"""
#     uvicorn.run(
#         'app:app',
#         port=api_settings.port,
#         host=api_settings.host,
#         reload=True,
#     )

if __name__=="__main__":
    print("running")
    # run()
    # uvicorn.run('app:app', host='localhost', port=8000,reload=True)
