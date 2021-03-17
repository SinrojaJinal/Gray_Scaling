from fastapi import FastAPI, UploadFile, File
import cv2 as cv
import uvicorn
import os
from bgrtogray import GrayScale

app = FastAPI()
print("in main")
@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    try:
        os.mkdir("files")
        print(os.getcwd()) 
    except Exception as e:
        print(e) 
    file_name = os.getcwd()+"/files/"+file.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(file.file.read())
        f.close()
    obj = GrayScale()
    obj.GrayScaling(file_name)  
    return {"filename": file_name}

if __name__ =="__main__":
    print("in program")
    uvicorn.run(app,host ='0.0.0.0', port=8001)