import pandas as pd
import matplotlib.pyplot as plt

# ✅ Load ranked AQI data
file_path = r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\country_AQI_ranking.xlsx"
df = pd.read_excel(file_path)

# ✅ Sort by rank (cleanest → most polluted)
df = df.sort_values(by='Rank (Cleanest→Most Polluted)')

# ✅ Highlight India
colors = ['orange' if country == 'India' else 'skyblue' for country in df['WHO Country Name']]

# ✅ Plot
plt.figure(figsize=(14, 7))
bars = plt.bar(df['WHO Country Name'], df['Mean_AQI'], color=colors)

# ✅ Labels and title
plt.xlabel("Country", fontsize=12)
plt.ylabel("Mean AQI", fontsize=12)
plt.title("🌍 Global AQI Ranking (India Highlighted)", fontsize=16, fontweight='bold')

# ✅ Show rank numbers above bars
for i, (country, rank, aqi) in enumerate(zip(df['WHO Country Name'], df['Rank (Cleanest→Most Polluted)'], df['Mean_AQI'])):
    plt.text(i, aqi + 1, f"{rank}", ha='center', fontsize=10, fontweight='bold')

# ✅ Rotate labels and add grid
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# ✅ Display plot
plt.show()
