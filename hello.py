import pandas as pd
import plotly.express as px
import preswald

# ✅ Formatting function with aligned columns
def format_table_aligned(df, max_rows=10):
    df = df.head(max_rows)
    return df.to_string(index=False, col_space=15, justify="center")

# Load dataset
df = pd.read_csv("data/seattle-weather.csv")
df["precipitation"] = pd.to_numeric(df["precipitation"], errors="coerce")

# Filter for significant precipitation
significant_rain = df[df["precipitation"] > 0.5]

# App Introduction
preswald.text("# Seattle Weather 🌧️")
preswald.text("## Weather Data Overview")
preswald.text("This app analyzes Seattle's weather based on historical data.")

# 📊 Show original data preview with aligned columns
preswald.text("### Weather Data Preview")
preswald.text(format_table_aligned(df))

# 📊 Show filtered data if available
if not significant_rain.empty:
    preswald.text("### Filtered (Precip > 0.5)")
    preswald.text(format_table_aligned(significant_rain))

    # 📈 Plot chart
    fig = px.line(
        significant_rain,
        x="date",
        y="precipitation",
        title="Significant Rainfall Days in Seattle"
    )
    preswald.plotly(fig)
else:
    preswald.text("⚠️ No data found with precipitation > 0.5 inches.")
