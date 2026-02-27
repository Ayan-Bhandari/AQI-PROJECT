import pandas as pd
from scipy.stats import ttest_1samp

# Load raw AQI dataset
df = pd.read_excel(r"C:\\Users\\DELL\\OneDrive\\Desktop\\ALL AQI EXCEL\\selected_countries_AQI.xlsx")

# Extract India's ALL AQI values
india_data = df[df["WHO Country Name"] == "India"]["AQI"].dropna()

# Global mean AQI from ALL COUNTRIES
global_mean = df["AQI"].mean()

# Calculate India sample standard deviation
india_std = india_data.std()

# Perform one-sample t-test
t_stat, p_val_two_tailed = ttest_1samp(india_data, global_mean)

# Convert to one-tailed (because H1: India > Global)
p_val_one_tailed = p_val_two_tailed / 2

# Output
print("Number of India AQI values:", len(india_data))
print("India Mean AQI:", india_data.mean())
print("India Standard Deviation (Sample):", india_std)
print("Global Mean AQI:", global_mean)
print("t-statistic:", t_stat)
print("p-value (one-tailed):", p_val_one_tailed)
