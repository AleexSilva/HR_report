# 📊 Absenteeism Analysis with Power BI

This project analyzes absenteeism at work using datasets related to employee attendance, compensation, and reasons for absence. The data is processed in Python and stored in a MySQL database, with the final output visualized in an interactive Power BI dashboard.  
🔗 [View the Power BI Report](https://app.powerbi.com/view?r=eyJrIjoiMTgzMDA2MzItNzBmMS00MzcxLWE5YTktN2VlNjA5MTAzOTY2IiwidCI6IjRjODE4Zjc5LWFiODQtNDU1Mi05YjdjLTJmZTcxNWIwZDBkNSIsImMiOjR9&embedImagePlaceholder=true&pageName=45ba177659d111579ae6)<!-- REPORT LINK HERE -->

---

## Workflow

![Alt Text](https://raw.githubusercontent.com/AleexSilva/HR_report/refs/heads/main/mock-up/HR_Analysis_Workflow.png)

---
## 📑 Table of Contents

- [📂 Project Structure](#-project-structure)
- [📦 Required Libraries](#-required-libraries)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [📄 Files](#-files)

---

## 📂 Project Structure

```plaintext
├── README.md
├── code
│   └── data_import.py
├── data
│   ├── Absenteeism_at_work.csv
│   ├── Reasons.csv
│   └── compensation.csv
├── mock-up
│   └── PBI - Base-Ideas.png
└── sql
    └── query_hr.sql
```

---

## 📦 Required Libraries

- `pandas`
- `mysql-connector-python`
- `python-decouple`

Install them using:

```bash
pip install pandas mysql-connector-python python-decouple
```

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/absenteeism-analysis.git
   cd absenteeism-analysis
   ```

2. Create a `.env` file in the root directory with your MySQL credentials:

   ```env
   user=your_username
   password=your_password
   host=your_host
   database=your_database
   ```

3. Ensure MySQL is running and accessible.

---

## 🚀 Usage

1. Run the `data_import.py` script to populate the MySQL database with data from the CSV files:

   ```bash
   python code/data_import.py
   ```

2. Use the `sql/query_hr.sql` script to explore or prepare additional queries.

3. Open the Power BI report to visualize insights.

---

## 📄 Files

- `code/data_import.py`: Loads CSV data into a MySQL database and handles data transformation.
- `data/Absenteeism_at_work.csv`: Main dataset with employee absenteeism records.
- `data/compensation.csv`: Dataset containing compensation values.
- `data/Reasons.csv`: Mapping of reasons for absence.
- `mock-up/PBI - Base-Ideas.png`: Initial design concept for the Power BI dashboard.
- `sql/query_hr.sql`: SQL query for HR-related data exploration.

---
