import streamlit as st
import pandas as pd
import plotly.express as px

#up-left diagram
def plot_accord_evolution(df):
    accord_counts = (
        df["mainaccord1"]
        .dropna()
        .value_counts()
        .head(8)
        .reset_index()
    )
    accord_counts.columns = ["Accord", "Count"]
    accord_counts = accord_counts.sort_values(by="Count", ascending=True)
    total_scents = len(df)
    accord_counts["Percentage"] = (accord_counts["Count"] / total_scents * 100).round(1)

    fig = px.bar(
        accord_counts,
        x="Count",
        y="Accord",
        orientation="h",
        text=accord_counts["Percentage"].apply(lambda p: f"{p}%"),
        color="Count",
        color_continuous_scale=["#D98E9E", "#7B3B59"],
        title="Share of the most popular accords"
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False,
        textfont=dict(color="#121113", size=12, family="sans-serif")
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False,
        font=dict(color="#121113", family="sans-serif"),
        title=dict(
            font=dict(size=16, weight=700),
            x=0.02,
            y=0.95
        ),
        margin=dict(l=0, r=50, t=50, b=10),
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(0,0,0,0.06)",
            zeroline=False,
            title=""
        ),
        yaxis=dict(
            title="",
            autorange="reversed"
        )
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
