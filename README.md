# 📊 Data Analysis and Plotting using Python

A data analysis project that explores **GDP per capita trends** across 60+ countries from **1970 to 2020**, using Python, Pandas, and Matplotlib. GDP and population datasets are combined to compute and visualise per-capita economic growth in a structured 3×2 subplot dashboard.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Output](#-output)
- [Countries Covered](#-countries-covered)
- [Data Sources](#-data-sources)
- [Author](#-author)

---

## 🔍 Overview

This project answers a key economic question:

> *How has GDP per capita changed across different countries between 1970 and 2020?*

It merges two real-world datasets — world GDP and world population — computes GDP per capita for each decade, and plots the results across six grouped subplots for easy comparison.

---

## ✨ Features

- 📥 **Loads real-world CSV data** — World Bank-style GDP data and world population figures
- 🔗 **Merges two datasets** — GDP and population joined by country name
- 🧮 **Computes GDP per capita** for each country across 7 time points (1970–2020)
- 📈 **6-panel matplotlib dashboard** — countries grouped alphabetically across a 3×2 subplot grid
- 🌍 **60+ countries covered** spanning all continents
- 📌 **Marker-annotated line charts** for clear trend visibility

---

## 📁 Project Structure

```
Data-Analysis-and-Plotting-using-Python/
│
├── dataanalysisandplotting.py    # Main analysis and plotting script
├── new_gdp.csv                   # GDP data by country (1960–2020)
├── new_world_population.csv      # World population data by country
└── README.md                     # Project documentation
```

---

## 🛠 Prerequisites

Make sure you have **Python 3.x** installed, then install the required libraries:

| Library      | Purpose                              |
|--------------|--------------------------------------|
| `pandas`     | Data loading, indexing, computation  |
| `matplotlib` | Plotting the GDP per capita charts   |
| `numpy`      | Numerical support                    |

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/frmahmud/Data-Analysis-and-Plotting-using-Python.git
   cd Data-Analysis-and-Plotting-using-Python
   ```

2. **Install dependencies**
   ```bash
   pip install pandas matplotlib numpy
   ```

---

## ▶️ How to Run

```bash
python dataanalysisandplotting.py
```

A matplotlib window will open displaying a **3×2 grid of GDP per capita line charts**, one panel per country group.

> **Note:** Both CSV files (`new_gdp.csv` and `new_world_population.csv`) must be in the same directory as the script.

---

## 📊 Output

The script generates a **3×2 subplot figure** where each panel shows GDP per capita (USD) on the Y-axis and year on the X-axis, for a group of ~10 countries. Each line represents one country, with circular markers at each data point (1970, 1980, 1990, 2000, 2010, 2015, 2020).

| Panel      | Countries    |
|------------|--------------|
| Top Left   | Group 1 (A–B) |
| Top Right  | Group 2 (C–F) |
| Mid Left   | Group 3 (F–I) |
| Mid Right  | Group 4 (J–N) |
| Bot Left   | Group 5 (N–S) |
| Bot Right  | Group 6 (S–Z) |

---

## 🌍 Countries Covered

Afghanistan, Argentina, Armenia, Australia, Azerbaijan, Bahrain, Bangladesh, Belgium, Brazil, Canada, Chile, China, Colombia, Cuba, Cayman Islands, Denmark, Finland, France, Greece, Haiti, Iceland, India, Iraq, Ireland, Israel, Italy, Japan, Kazakhstan, Kenya, Lebanon, Libya, Madagascar, Malaysia, Mexico, Netherlands, Nigeria, Norway, Oman, Pakistan, Panama, Philippines, Poland, Romania, Rwanda, Saudi Arabia, Singapore, Spain, Sri Lanka, Sudan, Sweden, Thailand, Uganda, Ukraine, United Arab Emirates, United Kingdom, United States, Vietnam, Zimbabwe — plus **World** aggregate in each group.

---

## 📂 Data Sources

| File                        | Description                                      |
|-----------------------------|--------------------------------------------------|
| `new_gdp.csv`               | GDP (current USD) by country, 1960–2020          |
| `new_world_population.csv`  | Population by country, 1970–2022                 |

Both datasets follow a **World Bank** style format, indexed by country name.

---

## 👤 Author

**Firoz Mahmud**  
📧 fmahmud.ruet@gmail.com  
🌐 [frmahmud.github.io](https://frmahmud.github.io)

---

*Created: 2024*
