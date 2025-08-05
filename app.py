import streamlit as st
import tempfile
from ultralytics import YOLO

# Set up the Streamlit page
st.set_page_config(page_title="Chili Pepper Disease and Ripeness Detection", layout="wide")
st.title("Chili Pepper Disease and Ripeness Detection")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Load the YOLOv8 model
model_path = "D:/DS_repo/Sweet-Chili/runs/segment/chili_yolov8_seg8/weights/best.pt"
try:
    model = YOLO(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}")

if uploaded_file is not None:
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tfile:
        tfile.write(uploaded_file.read())
        temp_image_path = tfile.name

    # Display the uploaded image
    st.image(temp_image_path, caption="Uploaded Image", use_container_width=True)

    # Perform inference on the image
    try:
        results = model.predict(source=temp_image_path, save=True)
        # The predicted image with bounding boxes is saved by default in the 'runs/segment/predict' directory
        # The path to the saved image is in the results object
        saved_image_path = results[0].save_dir + '/' + uploaded_file.name

        # Display the image with detections
        st.image(saved_image_path, caption="Image with Detections", use_container_width=True)
    except Exception as e:
        st.error(f"An error occurred during inference: {e}")