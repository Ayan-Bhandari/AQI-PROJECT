# GRAPH FOR AVERAGE AQI OVERALL COMPARING WITH INDIA
import pandas as pd
import matplotlib.pyplot as plt

df_global = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\average_AQI_ranking.xlsx")

df_global = df_global.sort_values(by='Average AQI', ascending=True)

colors = ['orange' if c == 'India' else 'skyblue' for c in df_global['WHO Country Name']]

plt.figure(figsize=(12,6))
plt.bar(df_global['WHO Country Name'], df_global['Average AQI'], color=colors)
plt.axhline(df_global['Average AQI'].mean(), color='red', linestyle='--', label='Global Average AQI')

plt.title('Global AQI Comparison — India Highlighted', fontsize=14, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Average AQI', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend()

plt.tight_layout()
plt.savefig("Global_AQI_Comparison_India.png", dpi=300, bbox_inches='tight')
plt.show()
