import streamlit as st
from pathlib import Path
import warnings
from src.data_loader import load_cleaned_data
from src.utils import set_jpg_background
from src.components import render_sidebar, render_kpis
warnings.filterwarnings("ignore")

BASE_DIR = Path(__file__).resolve().parent
BG_IMAGE_PATH = BASE_DIR / "assets" / "wallpaper2.jpg"

st.set_page_config(page_title="Perfume analysis", page_icon="assets/perfume.png", layout="wide")
set_jpg_background(str(BG_IMAGE_PATH))
st.markdown("<h1 style='color: #121113; font-weight: 700;'>Perfume Analysis</h1>", unsafe_allow_html=True)

df = load_cleaned_data()
filtered_df = render_sidebar(df)
render_kpis(filtered_df)
