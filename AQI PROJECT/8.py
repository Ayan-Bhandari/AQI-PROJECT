import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Load and prepare data
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\data_with_AQI.xlsx")
df_india = df[df['WHO Country Name'] == 'India']
df_india = df_india.dropna(subset=['Measurement Year', 'AQI'])
df_trend = df_india.groupby('Measurement Year')['AQI'].mean().reset_index()

# Correlation and regression
correlation = df_trend['Measurement Year'].corr(df_trend['AQI'])
slope, intercept, r_value, p_value, std_err = linregress(df_trend['Measurement Year'], df_trend['AQI'])
line = slope * df_trend['Measurement Year'] + intercept

# Plot
plt.figure(figsize=(12,6))
plt.scatter(df_trend['Measurement Year'], df_trend['AQI'], color='orange', s=100, label='India AQI Data')
plt.plot(df_trend['Measurement Year'], df_trend['AQI'], color='orange', linewidth=2, alpha=0.7)
plt.plot(df_trend['Measurement Year'], line, color='blue', linestyle='--', label=f'Trendline (R² = {r_value**2:.2f})')

# Labels and styling
plt.title("India's AQI Trend Over Years with Regression Line", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=13)
plt.ylabel("Average AQI", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Add correlation text
plt.text(df_trend['Measurement Year'].min(), df_trend['AQI'].max(), 
         f"Correlation (r) = {correlation:.2f}", fontsize=11, color='blue')

plt.tight_layout()
plt.savefig("India_AQI_Trendline_Enhanced.png", dpi=300, bbox_inches='tight')
plt.show()

# Interpretation
if correlation > 0:
    print("🔺 Positive correlation → AQI increasing with time (air quality worsening).")
elif correlation < 0:
    print("🟢 Negative correlation → AQI decreasing with time (air quality improving).")
else:
    print("⚪ No correlation → AQI stable over time.")
print("\nRegression Line Equation:")
print(f"AQI = {slope:.4f} × (Year) + {intercept:.4f}")
