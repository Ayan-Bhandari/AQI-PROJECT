import pandas as pd
from scipy.stats import spearmanr

# Load dataset
df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# Compute mean AQI for each country using WHO Country Name
country_mean = df.groupby("WHO Country Name")["AQI"].mean().reset_index()

# Compute ranks (1 = cleanest, lowest AQI)
country_mean["Rank"] = country_mean["AQI"].rank(method="dense")

# Spearman Rank Correlation between AQI and Rank
corr, p_value = spearmanr(country_mean["AQI"], country_mean["Rank"])

print("Spearman Rank Correlation:", round(corr, 3))
print("p-value:", p_value)

# Interpretation
if abs(corr) > 0.7:
    print("Strong rank-based relationship between AQI and global ranking.")
elif abs(corr) > 0.4:
    print("Moderate relationship between AQI and ranking.")
else:
    print("Weak relationship → ranking may depend on other factors too.")
