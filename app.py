
# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)




# Load the trained ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return "Student Performance Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        study_hours = float(data["study_hours"])
        attendance = float(data["attendance"])
        previous_marks = float(data["previous_marks"])

        # Validate inputs
        if not 0 <= study_hours <= 24:
            return jsonify({"error": "Study hours must be 0–24"}), 400

        if not 0 <= attendance <= 100:
            return jsonify({"error": "Attendance must be 0–100"}), 400

        if not 0 <= previous_marks <= 100:
            return jsonify({"error": "Previous marks must be 0–100"}), 400

        student = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance": attendance,
            "previous_marks": previous_marks
        }])

        prediction = float(model.predict(student)[0])
        prediction = max(0, min(100, prediction))

        return jsonify({
            "predicted_marks": round(prediction, 2)
        })

    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Please provide valid numeric inputs"}), 400

    except Exception:
        return jsonify({"error": "Unable to make prediction"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
