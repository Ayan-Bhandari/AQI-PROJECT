import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\average_AQI_ranking.xlsx")

# Drop rows with missing AQI values
df = df.dropna(subset=["Average AQI"])

# Sort by AQI (lower = cleaner)
df_sorted = df.sort_values(by="Average AQI", ascending=True)

# Select Top 5 cleanest and Bottom 5 most polluted
top5 = df_sorted.head(5)
bottom5 = df_sorted.tail(5)

# Combine both for visualization
combined = pd.concat([top5, bottom5])

# Create bar chart
plt.figure(figsize=(10,6))
bars = plt.bar(combined["WHO Country Name"], combined["Average AQI"], color=['skyblue']*5 + ['salmon']*5)

# Add title and labels
plt.title("Top 5 Cleanest vs Bottom 5 Most Polluted Countries (Average AQI)", fontsize=14, fontweight='bold')
plt.xlabel("Country", fontsize=12)
plt.ylabel("Average AQI", fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add AQI values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig("Top5_vs_Bottom5_AQI.png", dpi=300, bbox_inches='tight')
plt.show()
