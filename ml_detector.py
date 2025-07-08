import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Phishing_Legitimate_full.csv")

# Drop URL column if it exists (not needed for ML model)
if 'URL' in df.columns:
    df = df.drop(columns=['URL'])

# Features and Labels
X = df.drop(columns=['CLASS_LABEL'])
y = df['CLASS_LABEL']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict a sample URL (replace this with your real input later)
sample = X.iloc[[0]]  # Double brackets to keep it as DataFrame
print("Prediction:", model.predict(sample))


print("Expected feature count:", X.shape[1])
user_input = [[1, 0, 0, -1, 1, 0, 1, -1, 1, 0, -1, 0, 1, 0, -1, 1, 0, -1, 1, 0, -1, 1, 0, 1, -1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 0, -1, 1, 0, 1, -1, 1, 0, -1, 1, 0, 1, -1]]

user_input = X.iloc[[1]]  # Just a real sample row from dataset
print("User Prediction:", model.predict(user_input))
import joblib

# Save the model
joblib.dump(model, "phishing_rf_model.pkl")
print("Model saved as phishing_rf_model.pkl")
