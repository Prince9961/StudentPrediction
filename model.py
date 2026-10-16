
# model.py

import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Sample training dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "previous_marks": [30, 35, 40, 45, 50, 60, 65, 70, 80, 85],
    "final_marks": [25, 32, 38, 45, 52, 62, 68, 75, 85, 92]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "previous_marks"]]
y = df["final_marks"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("ML model trained and saved successfully!")
