# Phishing-Website-Detection-Tool

 Project Overview
 
Phishing websites are deceptive sites designed to trick users into providing sensitive information like login credentials, banking info, or personal data. This tool uses both Rule-Based logic and a Machine Learning model to identify potentially malicious URLs.

Objective

To build a lightweight and effective phishing detection tool that:

Flags suspicious URLs using rule-based heuristics

Applies a trained ML model to detect phishing characteristics

 Technologies Used
 
Technology	Description

Python	Core programming language

Pandas	Data preprocessing and loading CSV

Scikit-learn	Machine Learning (Random Forest Classifier)

Regex	Pattern matching for rule-based detection

Tkinter	GUI development (optional)

Joblib	Saving and loading ML models

URLLib/Parse	URL analysis for rule-based logic

📁 Project Structure

bash

Copy

Edit

Project1Cy/

├── Phishing_Legitimate_full.csv      # Dataset

├── ml_detector.py                    # Trains ML model and saves pkl

├── phishing_rf_model.pkl             # Saved ML model

├── gui.py                            # GUI version (Tkinter)

├── rule_based.py                     # Rule-based detector script


├── combined_detector.py              # Combines ML + Rule-based

├── README.md                         # Project documentation

 ML Model Used

Model: RandomForestClassifier

Input Features: 49 numerical features (engineered from URLs)

Target: CLASS_LABEL (0 = Legitimate, 1 = Phishing)

Accuracy: ~100% on provided dataset (for demo)

How to Run
1. Install Dependencies

pip install pandas scikit-learn joblib
2. Train & Save ML Model


python ml_detector.py

3. Run Combined Detector

python combined_detector.py

4. (Optional) Run GUI Version

python gui.py

Features
✅ Rule-based pattern checks (@, IP in domain, hyphens, keywords)

✅ ML prediction using trained model

✅ GUI interface for user input (optional)

✅ Easy to extend with more features

