import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("dataset/movie_dataset.csv")

# Encode categorical columns
le = LabelEncoder()
df["Genre"] = le.fit_transform(df["Genre"])

X = df.drop("Genre", axis=1)
y = df["Genre"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/gb_model.pkl")
