---

DATA WAREHOUSE & ETL PIPELINE FOR BANKING TRANSACTION ANALYSIS

Description
Project ini bertujuan untuk membangun Data Warehouse dan ETL (Extract, Transform, Load) pipeline untuk mengintegrasikan dan mengolah data transaksi perbankan dari berbagai sumber seperti SQL Server, Excel, dan CSV.
Data yang sudah terstruktur digunakan untuk analisis melalui stored procedure.

---

Objectives

* Membangun Data Warehouse (DWH) untuk data perbankan
* Melakukan ETL dari berbagai sumber data
* Membersihkan dan mentransformasi data
* Menggabungkan data transaksi ke dalam satu tabel
* Menyediakan analisis data menggunakan stored procedure

---

Data Sources

* SQL Server Database (transaction_db, account, customer, branch, city, state)
* File Excel (transaction_excel.xlsx)
* File CSV (transaction_csv.csv)

---

Tools & Technologies

* Python (Pandas, SQLAlchemy)
* Microsoft SQL Server
* SQL Server Management Studio (SSMS)

---

Data Warehouse Schema

Dimension Tables

* DimCustomer
* DimAccount
* DimBranch

Fact Table

* FactTransaction

---

ETL Process

Extract

* Mengambil data dari SQL Server, Excel, dan CSV

Transform

* Membersihkan data
* Mengubah huruf menjadi uppercase pada data customer
* Menggabungkan tabel customer, city, dan state
* Menghapus data duplikat
* Mengubah nama kolom ke format PascalCase

Load

* Memasukkan data ke dalam tabel Data Warehouse

---

Stored Procedures

DailyTransaction

* Menghitung jumlah transaksi per hari dan total nominal
* Parameter: start_date dan end_date

BalancePerCustomer

* Menghitung saldo akhir per customer
* Deposit menambah saldo, transaksi lain mengurangi saldo
* Parameter: name

---

How to Run

1. Jalankan create_table.sql untuk membuat database dan tabel
2. Jalankan etl.py untuk proses ETL
3. Jalankan stored_procedure.sql untuk membuat stored procedure
4. Jalankan query berikut di SQL Server:

EXEC DailyTransaction @start_date='2024-01-20', @end_date='2024-01-22';
EXEC BalancePerCustomer @name='Shelly';

---

Project Structure

data-warehouse-etl-banking

* etl.py
* sql

  * create_table.sql
  * stored_procedure.sql
* data

  * transaction_excel.xlsx
  * transaction_csv.csv
* README

---

Key Highlights

* Implementasi ETL end-to-end
* Integrasi data dari berbagai sumber
* Data cleaning dan transformasi
* Desain Data Warehouse dengan relasi yang baik
* Analisis menggunakan stored procedure

---

Author
Dafanov Dixie Einkinderen

---

Notes
Project ini dibuat sebagai bagian dari Data Engineer Project-Based Internship (VIX Program)

---
