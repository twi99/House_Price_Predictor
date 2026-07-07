import streamlit as st
import pandas as pd
import numpy as np
import joblib

from style import load_css
from utils import format_price
from model import predict_house_price
import charts
from pdf_report import create_pdf
from ai_helper import get_ai_response
st.set_page_config(
    page_title="🏠 House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS load
st.markdown(load_css(), unsafe_allow_html=True)
# ---------------- Page Config ---------------- #



# ---------------- Load CSS ---------------- #

st.markdown(load_css(), unsafe_allow_html=True)

# ---------------- Load Dataset ---------------- #

df = pd.read_csv("dataset/Housing.csv")

# ---------------- Sidebar ---------------- #

st.sidebar.image(
    "asset/house_banner.png",
    width=300
)

st.sidebar.title("🏠 House Price Predictor")

st.sidebar.markdown("---")

st.sidebar.success("🤖 Model : Linear Regression")

st.sidebar.info(f"📊 Dataset Size : {len(df)} Houses")

st.sidebar.info(f"📈 Features : {df.shape[1]-1}")

st.sidebar.metric("🎯 Model Accuracy", "64.95%")

st.sidebar.markdown("---")

st.sidebar.write("### 💻 Developer")

st.sidebar.write("**Tinkal Kachariya**")

st.sidebar.markdown("---")

st.sidebar.caption("Made with ❤️ using Streamlit")

# ---------------- Header ---------------- #

st.markdown(
"""
<h1 class='main-title'>
🏠 House Price Prediction
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p class='sub-title'>
Predict House Prices using Machine Learning
</p>
""",
unsafe_allow_html=True
)

st.markdown("---")

# =========================
# House Details Form
# =========================

st.markdown("## 📝 Enter House Details")

left_col, right_col = st.columns(2)

with left_col:

    area = st.number_input(
        "📐 Area (Square Feet)",
        min_value=500,
        max_value=20000,
        value=5000,
        step=100
    )

    bedrooms = st.slider(
        "🛏 Bedrooms",
        1,
        10,
        3
    )

    bathrooms = st.slider(
        "🚿 Bathrooms",
        1,
        10,
        2
    )

    stories = st.slider(
        "🏢 Stories",
        1,
        4,
        2
    )

    parking = st.slider(
        "🚗 Parking",
        0,
        5,
        2
    )

with right_col:

    mainroad = st.selectbox(
        "🛣 Main Road",
        ["Yes", "No"]
    )

    guestroom = st.selectbox(
        "🛋 Guest Room",
        ["Yes", "No"]
    )

    basement = st.selectbox(
        "🏠 Basement",
        ["Yes", "No"]
    )

    hotwaterheating = st.selectbox(
        "🔥 Hot Water Heating",
        ["Yes", "No"]
    )

    airconditioning = st.selectbox(
        "❄ Air Conditioning",
        ["Yes", "No"]
    )

    prefarea = st.selectbox(
        "📍 Preferred Area",
        ["Yes", "No"]
    )

    furnishing = st.selectbox(
        "🪑 Furnishing Status",
        [
            "Furnished",
            "Semi-Furnished",
            "Unfurnished"
        ]
    )

st.markdown("---")

# =========================
# Property Summary Cards
# =========================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📐 Area", f"{area} sq.ft")

with c2:
    st.metric("🛏 Bedrooms", bedrooms)

with c3:
    st.metric("🚿 Bathrooms", bathrooms)

with c4:
    st.metric("🚗 Parking", parking)

st.markdown("---")

# =========================
# Data Conversion
# =========================

mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0

furnishing_map = {
    "Furnished": 2,
    "Semi-Furnished": 1,
    "Unfurnished": 0
}

furnishing = furnishing_map[furnishing]

st.markdown("## 🤖 Predict House Price")

predict = st.button(
    "🚀 Predict Price",
    use_container_width=True
)

if predict:

    prediction = predict_house_price(
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
    )
    formatted_price = format_price(prediction)

    prompt = f"""
You are an AI Real Estate Advisor.

Analyze the following property.

Area: {area} sq.ft
Bedrooms: {bedrooms}
Bathrooms: {bathrooms}
Stories: {stories}
Parking: {parking}

Predicted Price: ₹{formatted_price}

Explain:
1. Why this price was predicted.
2. Whether it is a good investment.
3. Suggest improvements to increase the value.

Keep the response simple and professional.
"""

    ai_response = get_ai_response(prompt)

    st.balloons()

    st.success("Prediction Generated Successfully!")

    st.markdown("## 💰 Prediction Result")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#2563eb,#1d4ed8);
            padding:35px;
            border-radius:18px;
            text-align:center;
            color:white;
        ">
            <h2>Estimated House Price</h2>
            <h1>{formatted_price}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.metric("🎯 Model Accuracy", "64.95%")
        st.progress(65)

        if prediction >= 10000000:
            st.success("🏆 Luxury House")
        elif prediction >= 5000000:
            st.info("🏡 Mid Range House")
        else:
            st.warning("💰 Budget House")

    st.markdown("---")
    st.subheader("🤖 AI Property Analysis")
    st.write(ai_response)

    create_pdf(
        "Prediction_Report.pdf",
        area,
        bedrooms,
        bathrooms,
        stories,
        parking,
        prediction
    )

    with open("Prediction_Report.pdf", "rb") as pdf:
        st.download_button(
            "📄 Download PDF Report",
            pdf,
            file_name="House_Price_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )
st.markdown("---")

# ==========================
# Analytics Dashboard
# ==========================

st.header("📊 Analytics Dashboard")

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "🏠 Total Houses",
    f"{len(df)}"
)

metric2.metric(
    "💰 Average Price",
    format_price(df["price"].mean())
)

metric3.metric(
    "📈 Maximum Price",
    format_price(df["price"].max())
)

metric4.metric(
    "📉 Minimum Price",
    format_price(df["price"].min())
)

st.markdown("---")

# ==========================
# Charts
# ==========================

chart1, chart2 = st.columns(2)

with chart1:

    st.subheader("📈 House Price Distribution")

    fig = charts.price_distribution()

    st.pyplot(fig, use_container_width=True)

with chart2:

    st.subheader("📊 Feature Importance")

    fig2 = charts.feature_importance()

    st.pyplot(fig2, use_container_width=True)

st.markdown("---")

# ==========================================
# Insights & Recommendations
# ==========================================

st.header("💡 House Buying Insights")

left, right = st.columns(2)

with left:

    st.info("""
### 🏡 Tips Before Buying

✅ Compare multiple properties

✅ Check nearby schools & hospitals

✅ Verify legal documents

✅ Check resale value

✅ Visit the property physically

✅ Check transportation facilities
""")

with right:

    st.success("""
### 🤖 About This Model

Algorithm : Linear Regression

Dataset : Housing.csv

Training Split : 80%

Testing Split : 20%

Accuracy : 64.95%

Language : Python
""")

st.markdown("---")

# ==========================================
# Developer Section
# ==========================================

st.header("👨‍💻 Developer")

col1, col2 = st.columns([1,3])

with col1:

    st.image(
        "asset/tinkal.png",
        width=150
    )

with col2:

    st.markdown("""
## Tinkal Kachariya

AI / Machine Learning Enthusiast

### Skills

- Python
- Machine Learning
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Data Analysis

📧 Email:
kachariyatinkal2005@gmail.com

🌐 GitHub:
https://github.com/twi99/House_Price_Predictor

💼 LinkedIn:
https://www.linkedin.com/in/tinkal-kachariya-23b6b9351?utm_source=share_via&utm_content=profile&utm_medium=member_android
""")
    
    st.markdown("---")

st.header("📌 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.success("""
🐍 Python

✔ NumPy

✔ Pandas

✔ Joblib
""")

with tech2:
    st.info("""
🤖 Machine Learning

✔ Scikit-Learn

✔ Linear Regression

✔ Model Prediction
""")

with tech3:
    st.warning("""
🎨 Frontend

✔ Streamlit

✔ CSS Styling

✔ Responsive Layout
""")
    
    st.markdown("---")

st.header("⭐ Project Features")

st.write("""
✅ Professional Dashboard

✅ House Price Prediction

✅ PDF Report Download

✅ Interactive Charts

✅ Feature Importance

✅ Price Distribution

✅ Beautiful Sidebar

✅ Dark Theme

✅ Responsive UI

✅ Machine Learning Model
""")

st.markdown("---")

st.caption(
"""
© 2026 House Price Prediction

Developed by Tinkal Kachariya

Made using ❤️ Python | Streamlit | Machine Learning
"""
)
