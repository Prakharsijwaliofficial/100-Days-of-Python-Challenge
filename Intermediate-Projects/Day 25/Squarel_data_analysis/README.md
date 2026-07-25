# 🐿️ Central Park Squirrel Data Analysis

A data processing script that analyzes real-world observations from the **2018 Central Park Squirrel Census** using **Pandas**. The script filters raw census records, extracts primary fur color populations, and generates a condensed summary CSV report.

---

## 📌 Features

* **Data Parsing:** Reads and processes thousands of observational records from raw CSV datasets.
* **Boolean Masking:** Uses Pandas conditional logic to filter rows based on primary fur colors (`Gray`, `Cinnamon`, `Black`).
* **Aggregation:** Calculates exact count totals for each primary fur color category.
* **Automated CSV Export:** Packages the extracted counts into a structured DataFrame and exports `squirrel_count.csv`.

---

## 📁 Folder Structure

```text
Squarel_data_analysis/
├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260724.csv  # Raw Census Dataset
├── main.py                                                         # Data processing script
└── squirrel_count.csv                                             # Generated summary output
