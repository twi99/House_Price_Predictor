def load_css():
    return """
    <style>

    /* 🌤️ Sky Background */
    .stApp {
        background: linear-gradient(to bottom, #87CEEB, #E0F7FF);
        color: #111827;
    }

    /* 📌 Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #b3e5fc, #e1f5fe);
    }

    /* 📝 All Text */
    p, span, label, div {
        color: #111827 !important;
    }

    /* 🧾 Main Title */
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #0d47a1;
    }

    /* Subtitle */
    .sub-title {
        text-align: center;
        color: #1f2937;
        font-size: 20px;
        font-weight: 500;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #111827 !important;
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #111827 !important;
        font-weight: bold;
    }

    [data-testid="stMetricLabel"] {
        color: #374151 !important;
    }

    /* Buttons */
    .stButton>button {
        font-weight: bold;
        border-radius: 10px;
    }

    /* Input labels */
    .stSelectbox label,
    .stSlider label,
    .stNumberInput label {
        color: #111827 !important;
        font-weight: 600;
    }

    /* Cards */
    div[data-testid="stExpander"] {
        background: white;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }

    /* Inputs */
    input, select, textarea {
        border-radius: 10px !important;
        color: #111827 !important;
    }

    </style>
    """
