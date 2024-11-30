import onnxruntime as ort
import numpy as np

class FOMOModel:
    def __init__(self, model_path):
        self.session = ort.InferenceSession(model_path)

    def predict(self, input_data):
        # Ensure input_data matches the ONNX model's expected shape
        inputs = {self.session.get_inputs()[0].name: input_data}
        outputs = self.session.run(None, inputs)
        return outputs  # Return probabilities or class predictions
