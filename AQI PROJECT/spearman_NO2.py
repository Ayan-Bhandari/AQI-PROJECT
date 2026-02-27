import pandas as pd
from scipy.stats import spearmanr

# Load dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# Clean data
df = df[['NO2 (μg/m3)', 'AQI']].dropna()

# Spearman correlation
rho, pval = spearmanr(df['NO2 (μg/m3)'], df['AQI'])

print("Spearman Rank Correlation =", round(rho, 3))
print("p-value =", pval)

if abs(rho) > 0.7:
    print("Strong monotonic relationship")
elif abs(rho) > 0.4:
    print("Moderate monotonic relationship")
else:
    print("Weak monotonic relationship")
