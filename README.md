
# Face Detection API (FastAPI + Mediapipe+ OpenCV)

This project provides a simple FastAPI-based REST API to detect whether an uploaded image contains a **full human face** using **Mediapipe**.

Only **complete, front-facing faces** (including eyes, nose, mouth) are accepted. Cropped, partial, or side faces are rejected.

---

## 🚀 Features

- Fast and lightweight face detection
- Full offline support (no API keys or cloud dependency)
- Powered by [Google Mediapipe](https://github.com/google/mediapipe)
- JSON response indicating whether a full face is present

---

## 🧱 Project Structure

```
FACE_DETECTION/
├── main.py              # FastAPI backend logic
├── requirements.txt     # Required Python packages
└── README.md            # This file
```

---

## 🔧 Setup Instructions

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, install manually:

```bash
pip install fastapi uvicorn mediapipe opencv-python numpy
```

---

## ▶️ Run the API Server

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for Swagger UI where you can upload images.

---

## 📷 API Endpoint

### `POST /detect-face/`

Uploads an image and detects if a **complete human face** is present.

#### Request (form-data):
- `file`: Image file (JPEG, PNG, etc.)

#### Response (JSON):

```json
{
  "face": true   // or false
}
```

---

## ✅ Example Output

### Case 1: Full face present  
→ Response: `{ "face": true }`

### Case 2: Partial or side face only  
→ Response: `{ "face": false }`

---

## 📌 Notes

- Only front-facing, uncropped faces are accepted.
- Internally uses Mediapipe's `FaceDetection(model_selection=1)` with a minimum confidence of 0.6.
- You can adjust thresholds or expand to include facial landmark checks if needed.

---

## 🧪 Future Ideas

- Add eye/nose/mouth landmark checks for stricter face completeness.
- Extend with face recognition (identity matching).
- Add support for webcam/live detection mode.

---

## License

MIT – free to use, modify, and distribute.
