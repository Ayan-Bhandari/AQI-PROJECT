import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\selected_countries_AQI.xlsx")

# Keep only relevant columns
pollutant_cols = ['PM2.5 (μg/m3)', 'PM10 (μg/m3)', 'NO2 (μg/m3)', 'AQI']
df = df[pollutant_cols].dropna()

# Calculate correlation with AQI
corr_values = df.corr()['AQI'].drop('AQI')

# Find pollutant most responsible for AQI variation
most_responsible = corr_values.idxmax()
corr_value = corr_values.max()

print(f"🌍 Most responsible pollutant: {most_responsible}")
print(f"📈 Correlation with AQI: {corr_value:.2f}")

# --- 🎨 Plot (Modern Style) ---
plt.figure(figsize=(9,6))
sns.set_theme(style="whitegrid")

sns.regplot(
    x=df[most_responsible], 
    y=df['AQI'], 
    scatter_kws={'alpha':0.6, 's':60, 'color':'#1f77b4'},  # soft blue dots
    line_kws={'color':'#ff4b4b', 'lw':2.5}  # bold red trendline
)

plt.title(f"AQI vs {most_responsible}\nCorrelation = {corr_value:.2f}",
          fontsize=15, fontweight='bold', color='#333333', pad=15)
plt.xlabel(most_responsible, fontsize=12)
plt.ylabel("Air Quality Index (AQI)", fontsize=12)

# Style tweaks
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()

# Save and show
plt.savefig("Most_Responsible_Pollutant_AQI.png", dpi=300, bbox_inches='tight')
plt.show()

# --- 🧠 Interpretation ---
if corr_value > 0.7:
    print("🔺 Strong positive correlation → AQI rises sharply with increase in pollutant levels.")
elif 0.4 < corr_value <= 0.7:
    print("🟠 Moderate correlation → AQI moderately affected by pollutant levels.")
else:
    print("🟢 Weak correlation → AQI weakly influenced by this pollutant.")
