import pandas as pd
import matplotlib.pyplot as plt


def price_distribution():
    """
    Plot house price distribution.
    """
    df = pd.read_csv("dataset/Housing.csv")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(df["price"], bins=20, edgecolor="black")

    ax.set_title("House Price Distribution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Number of Houses")

    plt.tight_layout()

    return fig


def feature_importance():
    """
    Plot feature importance.
    """

    features = [
        "Area",
        "Bedrooms",
        "Bathrooms",
        "Stories",
        "Parking",
        "Main Road",
        "Guest Room",
        "Basement",
        "Air Conditioning",
        "Preferred Area"
    ]

    importance = [
        0.74,
        0.06,
        0.05,
        0.04,
        0.03,
        0.02,
        0.02,
        0.01,
        0.02,
        0.01
    ]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.barh(features, importance)

    ax.set_title("Feature Importance")
    ax.set_xlabel("Importance Score")

    plt.tight_layout()

    return fig


if __name__ == "__main__":
    print("charts.py loaded successfully")
