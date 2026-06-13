# 🇮🇳 India Unemployment Analysis Dashboard

An interactive dashboard to analyze unemployment trends across Indian states, especially during COVID-19, built with Python, Pandas, Plotly, and Streamlit.

## 🔗 Demo
> Add a screenshot or GIF of the app here after running it locally.
> Example: `![App Screenshot](screenshot.png)`

## 📌 Problem Statement
The unemployment rate is a key economic indicator, and it spiked sharply during COVID-19. This project builds a dashboard to explore unemployment trends across Indian states over time.

## 🛠 Tech Stack
- Python
- Pandas (data cleaning)
- Plotly (interactive charts)
- Streamlit (dashboard)

## 📊 Dataset
`Unemployment in India.csv` — state-wise unemployment rate data over time.

## 🧠 Approach
1. **Data Cleaning**: Stripped column names, dropped rows with missing region values, and parsed dates.
2. **State-wise View**: Selecting a state shows its unemployment trend over time, along with average, highest, and lowest rates.
3. **COVID Impact Level**: A simple rule-based indicator (Low / Moderate / Severe) based on the average unemployment rate.
4. **National View**: An overall India-wide trend line (average across all states per date).
5. **State Comparison**: A bar chart ranking all states by their average unemployment rate.

## ✅ Result
A fully interactive dashboard where selecting a state instantly updates the trend chart, KPI cards, and summary — alongside a national overview and state-wise comparison.

## 🚀 How to Run
```bash
pip install streamlit pandas plotly
streamlit run app.py
```
The app opens automatically in your browser.

## 📂 Project Structure
```
Unemployment_Analysis/
├── app.py                              # Streamlit dashboard
├── Unemployment in India.csv             # Dataset
└── Unemployment_Rate_upto_11_2020.csv     # Additional dataset (regional breakdown)
```

## 💡 What I Learned
- Cleaning and parsing real-world messy datasets (column names, dates, missing values)
- Building interactive visualizations with Plotly
- Designing a multi-section analytical dashboard with Streamlit
- Translating raw data into simple, interpretable insights (e.g. impact levels)
