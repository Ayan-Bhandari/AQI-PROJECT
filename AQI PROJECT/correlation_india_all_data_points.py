import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Load your dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\selected_countries_AQI.xlsx")

# Keep only India data
df_india = df[df['WHO Country Name'] == 'India']

# Drop missing values
df_india = df_india.dropna(subset=['Measurement Year', 'AQI'])

# Convert year to numeric (in case it’s stored as text)
df_india['Measurement Year'] = pd.to_numeric(df_india['Measurement Year'], errors='coerce')
df_india = df_india.dropna(subset=['Measurement Year'])

# Compute correlation and regression line
corr_india = df_india['Measurement Year'].corr(df_india['AQI'])
slope, intercept, r_value, p_value, std_err = linregress(df_india['Measurement Year'], df_india['AQI'])
line = slope * df_india['Measurement Year'] + intercept

# Plot all points + trendline
plt.figure(figsize=(12,6))
plt.scatter(df_india['Measurement Year'], df_india['AQI'], 
            alpha=0.5, color='orange', s=50, label='All AQI Data (India)')
plt.plot(df_india['Measurement Year'], line, color='red', linewidth=2, 
         linestyle='--', label=f'Trendline (R²={r_value**2:.2f})')

# Labels & titles
plt.title("India AQI Trend (All Data Points)", fontsize=16, fontweight='bold')
plt.xlabel("Measurement Year", fontsize=13)
plt.ylabel("AQI", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show correlation on graph
plt.text(df_india['Measurement Year'].min(), df_india['AQI'].max(), 
         f"Correlation (r) = {corr_india:.2f}", fontsize=11, color='red')

plt.tight_layout()
plt.show()

# Interpretation in console
if corr_india > 0:
    print("🔺 Positive correlation → AQI increasing over years (air quality worsening).")
elif corr_india < 0:
    print("🟢 Negative correlation → AQI decreasing over years (air quality improving).")
else:
    print("⚪ No clear correlation → AQI stable over time.")
