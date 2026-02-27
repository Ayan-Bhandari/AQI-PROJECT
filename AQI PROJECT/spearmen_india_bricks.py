import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

# Load AQI ranking data
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\average_AQI_ranking.xlsx")

# Filter for BRICS countries
brics = ["India", "Brazil", "Russia", "China", "South Africa"]
df_brics = df[df["WHO Country Name"].isin(brics)].copy()

# Rank countries by AQI (lower AQI → cleaner)
df_brics["AQI Rank"] = df_brics["Average AQI"].rank(ascending=True)

# Spearman rank correlation
corr_brics, p_value_brics = spearmanr(df_brics["Average AQI"], df_brics["AQI Rank"])

# Print correlation results
print("🇮🇳 Spearman Rank Correlation (India vs BRICS):", round(corr_brics, 2))
print("P-Value:", round(p_value_brics, 4))

# --- Visualization ---
colors = ['orange' if country == 'India' else 'lightgreen' for country in df_brics["WHO Country Name"]]

plt.figure(figsize=(8,5))
plt.bar(df_brics["WHO Country Name"], df_brics["AQI Rank"], color=colors, edgecolor='black')
plt.title("India vs BRICS: AQI Rank Comparison", fontsize=14, fontweight='bold')
plt.xlabel("BRICS Countries", fontsize=12)
plt.ylabel("AQI Rank (Lower = Cleaner Air)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
