# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load dataset
# df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# # Select relevant columns and drop missing values
# df = df[['PM2.5 (μg/m3)', 'AQI']].dropna()

# # --- Plot Styling ---
# plt.figure(figsize=(9,6))
# sns.set_theme(style="whitegrid")

# # Scatter Plot Only
# plt.scatter(df['PM2.5 (μg/m3)'], df['AQI'], 
#             alpha=0.45, s=45, color='#007acc', edgecolors='none')

# # Labels & Title
# plt.title("Scatter Plot: AQI vs PM2.5 Concentration", 
#           fontsize=15, fontweight='bold', color='#222', pad=15)
# plt.xlabel("PM2.5 Concentration (μg/m³)", fontsize=12)
# plt.ylabel("Air Quality Index (AQI)", fontsize=12)

# # Optional axis scaling
# # plt.xlim(0, 100)
# # plt.ylim(0, 200)

# plt.grid(True, linestyle='--', alpha=0.3)
# plt.tight_layout()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# Select relevant columns and drop missing values
df = df[['PM2.5 (μg/m3)', 'AQI']].dropna()

# ---- Regression Calculation ----
slope, intercept, r_value, p_value, std_err = linregress(df['PM2.5 (μg/m3)'], df['AQI'])

# Regression equation line
line = slope * df['PM2.5 (μg/m3)'] + intercept

print("\n📌 Regression Line Equation:")
print(f"AQI = {slope:.4f} × PM2.5 + {intercept:.4f}")

print("\n📌 Correlation Coefficient:", round(r_value, 3))
print("📌 p-value:", p_value)

# ---- Scatter Plot ----
plt.figure(figsize=(9,6))
sns.set_theme(style="whitegrid")

plt.scatter(df['PM2.5 (μg/m3)'], df['AQI'], 
            alpha=0.45, s=45, color='#007acc', edgecolors='none')

plt.title("Scatter Plot: AQI vs PM2.5 Concentration", 
          fontsize=15, fontweight='bold', color='#222', pad=15)
plt.xlabel("PM2.5 Concentration (μg/m³)", fontsize=12)
plt.ylabel("Air Quality Index (AQI)", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
