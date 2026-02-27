import pandas as pd

# ✅ Load your AQI summary file (from previous step)
file_path = r"C:\Users\DELL\OneDrive\Desktop\country_AQI_summary.xlsx"
df = pd.read_excel(file_path)

# ✅ Rank countries — lower AQI means cleaner air
df['Rank (Cleanest→Most Polluted)'] = df['Mean_AQI'].rank(method='dense', ascending=True).astype(int)

# ✅ Sort by rank for clarity
df_sorted = df.sort_values(by='Rank (Cleanest→Most Polluted)')

# ✅ Display
print("🏆 Country AQI Rankings:")
print(df_sorted)

# ✅ Save ranked data to Excel
output_path = r"C:\Users\DELL\OneDrive\Desktop\country_AQI_ranking.xlsx"
df_sorted.to_excel(output_path, index=False)
print(f"\n✅ Ranked data saved at: {output_path}")
