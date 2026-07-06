def load_css():
    return """
    <style>

    /* 🌤️ Sky Background */
    .stApp {
        background: linear-gradient(to bottom, #87CEEB, #E0F7FF);
        color: #1a1a1a;
    }

    /* 📌 Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #b3e5fc, #e1f5fe);
    }

    /* 🧾 Main Title */
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #0d47a1;
    }

    /* 🪟 Cards */
    div[data-testid="stExpander"] {
        background: white;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }

    /* 🔘 Inputs */
    input, select, textarea {
        border-radius: 10px !important;
    }

    </style>
    """
