import joblib
import numpy as np

model = joblib.load("house_price_model.pkl")


def predict_house_price(
    area,
    bedrooms,
    bathrooms,
    stories,
    mainroad,
    guestroom,
    basement,
    hotwaterheating,
    airconditioning,
    parking,
    prefarea,
    furnishing
):

    features = np.array([[
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnishing
    ]])

    prediction = model.predict(features)

    return prediction[0]
