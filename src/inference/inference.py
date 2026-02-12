import os 
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "models", "anomaly_model.pk")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pk")

# Loading the model
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
# run once when app starts — not per request.


# Inference Function that returns :
# {
#   "anomaly_score": -0.42,
#   "is_suspicious": true
# }

FEATURE_ORDER = ["amount", "hour", "day_of_week", "time_gap_minutes"]

def predict_expense(amount, hour, day_of_week, time_gap_minutes):
    features  = np.array([[amount,hour,day_of_week, time_gap_minutes]])

    scaled_features = scaler.transform(features)
    print(scaled_features)

    anomaly_score = model.decision_function(scaled_features)[0]

    prediction = model.predict(scaled_features)[0]

    return {
        "anomaly_score": float(anomaly_score),
        "is_suspicious": bool(prediction == -1)
    }

if __name__ == "__main__":
    result = predict_expense(
        amount=18000,
        hour=2,
        day_of_week=6,
        time_gap_minutes=1
    )

    print(result)
