"""
Day 25 Master File: CSV Data & The Pandas Library
------------------------------------------------
Topics Covered:
1. Pure Python CSV reading vs. `csv` module vs. `pandas`
2. Pandas Data Structures: Series (columns) and DataFrames (tables)
3. Extracting rows, columns, and specific values
4. Data filtering and conditional selections
5. Constructing DataFrames from scratch and exporting to CSV
"""

import csv
import pandas as pd

# ==========================================
# 1. TRADITIONAL CSV HANDLING vs PANDAS
# ==========================================

print("--- 1. Traditional CSV Reading ---")

# Standard Python approach (verbose, manual stripping)
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print("Raw readlines output:", data[:2])  # Shows raw strings with \n

# Built-in csv module approach
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print("Extracted Temps via CSV module:", temperatures)

# Pandas approach (One line, auto-headers, typed data)
df = pd.read_csv("weather_data.csv")
print("\nPandas DataFrame:")
print(df)


# ==========================================
# 2. DATAFRAMES & SERIES BASICS
# ==========================================

print("\n--- 2. DataFrames vs Series ---")

# Type checking
print("Type of full object:", type(df))       # pandas.core.frame.DataFrame
print("Type of 'temp' column:", type(df["temp"])) # pandas.core.series.Series

# Two ways to access columns
print("\nAccess as dictionary key:", df["temp"].tolist())
print("Access as object attribute:", df.temp.tolist())

# Summary Math Methods on Series
print("Mean Temperature:", df["temp"].mean())
print("Max Temperature:", df["temp"].max())


# ==========================================
# 3. ROW SELECTION & FILTERING
# ==========================================

print("\n--- 3. Row Selection & Data Filtering ---")

# Get row where day is Monday
monday_row = df[df.day == "Monday"]
print("Monday Row:\n", monday_row)

# Get row with maximum temperature
hottest_day = df[df.temp == df.temp.max()]
print("\nHottest Day of the Week:\n", hottest_day)

# Accessing specific cell values & conversions
monday_temp_c = monday_row.temp.item()
monday_temp_f = (monday_temp_c * 9 / 5) + 32
print(f"\nMonday Temp in Fahrenheit: {monday_temp_f}°F")


# ==========================================
# 4. CREATING DATAFRAMES FROM SCRATCH & EXPORTING
# ==========================================

print("\n--- 4. Creating & Exporting CSVs ---")

# Dictionary to DataFrame
student_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_df = pd.DataFrame(student_dict)
print("Newly Created DataFrame:")
print(student_df)

# Export to CSV (index=False prevents extra index column)
student_df.to_csv("student_scores.csv", index=False)
print("Successfully exported 'student_scores.csv'!")


# ==========================================
# 5. SQUIRREL DATA ANALYSIS (DAY 25 MINI-PROJECT RECAP)
# ==========================================

print("\n--- 5. Central Park Squirrel Analysis Example ---")

"""
Given a large dataset (e.g., 2018 Central Park Squirrel Census),
how to extract primary fur colors and count totals into a new CSV.
"""
try:
    squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    
    gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
    cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
    black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

    squirrel_count_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_count, cinnamon_count, black_count]
    }

    squirrel_count_df = pd.DataFrame(squirrel_count_dict)
    squirrel_count_df.to_csv("squirrel_count.csv", index=False)
    print("Squirrel Analysis Table:")
    print(squirrel_count_df)

except FileNotFoundError:
    print("Squirrel CSV dataset not found in directory — skipping analysis snippet.")
