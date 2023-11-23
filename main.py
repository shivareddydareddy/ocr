from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.post("/extract_image_data/")

def extract_image_data( file: UploadFile = File(...)):
    try:
        if file.content_type in ["image/jpeg","png","image"]:
            contents =  file.read()
            img = Image.open(BytesIO(contents))
    
            
            
            extracted_data = pytesseract.image_to_string(img, lang='eng')
            
            return JSONResponse(content={"extracted_data": extracted_data}, status_code=200)
        else:
            raise HTTPException(status_code=422, detail="file is not an image")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error")


