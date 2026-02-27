import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Load your CSV file (update the path if needed)
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\selected_countries_AQI.xlsx")

# Check columns to ensure correct names
print("✅ Columns in your dataset:", df.columns.tolist())

# Filter for India using the country column (update if your column name differs)
df_india = df[df['WHO Country Name'] == 'India']

# Drop missing or invalid values for correlation
df_india = df_india.dropna(subset=['Measurement Year', 'AQI'])

# Convert Measurement Year to numeric if needed
df_india['Measurement Year'] = pd.to_numeric(df_india['Measurement Year'], errors='coerce')
df_india = df_india.dropna(subset=['Measurement Year'])

# Group by year to get average AQI for India
df_india_trend = df_india.groupby('Measurement Year')['AQI'].mean().reset_index()

# If no valid data exists
if df_india_trend.empty:
    print("⚠️ No valid data found for India in the selected_cities.csv file.")
else:
    # Correlation & regression
    corr_india = df_india_trend['Measurement Year'].corr(df_india_trend['AQI'])
    slope, intercept, r_value, p_value, std_err = linregress(
        df_india_trend['Measurement Year'], df_india_trend['AQI']
    )
    line = slope * df_india_trend['Measurement Year'] + intercept

    # Plot
    plt.figure(figsize=(12,6))
    plt.scatter(df_india_trend['Measurement Year'], df_india_trend['AQI'], 
                color='orange', s=100, label='India AQI')
    plt.plot(df_india_trend['Measurement Year'], line, 
             color='red', linestyle='--', linewidth=2, 
             label=f'Trendline (R²={r_value**2:.2f})')

    plt.title("🇮🇳 India AQI Trend Over Years", fontsize=16, fontweight='bold')
    plt.xlabel("Measurement Year", fontsize=13)
    plt.ylabel("Average AQI", fontsize=13)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # Add correlation text to the chart
    plt.text(df_india_trend['Measurement Year'].min(), 
             df_india_trend['AQI'].max(), 
             f"Correlation (r) = {corr_india:.2f}", 
             fontsize=12, color='red')

    plt.tight_layout()
    plt.show()

    # Print summary
    print(f"📊 Pearson Correlation (r): {corr_india:.3f}")
    if corr_india > 0:
        print("🔺 Positive correlation → AQI rising with year (air quality worsening in India).")
    elif corr_india < 0:
        print("🟢 Negative correlation → AQI dropping with year (air quality improving in India).")
    else:
        print("⚪ No clear correlation → AQI stable over years in India.")
