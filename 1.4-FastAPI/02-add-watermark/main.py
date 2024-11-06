from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io

app = FastAPI()

@app.post("/image")
async def add_logo(input_file: UploadFile = File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Unsupported file type")
    contents = await input_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    user_image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    logo = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)

    logo_height, logo_width, _ = logo.shape
    image_height, image_width, _ = user_image.shape
    x_offset = (image_width - logo_width) // 2
    y_offset = (image_height - logo_height) // 2

    # Blend the logo onto the uploaded image
    for c in range(3):
        user_image[y_offset:y_offset+logo_height, x_offset:x_offset+logo_width, c] = (
            user_image[y_offset:y_offset+logo_height, x_offset:x_offset+logo_width, c] * (1 - logo[:, :, 3] / 255.0) +
            logo[:, :, c] * (logo[:, :, 3] / 255.0))

    _, encoded_image = cv2.imencode(".jpg", user_image)
    image_bytes = encoded_image.tobytes()
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg")
