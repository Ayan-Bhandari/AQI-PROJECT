import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\data_with_AQI.xlsx")

df_india = df[df['WHO Country Name'] == 'India']

df_india = df_india.dropna(subset=['Measurement Year', 'AQI'])

df_trend = df_india.groupby('Measurement Year')['AQI'].mean().reset_index()

plt.figure(figsize=(12,6))
plt.plot(df_trend['Measurement Year'], df_trend['AQI'], marker='o', color='orange', linewidth=2.5)

plt.title("India's AQI Trend Over the Years", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=13)
plt.ylabel("Average AQI", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)

for i, val in enumerate(df_trend['AQI']):
    if pd.notna(val) and pd.notna(df_trend['Measurement Year'].iloc[i]):
        plt.text(df_trend['Measurement Year'].iloc[i], val + 1, f'{val:.1f}', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig("India_AQI_Trendline_Fixed.png", dpi=300, bbox_inches='tight')
plt.show()
