import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=6, random_state=42)
df = pd.DataFrame(X, columns=[
    "amount", "merchant", "location_id", "transaction_type", "customer_age", "device_trust_score"
])
df["is_fraud"] = y

X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model.joblib")
