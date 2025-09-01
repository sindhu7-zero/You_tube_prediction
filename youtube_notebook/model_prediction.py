import streamlit as st
import pandas as pd
import pickle

# Load Model
with open(r'C:\Users\admin\Documents\youtube_project\youtube_notebook\youtube_revenue_model.pkl','rb') as f:
    model = pickle.load(f)

# Page Config
st.set_page_config(page_title="YouTube Revenue Predictor", page_icon="📺", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background color or gradient */
        .stApp {
            background: linear-gradient(to right, #e3f2fd, #bbdefb);
        }

        /* Title */
        .title {
            text-align: center;
            font-size: 40px;
            color: #0d47a1;
            font-weight: bold;
            margin-bottom: 5px;
        }

        /* Subtitle */
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #1e3a5f;
            margin-bottom: 30px;
        }

        /* Input labels */
        label, .stSelectbox label {
            font-size: 16px !important;
            font-weight: 500 !important;
            color: #0d47a1 !important;
        }

        /* Button */
        .stButton>button {
            background-color: #1565c0;
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #0d47a1;
            color: white;
        }

        /* Prediction Result */
        .result {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #2e7d32;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown('<h1 class="title">📺 YouTube Revenue Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Fill in the details of your video to estimate the ad revenue 💰</p>', unsafe_allow_html=True)

# ---- User Inputs ----
col1, col2 = st.columns(2)
with col1:
    views = st.number_input("👀 Total Views", min_value=0, step=1000)
    likes = st.number_input("👍 Total Likes", min_value=0, step=100)
    comments = st.number_input("💬 Total Comments", min_value=0, step=10)
    watch_time = st.number_input("⏱️ Watch Time (minutes)", min_value=0.0, step=10.0, format="%.2f")

with col2:
    subscribers = st.number_input("👥 Subscribers", min_value=0, step=100)
    category = st.selectbox("🎭 Category", ["Entertainment", "Gaming", "Education", "Music", "Tech","Lifestyle"])
    device = st.selectbox("📱 Device", ["Mobile", "Tablet", "Desktop", "TV"])
    country = st.selectbox("🌍 Country", ["IN", "US", "UK", "CA", "AU"])

# ---- Prediction ----
if st.button("Estimate Revenue"):
    # Create DataFrame for model
    input_data = {
        "views": [views],
        "likes": [likes],
        "comments": [comments],
        "watch_time_minutes": [watch_time],
        "subscribers": [subscribers],
        "category": [category],
        "device": [device],
        "country": [country]
    }
    input_df = pd.DataFrame(input_data)

    # Predict revenue
    prediction = model.predict(input_df)[0]

    # Show result
    st.markdown(f'<p class="result">💰 Estimated Revenue: <b>${prediction:.2f}</b></p>', unsafe_allow_html=True)
