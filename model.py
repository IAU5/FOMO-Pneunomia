import onnxruntime as ort
import numpy as np

class FOMOModel:
    def __init__(self, model_path="model.onnx"):
        """Initialize the ONNX Runtime session."""
        self.session = ort.InferenceSession(model_path)

    def preprocess(self, input_data):
        """Resize and normalize input data if necessary.
        Modify this function as needed to match your model input requirements.
        """
        input_data = np.expand_dims(input_data, axis=0)  # Add batch dimension
        input_data = input_data.astype(np.float32)  # Ensure the data type matches the ONNX model
        return input_data

    def predict(self, input_data):
        """Run inference using the ONNX model."""
        input_data = self.preprocess(input_data)
        inputs = {self.session.get_inputs()[0].name: input_data}
        outputs = self.session.run(None, inputs)
        return outputs
