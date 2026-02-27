import pandas as pd
import matplotlib.pyplot as plt

df_clean = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\top10_cleanest_AQI_countries.xlsx")

df_clean = df_clean.sort_values(by='Average AQI', ascending=True)

plt.figure(figsize=(10,6))
plt.barh(df_clean['WHO Country Name'], df_clean['Average AQI'], color='lightgreen')

plt.title('Top 10 Cleanest Countries (Lowest Average AQI)', fontsize=14, fontweight='bold')
plt.xlabel('Average AQI', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.gca().invert_yaxis()  # Cleanest (lowest AQI) at the top

for index, value in enumerate(df_clean['Average AQI']):
    plt.text(value + 1, index, f"{value:.1f}", va='center', fontsize=10)

plt.tight_layout()
plt.savefig("Top_10_Cleanest_Countries.png", dpi=300, bbox_inches='tight')
plt.show()
