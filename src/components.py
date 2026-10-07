import streamlit as st

def render_sidebar(df):
    with st.sidebar:
        st.markdown("FILTERS")

        min_year = int(df["year"].dropna().min()) if "year" in df.columns else 1980
        max_year = int(df["year"].dropna().max()) if "year" in df.columns else 2024

        selected_years = st.slider(
            "Release date:",
            min_value=min_year,
            max_value=max_year,
            value=(1995, max_year)
        )

        selected_genders = st.pills(
            "Gender:",
            options=["unisex", "women", "men"],
            default=["unisex", "women", "men"],
            selection_mode="multi"
        )

    active_genders = selected_genders if selected_genders else ["unisex", "women", "men"]

    filtered_df = df[
        (df["year"] >= selected_years[0]) &
        (df["year"] <= selected_years[1]) &
        (df["gender"].astype(str).str.lower().isin(active_genders))
        ]
    return filtered_df


def render_kpis(filtered_df):
    total_perfumes = len(filtered_df)
    avg_rating = round(filtered_df['rating_value'].mean(),
                       2) if not filtered_df.empty and 'rating_value' in filtered_df.columns else 0.0

    if 'main_accord' in filtered_df.columns and not filtered_df['main_accord'].dropna().empty:
        kpi3_title = "DOMINANT ACCORD"
        kpi3_val = str(filtered_df['main_accord'].mode()[0]).capitalize()
    elif 'brand' in filtered_df.columns and not filtered_df['brand'].dropna().empty:
        kpi3_title = "MOST ACTIVE BRAND"
        kpi3_val = str(filtered_df['brand'].mode()[0])
    else:
        kpi3_title = "STATUS"
        kpi3_val = "N/A"

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="ALL SCENTS", value=f"{total_perfumes:,}".replace(",", " "))
    with col2:
        st.metric(label="AVERAGE RATING", value=f"{avg_rating} / 5")
    with col3:
        st.metric(label=kpi3_title, value=kpi3_val)