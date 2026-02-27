import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# Select needed columns & drop missing values
df = df[['NO2 (μg/m3)', 'AQI']].dropna()

# Sort values so line graph makes sense
df_sorted = df.sort_values(by='NO2 (μg/m3)')

# Plot
plt.figure(figsize=(10,6))
sns.set_theme(style="whitegrid")

plt.scatter(df_sorted['NO2 (μg/m3)'], df_sorted['AQI'],
         color='#1f77b4')

plt.title("Line Graph: AQI vs NO₂ Concentration",
          fontsize=15, fontweight='bold')
plt.xlabel("NO₂ (μg/m³)", fontsize=12)
plt.ylabel("AQI", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
