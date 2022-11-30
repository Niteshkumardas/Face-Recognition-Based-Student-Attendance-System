from fastapi import APIRouter
from fastapi.responses import FileResponse
from attendence_api.predict import predict
from attendence_api.ExcelFile import register_attendance
from attendence_api.schemas import AttendenceCreate
import base64

router=APIRouter(
    tags=['Attendence']
)


@router.post("/attendence",response_model=str)
def post_image(file:AttendenceCreate):
    print(len(file.base64_img))
    try:    
        imgdata = base64.b64decode(file.base64_img)
        print(len(imgdata))
        # filename = 'new.png'  # I assume you have a way of picking unique filenames
        with open('image.png', 'wb') as f:
            f.write(imgdata)
        predicted_name = predict('image.png')
        register_attendance(predicted_name)
        print(predicted_name)
        return predicted_name
    except:
         return "failed"

@router.get("/attendance.csv")  
def get_csv():
    return FileResponse('attendance.csv')


