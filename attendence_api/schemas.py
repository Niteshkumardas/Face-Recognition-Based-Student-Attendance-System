from pydantic import BaseModel

class Attendence(BaseModel):
    base64_img: str
    # class Config:
    #     orm_mode=True

class AttendenceCreate(Attendence):
    pass