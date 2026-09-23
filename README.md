# AML Transaction Monitoring Dashboard | Power BI

## 📌 Overview

The **AML Transaction Monitoring Dashboard** is an end-to-end data analytics project designed to analyze banking transactions, identify suspicious activity, assess transaction and customer risk, and present actionable AML monitoring insights through an interactive Power BI dashboard.

The project combines **Python for data generation and validation, SQL for analytical verification, and Power BI/DAX for interactive reporting and visualization**.

---

## 🎯 Project Objectives

The primary objectives of this project are to:

* Monitor banking transaction activity
* Identify suspicious transactions
* Analyze transaction risk levels
* Identify high-risk customers
* Analyze transaction amounts across transaction types
* Calculate key AML monitoring KPIs
* Validate analytical results using SQL
* Build an interactive Power BI dashboard for investigation and reporting

---

## 🛠️ Technologies & Tools

* **Python**

  * Pandas
  * NumPy
  * OpenPyXL
* **SQL / MySQL**
* **Power BI**
* **DAX**
* **Git & GitHub**
* **Microsoft Excel**

---

## 📊 Dataset

The project uses a generated banking transaction dataset containing **10,000 transactions** and **1,497 unique customers**.

The dataset includes transaction, customer, geographic, risk, and suspicious-activity attributes.

### Key Columns

* `Transaction_ID`
* `Customer_ID`
* `Transaction_Amount`
* `Country`
* `Transaction_Type`
* `International_Transaction_Flag`
* `High_Risk_Customer_Flag`
* `Risk_Score`
* `Risk_Category`
* `Is_Suspicious`

The dataset is available in:

```text
Python/aml_transactions.csv
```

---

## 🔍 Project Workflow

```text
Python
   ↓
Transaction Dataset
   ↓
Data Validation
   ↓
SQL Analysis & Verification
   ↓
Power BI Data Modeling
   ↓
DAX Measures
   ↓
Interactive AML Dashboard
   ↓
Suspicious Transaction Investigation
```

---

# 📈 Power BI Dashboard

The dashboard consists of three analytical pages.

## 1. AML Executive Overview

Provides a high-level summary of the transaction portfolio and AML indicators.

### Key KPIs

* **Total Transactions:** 10,000
* **Total Transaction Amount:** 102.55M
* **Suspicious Transactions:** 36
* **Suspicious Transaction Rate:** 0.36%

### Visualizations

* Risk Category Distribution
* Transaction Amount by Transaction Type
* Transaction Detail Table
* Country Slicer

---

## 2. AML Risk Analysis

Focuses on transaction and customer risk analysis.

### Key Metrics

* High-Risk Transactions: **2**
* Average Risk Score: **13.97**
* High-Risk Customer Analysis
* Risk Category Distribution
* Transaction Risk Analysis

---

## 3. Suspicious Transactions Investigation

Provides a focused view for investigating transactions flagged as suspicious.

The page supports analysis of suspicious activity using transaction-level details and relevant risk indicators.

---

# 🧮 DAX & KPI Analysis

Several DAX measures were created to calculate important AML monitoring metrics, including:

* Total Transactions
* Total Transaction Amount
* Suspicious Transactions
* Suspicious Transaction Rate
* High-Risk Transactions
* Average Risk Score
* High-Risk Customer Transaction Amount

Example:

```DAX
Suspicious Transactions =
CALCULATE(
    [Total Transactions],
    aml_transactions[Is_Suspicious] = "Yes"
)
```

These measures allow dashboard KPIs and visualizations to dynamically respond to filters and slicers.

---

# 🗄️ SQL Analysis & Validation

SQL was used to independently verify important Power BI metrics and analyze the underlying transaction data.

The project includes **13 SQL queries** covering:

* Total transaction count
* Total transaction amount
* Suspicious transaction count
* Suspicious transaction amount
* Suspicious customer count
* High-risk transaction count
* High-risk customer count
* Average risk score
* Suspicious transaction rate
* High-risk customer transaction amount
* Transaction amount by transaction type
* Risk category distribution
* Suspicious vs. non-suspicious transactions

SQL analysis is available in:

```text
SQL/aml_analysis.sql
```

---

# 🐍 Python Analysis

Python was used for dataset generation and data validation.

### Python scripts

```text
Python/
├── aml_transactions.csv
├── generate_dataset.py
└── check_data.py
```

`generate_dataset.py` generates the transaction dataset, while `check_data.py` is used to validate and inspect the generated data.

---

# 📌 Key Project Results

Based on the final dataset:

| Metric                      |  Result |
| --------------------------- | ------: |
| Total Transactions          |  10,000 |
| Unique Customers            |   1,497 |
| Suspicious Transactions     |      36 |
| Suspicious Transaction Rate |   0.36% |
| High-Risk Transactions      |       2 |
| Average Risk Score          |   13.97 |
| Suspicious Customers        |      14 |
| High-Risk Customers         |     159 |
| Total Transaction Amount    | 102.55M |

---

# 📁 Project Structure

```text
AML-Transaction-Monitoring-PowerBI/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── PowerBI/
│   └── AML_Transaction_Monitoring_Dashboard.pbix
│
├── Python/
│   ├── aml_transactions.csv
│   ├── check_data.py
│   └── generate_dataset.py
│
├── SQL/
│   └── aml_analysis.sql
│
└── screenshots/
    ├── AML Executive Overview.png
    ├── AML Risk Analysis.png
    ├── Suspicious Transactions Investigation.png
    ├── sql_queries_verification_1.png
    └── sql_queries_verification_2.png
```

---

# ⚙️ Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/nikhilgit-1/AML-Transaction-Monitoring-PowerBI.git
cd AML-Transaction-Monitoring-PowerBI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Generate the dataset

```bash
python Python/generate_dataset.py
```

### 6. Validate the dataset

```bash
python Python/check_data.py
```

### 7. Open the Power BI dashboard

Open:

```text
PowerBI/AML_Transaction_Monitoring_Dashboard.pbix
```

---

# 📷 Dashboard Screenshots

### AML Executive Overview

![AML Executive Overview](screenshots/AML%20Executive%20%20Overview.png)

### AML Risk Analysis

![AML Risk Analysis](screenshots/AML%20Risk%20Analysis.png)

### Suspicious Transactions Investigation

![Suspicious Transactions Investigation](screenshots/Suspicious%20Transactions%20Investigation.png)

---

# 📚 Skills Demonstrated

This project demonstrates practical experience in:

* Data Analytics
* Python
* Pandas & NumPy
* SQL
* Power BI
* DAX
* Data Visualization
* KPI Development
* Risk Analysis
* Transaction Monitoring
* Data Validation
* Git & GitHub
* Dashboard Development

---

## 🚀 Future Enhancements

Potential future improvements could include:

* Automated data ingestion from a live database
* Real-time transaction monitoring
* Machine learning-based anomaly detection
* Automated alert generation
* Customer risk scoring models
* Time-series monitoring of suspicious activity
* Integration with additional AML data sources

---

## 👤 Author

**Nikhil Kumar**

B.Tech Computer Science & Engineering

GitHub: [nikhilgit-1](https://github.com/nikhilgit-1)
