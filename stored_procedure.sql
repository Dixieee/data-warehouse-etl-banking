-- ========================================
-- STORED PROCEDURES
-- ========================================

GO
CREATE PROCEDURE DailyTransaction
    @start_date DATE,
    @end_date DATE
AS
BEGIN
    SELECT 
        CAST(TransactionDate AS DATE) AS [Date],
        COUNT(*) AS TotalTransactions,
        SUM(Amount) AS TotalAmount
    FROM FactTransaction
    WHERE CAST(TransactionDate AS DATE) BETWEEN @start_date AND @end_date
    GROUP BY CAST(TransactionDate AS DATE)
    ORDER BY [Date];
END;
GO


DROP PROCEDURE IF EXISTS BalancePerCustomer;
GO

CREATE PROCEDURE BalancePerCustomer
    @name VARCHAR(100)
AS
BEGIN
    SELECT 
        c.CustomerName,
        a.AccountType,
        a.Balance,
        a.Balance + 
        ISNULL(SUM(
            CASE 
                WHEN f.TransactionType = 'Deposit' THEN f.Amount
                ELSE -f.Amount
            END
        ), 0) AS CurrentBalance
    FROM DimCustomer c
    JOIN DimAccount a 
        ON c.CustomerID = a.CustomerID
    LEFT JOIN FactTransaction f 
        ON a.AccountID = f.AccountID
    WHERE 
        UPPER(c.CustomerName) LIKE '%' + UPPER(@name) + '%'
        AND LOWER(a.Status) = 'active'
    GROUP BY 
        c.CustomerName,
        a.AccountType,
        a.Balance
    ORDER BY 
        c.CustomerName,
        CASE 
            WHEN a.AccountType = 'saving' THEN 1
            WHEN a.AccountType = 'checking' THEN 2
            ELSE 3
        END;
END;
GO

-- ========================================
-- END
-- ========================================