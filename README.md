````markdown
# 📊 Data Warehouse & ETL Pipeline for Banking Transaction Analysis

## 📌 Description
This project focuses on designing and implementing a Data Warehouse along with an ETL (Extract, Transform, Load) pipeline to integrate and process banking transaction data from multiple sources including SQL Server, Excel, and CSV files.

The system enables efficient data analysis through structured dimension and fact tables, supported by analytical stored procedures.

---

## 🎯 Objectives
- Build a Data Warehouse (DWH) for banking data  
- Perform ETL from multiple data sources  
- Clean and transform data for consistency  
- Integrate transaction data into a single fact table  
- Provide analytical insights using stored procedures  

---

## 🗂️ Data Sources
- SQL Server Database (`transaction_db`, `account`, `customer`, `branch`, `city`, `state`)  
- Excel File (`transaction_excel.xlsx`)  
- CSV File (`transaction_csv.csv`)  

---

## ⚙️ Tools & Technologies
- Python (Pandas, SQLAlchemy)  
- Microsoft SQL Server  
- SQL Server Management Studio (SSMS)  

---

## 🏗️ Data Warehouse Schema

### Dimension Tables
- `DimCustomer`  
- `DimAccount`  
- `DimBranch`  

### Fact Table
- `FactTransaction`  

---

## 🔄 ETL Process

### Extract
- Load data from SQL Server, Excel, and CSV  

### Transform
- Data cleaning and formatting  
- Uppercase transformation for customer data  
- Join customer, city, and state tables  
- Remove duplicate transaction records  
- Standardize column naming (PascalCase)  

### Load
- Insert processed data into Data Warehouse tables  

---

## 📊 Stored Procedures

### 1. DailyTransaction
- Calculates daily transaction count and total amount  
- Parameters:
  - `start_date`  
  - `end_date`  

### 2. BalancePerCustomer
- Calculates current balance per customer  
- Logic:
  - Deposit → adds balance  
  - Other transactions → subtract balance  
- Parameter:
  - `name`  

---

## ▶️ How to Run

### 1. Create Database & Tables
Run:
```sql
create_table.sql
````

### 2. Run ETL Process

```bash
python etl.py
```

### 3. Create Stored Procedures

Run:

```sql
stored_procedure.sql
```

### 4. Execute Stored Procedures

```sql
EXEC DailyTransaction @start_date='2024-01-20', @end_date='2024-01-22';
EXEC BalancePerCustomer @name='Shelly';
```

---

## 📁 Project Structure

```
data-warehouse-etl-banking/
│
├── etl.py
├── sql/
│   ├── create_table.sql
│   ├── stored_procedure.sql
├── data/
│   ├── transaction_excel.xlsx
│   ├── transaction_csv.csv
└── README.md
```

---

## 🚀 Key Highlights

* End-to-end ETL pipeline implementation
* Integration of multiple heterogeneous data sources
* Data cleaning and transformation
* Data Warehouse design with relational integrity
* Analytical querying using stored procedures

---

## 📌 Author

**Your Name Here**

---

## 📎 Notes

This project was developed as part of a Data Engineer Project-Based Internship (VIX Program).

```
```
