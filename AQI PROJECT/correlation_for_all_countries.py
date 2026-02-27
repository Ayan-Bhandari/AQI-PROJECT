import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Load data
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\data_with_AQI.xlsx")

# Remove missing values
df = df.dropna(subset=['Measurement Year', 'AQI'])

# Group by year to get average AQI across all countries
df_global = df.groupby('Measurement Year')['AQI'].mean().reset_index()

# Calculate correlation and regression line
correlation = df_global['Measurement Year'].corr(df_global['AQI'])
slope, intercept, r_value, p_value, std_err = linregress(df_global['Measurement Year'], df_global['AQI'])
line = slope * df_global['Measurement Year'] + intercept

# Plot
plt.figure(figsize=(12,6))
plt.scatter(df_global['Measurement Year'], df_global['AQI'], color='green', s=100, label='Global Avg AQI')
plt.plot(df_global['Measurement Year'], line, color='blue', linestyle='--', label=f'Trendline (R²={r_value**2:.2f})')

plt.title("🌍 Global AQI Trend Over Years", fontsize=16, fontweight='bold')
plt.xlabel("Measurement Year", fontsize=13)
plt.ylabel("Average AQI", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.text(df_global['Measurement Year'].min(), df_global['AQI'].max(), 
         f"Correlation (r) = {correlation:.2f}", fontsize=11, color='blue')

plt.tight_layout()
plt.show()

# Interpretation
if correlation > 0:
    print("🔺 Positive correlation → AQI rising with year (global air quality worsening).")
elif correlation < 0:
    print("🟢 Negative correlation → AQI dropping with year (global air quality improving).")
else:
    print("⚪ No clear correlation → AQI stable globally.")
