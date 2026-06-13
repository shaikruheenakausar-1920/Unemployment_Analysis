import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="India Employment Pulse",
    page_icon="🇮🇳",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("Unemployment in India.csv")

df.columns = df.columns.str.strip()

df = df.dropna(subset=["Region"])

df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# ==========================
# HEADER
# ==========================

st.title("🇮🇳 India Employment Pulse")

st.markdown(
    """
    ### COVID-19 Unemployment Intelligence Dashboard

    Discover how COVID-19 affected employment in your state.
    Select a state and explore unemployment trends in a simple and interactive way.
    """
)

st.divider()

# ==========================
# SIDEBAR
# ==========================

st.sidebar.header("📍 State Explorer")

states = sorted(df["Region"].dropna().unique())

selected_state = st.sidebar.selectbox(
    "Select Your State",
    states
)

# ==========================
# STATE DATA
# ==========================

state_data = df[df["Region"] == selected_state]

avg_state = round(
    state_data["Estimated Unemployment Rate (%)"].mean(),
    2
)

max_state = round(
    state_data["Estimated Unemployment Rate (%)"].max(),
    2
)

min_state = round(
    state_data["Estimated Unemployment Rate (%)"].min(),
    2
)

# ==========================
# COVID IMPACT LEVEL
# ==========================

if avg_state >= 20:
    impact = "🔴 Severe"
elif avg_state >= 10:
    impact = "🟠 Moderate"
else:
    impact = "🟢 Low"

# ==========================
# KPI CARDS
# ==========================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📊 Average Rate",
    f"{avg_state}%"
)

col2.metric(
    "📈 Highest Rate",
    f"{max_state}%"
)

col3.metric(
    "📉 Lowest Rate",
    f"{min_state}%"
)

col4.metric(
    "🦠 COVID Impact",
    impact
)

st.divider()

# ==========================
# TREND GRAPH
# ==========================

st.subheader(
    f"📈 Unemployment Trend in {selected_state}"
)

fig = px.line(
    state_data,
    x="Date",
    y="Estimated Unemployment Rate (%)",
    markers=True,
    title=f"{selected_state} Unemployment Trend"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Unemployment Rate (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# STATE SUMMARY
# ==========================

st.divider()

st.subheader("🤖 COVID Impact Summary")

st.success(
    f"""
📍 State: {selected_state}

📊 Average Unemployment Rate: {avg_state}%

📈 Highest Recorded Unemployment: {max_state}%

📉 Lowest Recorded Unemployment: {min_state}%

🦠 COVID Impact Level: {impact}

This dashboard helps understand how unemployment changed in
{selected_state} during the COVID-19 period.
"""
)

# ==========================
# FOOTER
# ==========================

st.divider()

st.caption(
    "Developed using Python, Streamlit, Pandas and Plotly"
)
st.divider()
st.subheader("🇮🇳 Overall India Trend")

national_trend = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean().reset_index()

fig_national = px.line(
    national_trend,
    x="Date",
    y="Estimated Unemployment Rate (%)",
    markers=True,
    title="Average Unemployment Rate Across India"
)
st.plotly_chart(fig_national, use_container_width=True)

st.divider()
st.subheader("🏆 States Ranked by Average Unemployment")

state_avg = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean().reset_index()
state_avg = state_avg.sort_values("Estimated Unemployment Rate (%)", ascending=False)

fig_states = px.bar(
    state_avg,
    x="Region",
    y="Estimated Unemployment Rate (%)",
    color="Estimated Unemployment Rate (%)",
    color_continuous_scale="Reds",
    title="Average Unemployment Rate by State"
)
fig_states.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_states, use_container_width=True)