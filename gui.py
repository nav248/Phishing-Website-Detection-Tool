import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load the saved model
model = joblib.load("phishing_rf_model.pkl")
feature_count = 49  # Change this if your feature count is different

# Predict function
def predict_phishing():
    try:
        # Read and parse input
        raw_input = entry.get()
        values = list(map(int, raw_input.strip().split(',')))

        if len(values) != feature_count:
            raise ValueError(f"Expected {feature_count} features, got {len(values)}")

        # Predict
        input_array = np.array([values])
        prediction = model.predict(input_array)[0]

        # Show result
        if prediction == 1:
            result = " This looks like a PHISHING website!"
        else:
            result = " This seems like a LEGITIMATE website."
        messagebox.showinfo("Prediction Result", result)

    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

# GUI setup
root = tk.Tk()
root.title("Phishing Website Detector")
root.geometry("500x300")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Phishing Website Detector", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

instruction = tk.Label(root, text=f"Enter {feature_count} comma-separated numeric features:", bg="#f0f0f0")
instruction.pack()

entry = tk.Entry(root, width=80)
entry.pack(pady=10)

predict_btn = tk.Button(root, text="Predict", command=predict_phishing, bg="#4caf50", fg="white", font=("Arial", 12))
predict_btn.pack(pady=10)

root.mainloop()
