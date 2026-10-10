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

        st.markdown("---")

        all_countries = sorted([c for c in df["country"].dropna().unique() if str(c).strip() != ""])
        selected_countries = st.multiselect(
            "Country / Origin:",
            options=all_countries,
            placeholder="All countries"
        )

        top_brands = df["brand"].value_counts().head(30).index.tolist()
        other_brands = sorted([b for b in df["brand"].dropna().unique() if b not in top_brands])
        all_brands = top_brands + other_brands
        selected_brands = st.multiselect(
            "Brand:",
            options=all_brands,
            placeholder="All brands"
        )

        min_ratings = st.slider(
            "Min. Ratings (Popularity):",
            min_value=0,
            max_value=1000,
            value=25,
            step=25
        )

    filtered_df = df[
        (df["year"] >= selected_years[0]) &
        (df["year"] <= selected_years[1]) &
        (df["gender"].astype(str).str.lower().isin(active_genders)) &
        (df["rating_count"] >= min_ratings)
        ]

    if selected_countries:
        filtered_df = filtered_df[filtered_df["country"].isin(selected_countries)]

    if selected_brands:
        filtered_df = filtered_df[filtered_df["brand"].isin(selected_brands)]

    return filtered_df


def render_kpis(filtered_df):
    total_perfumes = len(filtered_df)
    avg_rating = round(filtered_df['rating_value'].mean(),
                       2) if not filtered_df.empty and 'rating_value' in filtered_df.columns else 0.0

    if not filtered_df.empty and 'brand' in filtered_df.columns and not filtered_df['brand'].dropna().empty:
        kpi3_title = "MOST ACTIVE BRAND"
        kpi3_val = str(filtered_df['brand'].mode()[0]).title()
    else:
        kpi3_title = "MOST ACTIVE BRAND"
        kpi3_val = "N/A"

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="ALL SCENTS", value=f"{total_perfumes:,}".replace(",", " "))
    with col2:
        st.metric(label="AVERAGE RATING", value=f"{avg_rating} / 5")
    with col3:
        st.metric(label=kpi3_title, value=kpi3_val)