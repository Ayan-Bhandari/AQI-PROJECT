import pandas as pd

# ✅ Load your dataset

df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\selected_countries_AQI.xlsx")

# ✅ Keep only necessary columns (adjust if needed)
df = df[['WHO Country Name', 'AQI']]

# ✅ Group by country and calculate descriptive statistics
aqi_stats = df.groupby('WHO Country Name')['AQI'].agg(
    Mean_AQI='mean',
    Min_AQI='min',
    Max_AQI='max',
    Std_Deviation='std'
).reset_index()

# ✅ Round for readability
aqi_stats = aqi_stats.round(2)

# ✅ Display the table
print("📊 AQI Descriptive Statistics by Country:")
print(aqi_stats)

# ✅ Optional: Save to Excel
output_path = r"C:\Users\DELL\OneDrive\Desktop\country_AQI_summary.xlsx"
aqi_stats.to_excel(output_path, index=False)
print(f"\n✅ Summary saved at: {output_path}")
