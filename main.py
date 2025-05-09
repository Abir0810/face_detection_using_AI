#Opencv+CVlib

# from fastapi import FastAPI, UploadFile, File
# import cv2
# import numpy as np
# import cvlib as cv
# from cvlib.object_detection import draw_bbox

# app = FastAPI()

# @app.post("/detect-face/")
# async def detect_face(file: UploadFile = File(...)):
#     # Read image in bytes and convert to numpy array
#     contents = await file.read()
#     np_array = np.frombuffer(contents, np.uint8)
#     image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

#     # Detect faces
#     faces, confidences = cv.detect_face(image)

#     # Return true if at least one face detected
#     return {"face": len(faces) > 0}


#Medipipe

from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import mediapipe as mp

app = FastAPI()

# Setup Mediapipe face detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.6)

@app.post("/detect-face/")
async def detect_face(file: UploadFile = File(...)):
    contents = await file.read()
    np_array = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # Convert to RGB (required by Mediapipe)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_image)

    # Check if full face is visible
    if results.detections:
        # You could inspect landmarks here (eyes, nose, mouth)
        return {"face": True}
    else:
        return {"face": False}