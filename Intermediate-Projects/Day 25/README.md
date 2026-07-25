# 🚀 Day 25: CSV Data Analysis & The Pandas Library

Welcome to **Day 25** of the **100 Days of Python Challenge**! Today focuses on moving beyond standard text manipulation to working with real-world structured datasets. By mastering the **Pandas** library, we learn how to import, filter, aggregate, analyze, and export tabular data efficiently.

---

## 🛠️ Key Concepts Learned Today

* **Data Reading:** Transitioning from raw Python `open().readlines()` and the built-in `csv` module to high-performance Pandas DataFrames via `pd.read_csv()`.
* **Data Structures:** Understanding the fundamental difference between a **DataFrame** (2D full tabular data structure) and a **Series** (1D single column data structure).
* **Data Selection & Filtering:** Querying specific rows and columns using boolean masking and conditional criteria (e.g., finding maximum values, filtering specific records).
* **Data Construction & Export:** Building DataFrames programmatically using Python dictionaries and exporting summary reports to `.csv` files.
* **GUI Integration:** Combining Pandas data lookups with Python's `turtle` library to build interactive graphical applications.

---

## 📁 Repository Overview

This directory is organized into two main projects along with a master notes script:

```text
Day 25/
├── README.md                                    # Root Documentation
├── main.py                                      # Master reference script covering Day 25 fundamentals
│
├── Squarel_data_analysis/                       # Project 1: Data aggregation & summary report
│   ├── 2018_Central_Park_Squirrel_Census...csv  # Raw NYC census dataset
│   └── main.py                                  # Processing script for fur color counts
│
└── American_State_Game/                         # Project 2: Interactive GUI map game
    ├── 50_states.csv                            # State name coordinates lookup table
    ├── blank_states_img.gif                     # U.S. Map background image
    ├── main.py                                  # Core game loop & Turtle renderer
    └── state_to_learn.py                        # Exporter for missed states review
