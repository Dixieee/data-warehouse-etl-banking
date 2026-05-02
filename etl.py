# ========================================
# ETL PIPELINE - DATA WAREHOUSE
# ========================================

import pandas as pd
from sqlalchemy import create_engine, text

# ========================================
# CONNECT DATABASE
# ========================================

engine = create_engine(
    "mssql+pyodbc://localhost/DWH?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

source_engine = create_engine(
    "mssql+pyodbc://localhost/sample?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

print("✅ Connected to databases")

# ========================================
# EXTRACT DIMENSION DATA
# ========================================

customer = pd.read_sql("SELECT * FROM customer", source_engine)
city = pd.read_sql("SELECT * FROM city", source_engine)
state = pd.read_sql("SELECT * FROM state", source_engine)
account = pd.read_sql("SELECT * FROM account", source_engine)
branch = pd.read_sql("SELECT * FROM branch", source_engine)

print("✅ Dimension data extracted")

# ========================================
# TRANSFORM DIMCUSTOMER
# ========================================

df = customer.merge(city, on="city_id").merge(state, on="state_id")

df["customer_name"] = df["customer_name"].str.upper()
df["address"] = df["address"].str.upper()
df["city_name"] = df["city_name"].str.upper()
df["state_name"] = df["state_name"].str.upper()
df["gender"] = df["gender"].str.upper()

dim_customer = df.rename(columns={
    "customer_id": "CustomerID",
    "customer_name": "CustomerName",
    "address": "Address",
    "city_name": "CityName",
    "state_name": "StateName",
    "age": "Age",
    "gender": "Gender",
    "email": "Email"
})[
    ["CustomerID", "CustomerName", "Address", "CityName", "StateName", "Age", "Gender", "Email"]
]

# ========================================
# TRANSFORM DIMACCOUNT
# ========================================

dim_account = account.rename(columns={
    "account_id": "AccountID",
    "customer_id": "CustomerID",
    "account_type": "AccountType",
    "balance": "Balance",
    "date_opened": "DateOpened",
    "status": "Status"
})

# ========================================
# TRANSFORM DIMBRANCH
# ========================================

dim_branch = branch.rename(columns={
    "branch_id": "BranchID",
    "branch_name": "BranchName",
    "branch_location": "BranchLocation"
})

# ========================================
# LOAD DIMENSIONS
# ========================================

with engine.connect() as conn:
    conn.execute(text("DELETE FROM DimCustomer"))
    conn.execute(text("DELETE FROM DimAccount"))
    conn.execute(text("DELETE FROM DimBranch"))
    conn.commit()

dim_customer.to_sql("DimCustomer", engine, if_exists="append", index=False)
dim_account.to_sql("DimAccount", engine, if_exists="append", index=False)
dim_branch.to_sql("DimBranch", engine, if_exists="append", index=False)

print("✅ Dimension tables loaded")

# ========================================
# EXTRACT FACT DATA
# ========================================

db_df = pd.read_sql("SELECT * FROM transaction_db", source_engine)
excel_df = pd.read_excel("transaction_excel.xlsx")
csv_df = pd.read_csv("transaction_csv.csv")

print("✅ Fact data extracted")

# ========================================
# TRANSFORM FACT
# ========================================

csv_df["transaction_date"] = pd.to_datetime(csv_df["transaction_date"], dayfirst=True)
excel_df["transaction_date"] = pd.to_datetime(excel_df["transaction_date"])

fact = pd.concat([db_df, excel_df, csv_df])
fact["transaction_id"] = fact["transaction_id"].astype(int)
fact = fact.drop_duplicates()

fact = fact.rename(columns={
    "transaction_id": "TransactionID",
    "account_id": "AccountID",
    "transaction_date": "TransactionDate",
    "amount": "Amount",
    "transaction_type": "TransactionType",
    "branch_id": "BranchID"
})

# ========================================
# LOAD FACT
# ========================================

with engine.connect() as conn:
    conn.execute(text("DELETE FROM FactTransaction"))
    conn.commit()

fact.to_sql("FactTransaction", engine, if_exists="append", index=False)

print("✅ FactTransaction loaded")

# ========================================
# DONE
# ========================================

print("🚀 ETL PROCESS COMPLETED")