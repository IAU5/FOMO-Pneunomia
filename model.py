import onnxruntime as ort
import numpy as np
from PIL import Image
import sys

def preprocess(image_path):
    img = Image.open(image_path).convert("L")
    img = img.resize((64, 64))
    img = np.asarray(img, dtype=np.float32) / 255.0
    img = (img - 0.5) / 0.5
    img = img[np.newaxis, np.newaxis, :, :]
    return img

def run_inference(image_path, model_path="model.onnx"):
    session = ort.InferenceSession(model_path)
    input_tensor = preprocess(image_path)
    input_name = session.get_inputs()[0].name
    output = session.run(None, {input_name: input_tensor})
    probabilities = np.exp(output[0]) / np.sum(np.exp(output[0]), axis=1, keepdims=True)
    predicted_class = np.argmax(probabilities)
    return probabilities, predicted_class

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python model.py test_28.jpg")
        sys.exit(1)
    image_path = sys.argv[1]
    probabilities, predicted_class = run_inference(image_path)
    print(f"Predicted Class: {predicted_class}, Probabilities: {probabilities}")
