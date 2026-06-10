import pandas as pd
import joblib
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

print("Loading dataset...")

# Load dataset
df = pd.read_csv(
    "data/UpdatedResumeDataSet.csv"
)

X = df["Resume"]
y = df["Category"]

print("Training TF-IDF...")

# TF-IDF
tfidf = TfidfVectorizer(
    stop_words="english"
)

X_vectorized = tfidf.fit_transform(X)

print("Training model...")

# Model
model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_vectorized,
    y
)

# Create models folder
os.makedirs(
    "models",
    exist_ok=True
)

print("Saving files...")

# Save model
joblib.dump(
    model,
    "models/model.pkl"
)

joblib.dump(
    tfidf,
    "models/tfidf.pkl"
)

print("✅ Model saved successfully!")