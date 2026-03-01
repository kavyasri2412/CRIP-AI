import pandas as pd
import numpy as np

# Create synthetic governance dataset
np.random.seed(42)

data = pd.DataFrame({
    "corruption_index": np.random.randint(10, 100, 200),
    "public_complaints": np.random.randint(0, 500, 200),
    "fund_utilization_gap": np.random.randint(0, 100, 200),
    "delay_days": np.random.randint(0, 365, 200),
    "audit_flags": np.random.randint(0, 10, 200),
})

# Risk formula (custom logic)
data["risk_level"] = (
    0.3 * data["corruption_index"] +
    0.2 * data["public_complaints"] +
    0.2 * data["fund_utilization_gap"] +
    0.2 * data["delay_days"] +
    5 * data["audit_flags"]
)

# Convert to categories
data["risk_level"] = pd.cut(
    data["risk_level"],
    bins=[0, 150, 300, 1000],
    labels=[0, 1, 2]
)

data.to_csv("governance_data.csv", index=False)

print("Dataset created successfully!")

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

X = data.drop("risk_level", axis=1)
y = data["risk_level"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "risk_model.pkl")

print("Model trained and saved!")