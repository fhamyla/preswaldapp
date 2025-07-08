# Seattle Weather Data App 🌧️

This is a simple data app that analyzes and visualizes Seattle's historical weather data using Python, pandas, Plotly, and the preswald framework.

## ✨ Features
- 📥 Loads and previews Seattle weather data
- 🌧️ Filters for days with significant precipitation (> 0.5 inches)
- 📊 Displays formatted tables
- 📈 Plots a line chart of significant rainfall days

## 🛠️ Requirements
- 🐍 Python 3.8+
- 🐼 pandas
- 📦 plotly
- 🖥️ preswald

## ⚡ Setup
1. Install dependencies:
   ```sh
   pip install pandas plotly preswald
   ```
2. Make sure the data file `data/seattle-weather.csv` is present.

## 🚀 Running the App
Run the following command in your terminal:
```sh
python hello.py
```

After starting, the app will display a local server URL (e.g., http://localhost:xxxx). Open this URL in your web browser to view the app.

## 📁 File Structure
- `hello.py` - Main application script
- `data/seattle-weather.csv` - Weather data file
- `images/` - App images and icons

---

**Note:** If you encounter errors related to `preswald`, please check the preswald documentation for the latest usage instructions. 😊
