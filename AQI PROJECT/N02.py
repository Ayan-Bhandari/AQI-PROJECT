# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.stats import linregress

# # Load dataset
# df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# # Drop missing values
# df = df[['NO2 (μg/m3)', 'AQI']].dropna()

# # Filter only NO2 range 0–50 for cleaner plot
# df_filtered = df[df['NO2 (μg/m3)'] <= 50]

# # Calculate correlation and regression on filtered data
# corr_value = df_filtered['NO2 (μg/m3)'].corr(df_filtered['AQI'])
# slope, intercept, r_value, p_value, std_err = linregress(df_filtered['NO2 (μg/m3)'], df_filtered['AQI'])
# line = slope * df_filtered['NO2 (μg/m3)'] + intercept

# # --- Plot Styling ---
# plt.figure(figsize=(9,6))
# sns.set_theme(style="whitegrid")

# # Scatter points
# plt.scatter(df_filtered['NO2 (μg/m3)'], df_filtered['AQI'], 
#             alpha=0.35, s=45, color='#007acc', edgecolors='none', label='Data points')

# # Regression line
# plt.plot(df_filtered['NO2 (μg/m3)'], line, color='#d62828', lw=2.5, label='Regression line')

# # Title & labels
# plt.title(f"AQI vs NO₂ Concentration (0–50 µg/m³)\nCorrelation = {corr_value:.2f}", 
#           fontsize=15, fontweight='bold', color='#222', pad=15)
# plt.xlabel("NO₂ Concentration (μg/m³)", fontsize=12)
# plt.ylabel("Air Quality Index (AQI)", fontsize=12)

# # Formatting
# plt.xlim(0, 50)   # <<< ONLY CHANGE NEEDED FOR SCALING
# plt.legend(frameon=False, fontsize=11)
# plt.grid(True, linestyle='--', alpha=0.3)
# plt.tight_layout()
# plt.show()

# # --- Interpretation ---
# print(f"📊 Correlation between NO₂ (0–50 µg/m³) and AQI = {corr_value:.2f}")
# if corr_value > 0.7:
#     print("🔺 Strong positive correlation → AQI rises significantly with NO₂ levels.")
# elif 0.4 < corr_value <= 0.7:
#     print("🟠 Moderate correlation → AQI moderately influenced by NO₂.")
# else:
#     print("🟢 Weak correlation → AQI weakly affected by NO₂.")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# Use clipped values (keeps graph visible)
df['NO2_clipped'] = df['NO2 (μg/m3)'].clip(upper=50)

# Drop missing
df_clean = df[['NO2_clipped', 'AQI']].dropna()

# Correlation & regression
corr_value = df_clean['NO2_clipped'].corr(df_clean['AQI'])
slope, intercept, r_value, p_value, std_err = linregress(df_clean['NO2_clipped'], df_clean['AQI'])
line = slope * df_clean['NO2_clipped'] + intercept

# Plot
plt.figure(figsize=(9,6))
sns.set_theme(style="whitegrid")

plt.scatter(df_clean['NO2_clipped'], df_clean['AQI'],
            alpha=0.35, s=45, color='#007acc', edgecolors='none', label='Data Points')

plt.plot(df_clean['NO2_clipped'], line, color='#d62828', lw=2.5, label='Regression line')

plt.title(f"AQI vs NO₂ Concentration (Scaled 0–50 µg/m³)\nCorrelation = {corr_value:.2f}",
          fontsize=15, fontweight='bold')
plt.xlabel("NO₂ Concentration (µg/m³) — Scaled", fontsize=12)
plt.ylabel("Air Quality Index (AQI)", fontsize=12)

plt.xlim(0, 50)
plt.legend(frameon=False, fontsize=11)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
