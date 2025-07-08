import pandas as pd

# Load the dataset
df = pd.read_csv("Phishing_Legitimate_full.csv")

# Preview the data
print(df.head())
print("\nColumns:\n", df.columns)
print("\nClass balance:\n", df['CLASS_LABEL'].value_counts())
