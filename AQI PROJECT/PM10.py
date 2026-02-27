# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.stats import linregress

# # Load dataset
# df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# # Drop missing values
# df = df[['PM10 (μg/m3)', 'AQI']].dropna()

# # Calculate correlation and regression
# corr_value = df['PM10 (μg/m3)'].corr(df['AQI'])
# slope, intercept, r_value, p_value, std_err = linregress(df['PM10 (μg/m3)'], df['AQI'])
# line = slope * df['PM10 (μg/m3)'] + intercept

# # --- 🎨 Plot Styling ---
# plt.figure(figsize=(9,6))
# sns.set_theme(style="whitegrid")

# # Scatter points (transparent & small)
# plt.scatter(df['PM10 (μg/m3)'], df['AQI'], 
#             alpha=0.35, s=45, color='#007acc', edgecolors='none', label='Data points')

# # Trendline
# plt.plot(df['PM10 (μg/m3)'], line, color='#d62828', lw=2.5, label='Regression line')

# # Title & labels
# plt.title(f"AQI vs PM10 Concentration\nCorrelation = {corr_value:.2f}", 
#           fontsize=15, fontweight='bold', color='#222', pad=15)
# plt.xlabel("PM10 Concentration (μg/m³)", fontsize=12)
# plt.ylabel("Air Quality Index (AQI)", fontsize=12)

# # Formatting
# plt.legend(frameon=False, fontsize=11)
# plt.grid(True, linestyle='--', alpha=0.3)
# plt.tight_layout()
# plt.savefig("AQI_vs_PM10_clean.png", dpi=300, bbox_inches='tight')
# plt.show()

# # --- Interpretation ---
# print(f"📊 Correlation between PM10 and AQI = {corr_value:.2f}")
# if corr_value > 0.7:
#     print("🔺 Strong positive correlation → AQI rises significantly with PM10 levels.")
# elif 0.4 < corr_value <= 0.7:
#     print("🟠 Moderate correlation → AQI moderately influenced by PM10.")
# else:
#     print("🟢 Weak correlation → AQI weakly affected by PM10.")


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.stats import linregress

# # Load dataset
# df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# # Drop missing values
# df = df[['PM10 (μg/m3)', 'AQI']].dropna()

# # Clip PM10 values so graph remains visible
# df['PM10_clipped'] = df['PM10 (μg/m3)'].clip(upper=50)

# # Correlation & regression using clipped values
# corr_value = df['PM10_clipped'].corr(df['AQI'])
# slope, intercept, r_value, p_value, std_err = linregress(df['PM10_clipped'], df['AQI'])
# line = slope * df['PM10_clipped'] + intercept

# # --- 🎨 Plot Styling ---
# plt.figure(figsize=(9,6))
# sns.set_theme(style="whitegrid")

# # Scatter points
# plt.scatter(df['PM10_clipped'], df['AQI'], 
#             alpha=0.35, s=45, color='#007acc', edgecolors='none', label='Data points')

# # Regression line
# plt.plot(df['PM10_clipped'], line, color='#d62828', lw=2.5, label='Regression line')

# # Labels & Title
# plt.title(f"AQI vs PM10 Concentration (0–50 µg/m³)\nCorrelation = {corr_value:.2f}", 
#           fontsize=15, fontweight='bold')
# plt.xlabel("PM10 Concentration (μg/m³) — Scaled", fontsize=12)
# plt.ylabel("Air Quality Index (AQI)", fontsize=12)

# # Scale X-axis 0–50
# plt.xlim(0, 50)

# plt.legend(frameon=False, fontsize=11)
# plt.grid(True, linestyle='--', alpha=0.3)
# plt.tight_layout()
# plt.show()

# # --- Interpretation ---
# print(f"📊 Correlation between PM10 (0–50 µg/m³) and AQI = {corr_value:.2f}")
# if corr_value > 0.7:
#     print("🔺 Strong positive correlation → AQI rises significantly with PM10 levels.")
# elif 0.4 < corr_value <= 0.7:
#     print("🟠 Moderate correlation → AQI moderately influenced by PM10.")
# else:
#     print("🟢 Weak correlation → AQI weakly affected by PM10.")



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.stats import linregress

# # Load dataset
# df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# # Drop missing values
# df = df[['PM10 (μg/m3)', 'AQI']].dropna()

# # Clip PM10 values for better visualization
# df['PM10_clipped'] = df['PM10 (μg/m3)'].clip(upper=50)

# # Clip AQI also to 0–100 for cleaner graph
# df['AQI_clipped'] = df['AQI'].clip(upper=100)

# # Correlation & regression using clipped values
# corr_value = df['PM10_clipped'].corr(df['AQI_clipped'])
# slope, intercept, r_value, p_value, std_err = linregress(df['PM10_clipped'], df['AQI_clipped'])
# line = slope * df['PM10_clipped'] + intercept

# # --- 🎨 Plot Styling ---
# plt.figure(figsize=(9,6))
# sns.set_theme(style="whitegrid")

# # Scatter points
# plt.scatter(df['PM10_clipped'], df['AQI_clipped'], 
#             alpha=0.35, s=45, color='#007acc', edgecolors='none', label='Data points')

# # Regression line
# plt.plot(df['PM10_clipped'], line, color='#d62828', lw=2.5, label='Regression line')

# # Title & labels
# plt.title(f"AQI vs PM10 Concentration (Scaled)\nCorrelation = {corr_value:.2f}", 
#           fontsize=15, fontweight='bold')
# plt.xlabel("PM10 Concentration (μg/m³) — (0–50)", fontsize=12)
# plt.ylabel("Air Quality Index (AQI) — (0–100)", fontsize=12)

# # Scale both axes
# plt.xlim(0, 50)
# plt.ylim(0, 100)

# # Formatting
# plt.legend(frameon=False, fontsize=11)
# plt.grid(True, linestyle='--', alpha=0.3)
# plt.tight_layout()
# plt.show()

# # Interpretation
# print(f"📊 Correlation between PM10 (0–50 µg/m³) and AQI (0–100) = {corr_value:.2f}")
# if corr_value > 0.7:
#     print("🔺 Strong positive correlation → AQI rises significantly with PM10 levels.")
# elif 0.4 < corr_value <= 0.7:
#     print("🟠 Moderate correlation → AQI moderately influenced by PM10.")
# else:
#     print("🟢 Weak correlation → AQI weakly affected by PM10.")




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# Drop missing values
df = df[['PM10 (μg/m3)', 'AQI']].dropna()

# Clip values for clean plotting
df['PM10_scaled'] = df['PM10 (μg/m3)'].clip(0, 300)
df['AQI_scaled'] = df['AQI'].clip(0, 300)

# Correlation & regression using scaled values
corr_value = df['PM10_scaled'].corr(df['AQI_scaled'])
slope, intercept, r_value, p_value, std_err = linregress(df['PM10_scaled'], df['AQI_scaled'])
line = slope * df['PM10_scaled'] + intercept

# --- 🎨 Plot Styling ---
plt.figure(figsize=(9,6))
sns.set_theme(style="whitegrid")

# Scatter points
plt.scatter(df['PM10_scaled'], df['AQI_scaled'], 
            alpha=0.35, s=45, color='#007acc', edgecolors='none', label='Data points')

# Regression line
plt.plot(df['PM10_scaled'], line, color='#d62828', lw=2.5, label='Regression line')

# Title & labels
plt.title(f"AQI vs PM10 Concentration (0–300 Scale)\nCorrelation = {corr_value:.2f}", 
          fontsize=15, fontweight='bold')
plt.xlabel("PM10 Concentration (μg/m³)", fontsize=12)
plt.ylabel("Air Quality Index (AQI)", fontsize=12)

# Scale axes as requested
plt.xlim(0, 300)
plt.ylim(0, 300)

# Formatting
plt.legend(frameon=False, fontsize=11)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# --- Interpretation ---
print(f"📊 Correlation between PM10 (0–300 µg/m³) and AQI (0–300) = {corr_value:.2f}")
if corr_value > 0.7:
    print("🔺 Strong positive correlation → AQI rises significantly with PM10 levels.")
elif 0.4 < corr_value <= 0.7:
    print("🟠 Moderate correlation → AQI moderately influenced by PM10.")
else:
    print("🟢 Weak correlation → AQI weakly affected by PM10.")
print("\nRegression Line Equation:")
print(f"AQI = {slope:.4f} × PM10 + {intercept:.4f}")
