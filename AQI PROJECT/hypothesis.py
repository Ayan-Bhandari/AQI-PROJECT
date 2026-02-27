import pandas as pd
from scipy.stats import ttest_1samp

df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")

# Drop missing values
df = df[['AQI', 'WHO Country Name']].dropna()

# India AQI sample
india = df[df['WHO Country Name'] == 'India']['AQI']

# Global mean AQI
global_mean = df['AQI'].mean()

# One-sample t-test (right tailed)
t_stat, p_value_two_tailed = ttest_1samp(india, global_mean)

# Convert to one-tailed
p_value = p_value_two_tailed / 2

print("India mean AQI:", india.mean())
print("Global mean AQI:", global_mean)
print("t statistic:", t_stat)
print("p-value (one-tailed):", p_value)
