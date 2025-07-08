import re
import joblib
import numpy as np
from urllib.parse import urlparse

# Load ML model
model = joblib.load("phishing_rf_model.pkl")
feature_count = 49  # Must match your model's expected input

# --- RULE-BASED CHECK ---
def is_ip_address(domain):
    return bool(re.fullmatch(r'\d+\.\d+\.\d+\.\d+', domain))

def rule_based_check(url):
    suspicious_words = ['login', 'verify', 'secure', 'account', 'update', 'bank', 'confirm']
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    if '@' in url:
        return True, "Contains '@' symbol — suspicious."
    if '//' in url[8:]:
        return True, "Contains '//' beyond protocol — suspicious."
    if '-' in domain:
        return True, "Hyphen in domain name — common in phishing."
    if is_ip_address(domain):
        return True, "Domain is an IP address — suspicious."
    if url.count('.') > 4:
        return True, "Too many dots — suspicious subdomains."
    if any(word in url.lower() for word in suspicious_words):
        return True, "Contains suspicious keyword — phishing suspected."

    return False, "No obvious rule-based phishing signs detected."

# --- ML CHECK (uses dummy features for now) ---
def ml_check():
    # Dummy test feature vector (replace with real feature extractor later)
    features = [1, 0, 0, -1, 1, 0, 1, -1, 1, 0, -1, 0, 1, 0, -1, 1, 0, -1, 1, 0,
                -1, 1, 0, 1, -1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 0, -1, 1, 0, 1, -1,
                1, 0, -1, 1, 0, 1, -1]

    if len(features) != feature_count:
        return "Feature count mismatch. Cannot proceed with ML prediction."

    prediction = model.predict([features])[0]
    return "ML Prediction: PHISHING" if prediction == 1 else "ML Prediction: LEGITIMATE"

# --- Main ---
if __name__ == "__main__":
    print(" Phishing Website Detector (Combined ML + Rule-Based)")
    url = input("Enter the URL to check: ")

    # Rule-Based
    rb_flag, rb_reason = rule_based_check(url)
    print("\n Rule-Based Check Result:")
    print(f"→ {rb_reason}")

    # ML Prediction
    print("\n ML-Based Check Result:")
    print(ml_check())
