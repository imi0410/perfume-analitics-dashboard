import streamlit as st
import plotly.express as px
import os
from src.utils import set_jpg_background
from pathlib import Path
import warnings
from src.data_loader import load_cleaned_data
warnings.filterwarnings("ignore")

BASE_DIR = Path(__file__).resolve().parent
BG_IMAGE_PATH = BASE_DIR / "assets" / "wallpaper2.jpg"
df = load_cleaned_data()

#Settings
st.set_page_config(page_title="Perfume analysis", page_icon="assets/perfume.png", layout="wide")
st.markdown("<h1 style='color: #121113; font-weight: 700;'>Perfume Analysis</h1>", unsafe_allow_html=True)
set_jpg_background(str(BG_IMAGE_PATH))

#Sidebar
with st.sidebar:
    st.markdown("FILTERS")
    selected_years = st.slider(
        "Kiadási év:",
        min_value=1980,
        max_value=int(df["year"].max()),
        value=(1995, int(df["year"].max()))
    )
    selected_genders = st.pills(
        "Gender:",
        options=["unisex", "women", "men"],
        default=["unisex", "women", "men"],
        selection_mode="multi"
    )