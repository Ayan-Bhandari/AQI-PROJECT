# import pandas as pd
# import matplotlib.pyplot as plt

# df_regional = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\india_regional_comparison.xlsx")

# df_regional = df_regional.sort_values(by='Average AQI', ascending=True)

# colors = ['orange' if c == 'India' else 'skyblue' for c in df_regional['WHO Country Name']]

# plt.figure(figsize=(10,6))
# plt.bar(df_regional['WHO Country Name'], df_regional['Average AQI'], color=colors)

# plt.title('Regional AQI Comparison — India Highlighted', fontsize=14, fontweight='bold')
# plt.xlabel('Country', fontsize=12)
# plt.ylabel('Average AQI', fontsize=12)
# plt.xticks(rotation=45, ha='right')

# for index, value in enumerate(df_regional['Average AQI']):
#     plt.text(index, value + 1, f"{value:.1f}", ha='center', fontsize=9)

# plt.tight_layout()
# plt.savefig("Regional_AQI_Comparison_India.png", dpi=300, bbox_inches='tight')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df_regional = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\india_regional_comparison.xlsx")

# --- Keep ONLY the Asian countries you selected ---
asia_countries = ["India", "China", "Bangladesh", "Indonesia"]
df_regional = df_regional[df_regional["WHO Country Name"].isin(asia_countries)]

# Sort by AQI
df_regional = df_regional.sort_values(by='Average AQI', ascending=True)

# Highlight India
colors = ['orange' if c == 'India' else 'skyblue' for c in df_regional['WHO Country Name']]

# Plot
plt.figure(figsize=(10,6))
plt.bar(df_regional['WHO Country Name'], df_regional['Average AQI'], color=colors)

# Labels
plt.title('Regional AQI Comparison — India Highlighted', fontsize=14, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Average AQI', fontsize=12)
plt.xticks(rotation=0)

# Show values above bars
for index, value in enumerate(df_regional['Average AQI']):
    plt.text(index, value + 1, f"{value:.1f}", ha='center', fontsize=9)

plt.tight_layout()
plt.show()
