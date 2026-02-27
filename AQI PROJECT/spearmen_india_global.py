import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

# Load AQI ranking data
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\average_AQI_ranking.xlsx")

# Rank all countries globally by AQI
df["AQI Rank"] = df["Average AQI"].rank(ascending=True)

# Spearman correlation for global set
corr_global, p_value_global = spearmanr(df["Average AQI"], df["AQI Rank"])

print("🌍 Spearman Rank Correlation (India vs Global):", round(corr_global, 2))
print("P-Value:", round(p_value_global, 4))

# --- Visualization ---
colors = ['orange' if country == 'India' else 'skyblue' for country in df["WHO Country Name"]]

plt.figure(figsize=(11,6))
plt.bar(df["WHO Country Name"], df["AQI Rank"], color=colors, edgecolor='black')
plt.title("India vs Global: AQI Rank Comparison", fontsize=15, fontweight='bold')
plt.xlabel("Countries", fontsize=12)
plt.ylabel("AQI Rank (Lower = Cleaner Air)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
