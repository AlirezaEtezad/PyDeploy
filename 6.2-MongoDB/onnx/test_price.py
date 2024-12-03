import onnxruntime as ort
import numpy as np

session = ort.InferenceSession("onnx/model.onnx")

input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name
sample_input = np.array([[0, 1800, 3]], dtype=np.float32)  # Example input

prediction = session.run([output_name], {input_name: sample_input})
print("Predicted price:", prediction)
