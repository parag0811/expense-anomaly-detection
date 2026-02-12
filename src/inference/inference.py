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

FEATURE_ORDER = ["amount", "past_transaction_count", "user_avg_amount", "amount_minus_user_avg", "time_gap_minutes", "hour", "day_of_week",  ]

def predict_expense(amount, past_transaction_count, user_avg_amount, amount_minus_user_avg, time_gap_minutes, hour, day_of_week):
    features  = np.array([[amount, past_transaction_count, user_avg_amount, amount_minus_user_avg, time_gap_minutes, hour, day_of_week]])

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
        amount=1000, past_transaction_count=69, user_avg_amount=1200, amount_minus_user_avg=-300, time_gap_minutes=20, hour=12, day_of_week=6
    )

    print(result)
