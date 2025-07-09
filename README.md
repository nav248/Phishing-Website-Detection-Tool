# Phishing-Website-Detection-Tool

 Project Overview:
 
Phishing websites are deceptive sites designed to trick users into providing sensitive information like login credentials, banking info, or personal data. This tool uses both Rule-Based logic and a Machine Learning model to identify potentially malicious URLs.

Objective:

To build a lightweight and effective phishing detection tool thatFlags suspicious URLs using rule-based heuristics Applies a trained ML model to detect phishing characteristics

 Technologies Used:

1.Python	Core- programming language

2.Pandas	-Data preprocessing and loading CSV

3.Scikit-learn	-Machine Learning (Random Forest Classifier)

4.Regex	Pattern - matching for rule-based detection

5.Tkinter -	GUI development (optional)

6.Joblib -	Saving and loading ML models

7.URLLib/Parse -	URL analysis for rule-based logic


How to Run:

1. Install Dependencies

pip install pandas scikit-learn joblib

2. Train & Save ML Model

python ml_detector.py

3. Run Combined Detector

python combined_detector.py

4. (Optional) Run GUI Version

python gui.py

Features:

1. Rule-based pattern checks (@, IP in domain, hyphens, keywords)

2. ML prediction using trained model

3. GUI interface for user input (optional)

4. Easy to extend with more features

