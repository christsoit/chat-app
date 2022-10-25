from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import routes

#app object
app = FastAPI()
app.include_router(routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/api/launch-details")
# def launch_details():
#     return {
#         "launch_details": {
#             "year": 2022,
#             "month": 10,
#             "day": "28",
#             "hour": 19,
#             "min": 0,
#             "tz:": "PST"
#         }
#     }