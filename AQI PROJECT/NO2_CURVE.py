# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")
# df = df[['NO2 (μg/m3)', 'AQI']].dropna()

# # Sort values for smooth curve
# x = df['NO2 (μg/m3)']
# y = df['AQI']
# poly = np.poly1d(np.polyfit(x, y, 3))
# xp = np.linspace(min(x), max(x), 300)

# plt.figure(figsize=(10,6))
# sns.scatterplot(x=x, y=y, alpha=0.4, s=40)

# plt.plot(xp, poly(xp), color='red', linewidth=2.5, label='Polynomial Fit (Degree 3)')
# plt.title("Curvilinear Relationship: AQI vs NO₂", fontsize=15)
# plt.xlabel("NO₂ (μg/m³)")
# plt.ylabel("Air Quality Index (AQI)")
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.3)
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\DELL\OneDrive\Desktop\ALL AQI EXCEL\selected_countries_AQI.xlsx")
df = df[['NO2 (μg/m3)', 'AQI']].dropna()

# Sort values for smooth curve
x = df['NO2 (μg/m3)']
y = df['AQI']

# Polynomial Fit (Degree 3)
coeffs = np.polyfit(x, y, 3)
poly = np.poly1d(coeffs)
xp = np.linspace(min(x), max(x), 300)

# Print polynomial equation
print("📌 Cubic Regression Equation (Degree 3):")
print(poly)

# Graph
plt.figure(figsize=(10,6))
sns.scatterplot(x=x, y=y, alpha=0.4, s=40)
plt.plot(xp, poly(xp), color='red', linewidth=2.5, label='Polynomial Fit (Degree 3)')
plt.title("Curvilinear Relationship: AQI vs NO₂", fontsize=15)
plt.xlabel("NO₂ (μg/m³)")
plt.ylabel("Air Quality Index (AQI)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()
