-- ========================================
-- CREATE DATABASE & TABLES
-- ========================================

CREATE DATABASE DWH;
GO

USE DWH;
GO

-- ========================================
-- DIMENSION TABLES
-- ========================================

CREATE TABLE DimCustomer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    Address VARCHAR(255),
    CityName VARCHAR(100),
    StateName VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Email VARCHAR(100)
);

CREATE TABLE DimBranch (
    BranchID INT PRIMARY KEY,
    BranchName VARCHAR(100),
    BranchLocation VARCHAR(255)
);

CREATE TABLE DimAccount (
    AccountID INT PRIMARY KEY,
    CustomerID INT,
    AccountType VARCHAR(50),
    Balance FLOAT,
    DateOpened DATE,
    Status VARCHAR(20),

    FOREIGN KEY (CustomerID) REFERENCES DimCustomer(CustomerID)
);

-- ========================================
-- FACT TABLE
-- ========================================

CREATE TABLE FactTransaction (
    TransactionID INT PRIMARY KEY,
    AccountID INT,
    TransactionDate DATE,
    Amount FLOAT,
    TransactionType VARCHAR(50),
    BranchID INT,

    FOREIGN KEY (AccountID) REFERENCES DimAccount(AccountID),
    FOREIGN KEY (BranchID) REFERENCES DimBranch(BranchID)
);

-- ========================================
-- END
-- ========================================