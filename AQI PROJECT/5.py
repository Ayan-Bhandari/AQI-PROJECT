import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\BRICS_AQI_Data.xlsx")   # Use your correct file name

country_col = "WHO Country Name"

brics_countries = ["India", "Brazil", "Russia", "China", "South Africa"]

df_brics = df[df[country_col].isin(brics_countries)]

df_brics = df_brics.dropna(subset=["AQI"])

df_brics = df_brics.sort_values(by="AQI")

plt.figure(figsize=(8, 5))
bars = plt.bar(df_brics[country_col], df_brics["AQI"], color="skyblue")

for bar, country in zip(bars, df_brics[country_col]):
    if country == "India":
        bar.set_color("orange")

plt.title("BRICS Countries: AQI Comparison (India Highlighted)", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Average AQI")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
