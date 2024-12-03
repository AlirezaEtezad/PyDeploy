import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import onnx
import skl2onnx
from skl2onnx.common.data_types import FloatTensorType

# Mock dataset (same features as in your prediction)
data = {
    "district": ["A", "B", "C", "D"],  # Categorical variable for district
    "area": [1200, 1500, 2000, 2500],
    "rooms": [2, 3, 3, 4],
    "price": [200000, 250000, 300000, 400000],
}
df = pd.DataFrame(data)

# For simplicity, let's assume "district" is categorical and use its numeric encoding
df["district"] = pd.Categorical(df["district"]).codes  # Encode district as numerical

# Features and target
X = df[["district", "area", "rooms"]]  # Using district, area, and rooms for prediction
y = df["price"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Export to ONNX
initial_type = [("float_input", FloatTensorType([None, 3]))]  # 3 features: district, area, rooms
onnx_model = skl2onnx.convert_sklearn(model, initial_types=initial_type)
with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Model exported to model.onnx")
