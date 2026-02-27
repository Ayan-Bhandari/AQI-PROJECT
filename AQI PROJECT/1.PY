import pandas as pd

file_path = r"C:\Users\DELL\OneDrive\Desktop\data.xlsx"
excel_file = pd.ExcelFile(file_path)


print("Sheets in your Excel file:")
for name in excel_file.sheet_names:
    print(f"→ '{name}'")
df = pd.read_excel(file_path, sheet_name='AAP_2022_city_v9 ')
import numpy as np

file_path = r"C:\Users\DELL\OneDrive\Desktop\data.xlsx"

df = pd.read_excel(file_path, sheet_name='AAP_2022_city_v9')  # <- adjust this name if needed

print(df.head())

pm25_bp = [
    (0.0, 12.0, 0, 50),
    (12.1, 35.4, 51, 100),
    (35.5, 55.4, 101, 150),
    (55.5, 150.4, 151, 200),
    (150.5, 250.4, 201, 300),
    (250.5, 500.4, 301, 500)
]

pm10_bp = [
    (0, 54, 0, 50),
    (55, 154, 51, 100),
    (155, 254, 101, 150),
    (255, 354, 151, 200),
    (355, 424, 201, 300),
    (425, 604, 301, 500)
]

def get_aqi(conc, breakpoints):
    if pd.isna(conc):
        return np.nan
    for Clow, Chigh, Ilow, Ihigh in breakpoints:
        if Clow <= conc <= Chigh:
            return ((Ihigh - Ilow) / (Chigh - Clow)) * (conc - Clow) + Ilow
    return np.nan

def calculate_aqi(row):
    aqi_pm25 = get_aqi(row.get("PM2.5 (μg/m3)"), pm25_bp)
    aqi_pm10 = get_aqi(row.get("PM10 (μg/m3)"), pm10_bp)
    if not np.isnan(aqi_pm25) and not np.isnan(aqi_pm10):
        return max(aqi_pm25, aqi_pm10)
    elif not np.isnan(aqi_pm25):
        return aqi_pm25
    elif not np.isnan(aqi_pm10):
        return aqi_pm10
    else:
        return np.nan

df["AQI"] = df.apply(calculate_aqi, axis=1)

def aqi_category(aqi):
    if pd.isna(aqi):
        return "No Data"
    elif aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

df["AQI Category"] = df["AQI"].apply(aqi_category)

output_path = r"C:\Users\DELL\OneDrive\Desktop\data_with_AQI.xlsx"
df.to_excel(output_path, index=False)

print("✅ AQI column added successfully!")
print("📁 File saved at:", output_path)
