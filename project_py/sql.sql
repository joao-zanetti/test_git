-- Example 1: Using ROW_NUMBER to find the top N records per group
WITH RankedSales AS (
    SELECT 
        EmployeeID,
        SaleAmount,
        ROW_NUMBER() OVER (PARTITION BY EmployeeID ORDER BY SaleAmount DESC) AS RowNum
    FROM Sales
)
SELECT 
    EmployeeID,
    SaleAmount
FROM RankedSales
WHERE RowNum = 1; -- Top sale per employee

-- Example 2: Using LAG to calculate the difference between consecutive rows
SELECT 
    EmployeeID,
    SaleDate,
    SaleAmount,
    LAG(SaleAmount) OVER (PARTITION BY EmployeeID ORDER BY SaleDate) AS PreviousSale,
    SaleAmount - LAG(SaleAmount) OVER (PARTITION BY EmployeeID ORDER BY SaleDate) AS SaleDifference
FROM Sales;

-- Example 3: Using LEAD to find the next event for each row
SELECT 
    CustomerID,
    PurchaseDate,
    ProductID,
    LEAD(ProductID) OVER (PARTITION BY CustomerID ORDER BY PurchaseDate) AS NextProduct
FROM Purchases;

-- Example 4: Using ROW_NUMBER to remove duplicates
WITH CTE AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY ColumnToCheckDuplicates ORDER BY ID) AS RowNum
    FROM TableName
)
DELETE FROM TableName
WHERE ID IN (
    SELECT ID FROM CTE WHERE RowNum > 1
);

-- Example 5: Using LAG and LEAD to detect gaps in sequences
SELECT 
    ID,
    Value,
    LAG(Value) OVER (ORDER BY ID) AS PreviousValue,
    LEAD(Value) OVER (ORDER BY ID) AS NextValue
FROM SequenceTable
WHERE Value - LAG(Value) OVER (ORDER BY ID) > 1
   OR LEAD(Value) OVER (ORDER BY ID) - Value > 1;

-- Example 6: Using ROW_NUMBER to paginate results
WITH PaginatedResults AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (ORDER BY SomeColumn) AS RowNum
    FROM TableName
)
SELECT *
FROM PaginatedResults
WHERE RowNum BETWEEN 11 AND 20; -- Fetch rows for page 2 (assuming 10 rows per page)