import base64
from pathlib import Path
import streamlit as st

def set_jpg_background(jpg_file_path: str):
    with open(jpg_file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        /* 1. Fejléc átlátszóvá tétele, visszanyitó gomb megtartása */
        header[data-testid="stHeader"] {{
            background-color: transparent !important;
        }}

        header[data-testid="stHeader"] button,
        [data-testid="collapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button {{
            color: #FFFFFF !important;
            background-color: #121113 !important;
            border-radius: 8px !important;
        }}

        /* 2. Háttérkép finom réteggel */
        .stApp {{
            background-image: 
                linear-gradient(rgba(255, 255, 255, 0.70), rgba(255, 255, 255, 0.70)),
                url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* 3. Margók minimalizálása, cím felhúzása */
        .block-container,
        [data-testid="stMainBlockContainer"],
        .stMainBlockContainer {{
            padding-top: 1rem !important;
            padding-bottom: 2rem !important;
        }}

        h1, [data-testid="stHeading"] h1 {{
            color: #121113 !important;
            font-weight: 700;
            margin-top: 0rem !important;
            padding-top: 0rem !important;
        }}

        /* 4. Mélyfekete Sidebar */
        section[data-testid="stSidebar"] {{
            background-color: #0E0E10 !important;
        }}

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span {{
            color: #F0F2F6 !important;
        }}

        section[data-testid="stSidebar"] hr {{
            border-color: #262730 !important;
        }}

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {{
            background-color: #1A1C23 !important;
            border: 1px solid #30363D !important;
            border-radius: 10px !important;
        }}

        section[data-testid="stSidebar"] span[data-baseweb="tag"] {{
            background-color: #2D3139 !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 6px !important;
        }}

        section[data-testid="stSidebar"] span[data-baseweb="tag"] span,
        section[data-testid="stSidebar"] span[data-baseweb="tag"] svg {{
            color: #FFFFFF !important;
            fill: #FFFFFF !important;
        }}

        section[data-testid="stSidebar"] div[data-baseweb="select"] svg {{
            fill: #8B949E !important;
        }}

        /* 5. Glassmorphism kártyák a leendő diagramok és KPI-k mögé */
        div[data-testid="stVerticalBlock"] > div:has(div.stPlotlyChart),
        div[data-testid="stMetric"] {{
            background: rgba(255, 255, 255, 0.65) !important;
            backdrop-filter: blur(12px) !important;
            border-radius: 16px !important;
            padding: 16px !important;
            box-shadow: 0 8px 24px 0 rgba(0, 0, 0, 0.06) !important;
            border: 1px solid rgba(255, 255, 255, 0.4) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )