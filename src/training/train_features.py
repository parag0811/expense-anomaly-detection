import pandas as pd

df = pd.read_csv("../../data/processed/features.csv")
df = df.drop(columns=['Unnamed: 0'])
df.head(5)

X = df
from sklearn.model_selection import train_test_split

X_train, X_test= train_test_split(X, test_size=0.2,random_state=42 )

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train) # Computes mean and STD of each column

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training the model
from sklearn.ensemble import IsolationForest
model = IsolationForest(random_state=42, contamination=0.1) 
model.fit(X_train_scaled)

import joblib

joblib.dump(model, "../../models/anomaly_model.pk")
joblib.dump(scaler, "../../models/scaler.pk")

model.predict(X_test_scaled)

model.decision_function(X_train_scaled)

df_trained = X_train.copy()
df_trained['prediction'] = model.predict(X_train_scaled)
df_trained.head(10)

df_trained['prediction'].value_counts() # Contamination

anomalies = df_trained[df_trained['prediction'] == -1]
anomalies


