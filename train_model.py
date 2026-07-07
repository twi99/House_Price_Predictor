import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("dataset/Housing.csv")

# Convert yes/no columns into 1/0
yes_no_columns = [
    "mainroad", "guestroom", "basement",
    "hotwaterheating", "airconditioning",
    "prefarea"
]

for col in yes_no_columns:
    data[col] = data[col].map({"yes": 1, "no": 0})

# Convert furnishingstatus into numbers
data["furnishingstatus"] = data["furnishingstatus"].map({
    "furnished": 2,
    "semi-furnished": 1,
    "unfurnished": 0
})

# Features and Target
X = data.drop("price", axis=1)
y = data["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "house_price_model.pkl")

# Accuracy
accuracy = model.score(X_test, y_test)

print("Model Trained Successfully!")
print("Accuracy:", accuracy)
