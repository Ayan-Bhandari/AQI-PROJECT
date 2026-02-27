import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# Drop missing
df = df[['PM10 (μg/m3)', 'AQI']].dropna()

# --- Plot ---
plt.figure(figsize=(10,6))
sns.set_theme(style="whitegrid")

plt.scatter(df['PM10 (μg/m3)'], df['AQI'], 
            alpha=0.35, s=45, color='#007acc', edgecolors='none')

plt.title("Scatter Plot: AQI vs PM10 Concentration", 
          fontsize=15, fontweight='bold')
plt.xlabel("PM10 Concentration (μg/m³)", fontsize=12)
plt.ylabel("Air Quality Index (AQI)", fontsize=12)

plt.tight_layout()
plt.show()
