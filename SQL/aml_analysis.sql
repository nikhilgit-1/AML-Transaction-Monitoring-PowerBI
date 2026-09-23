-- AML Transaction Monitoring SQL Analysis

USE aml_monitoring;

-- 1. Total number of transactions
SELECT COUNT(*) AS total_transactions
FROM aml_transactions;

-- 2. Total transaction amount
SELECT SUM(Transaction_Amount) AS total_transaction_amount
FROM aml_transactions;

-- 3. Total suspicious transactions
SELECT COUNT(*) AS suspicious_transactions
FROM aml_transactions
WHERE Is_Suspicious = 'Yes';

-- 4. Suspicious transaction amount
SELECT SUM(Transaction_Amount) AS suspicious_transaction_amount
FROM aml_transactions
WHERE Is_Suspicious = 'Yes';

-- 5. Number of unique suspicious customers
SELECT COUNT(DISTINCT Customer_ID) AS suspicious_customers
FROM aml_transactions
WHERE Is_Suspicious = 'Yes';

-- 6. Total high-risk transactions
SELECT COUNT(*) AS high_risk_transactions
FROM aml_transactions
WHERE Risk_Category = 'High';

-- 7. Number of unique high-risk customers
SELECT COUNT(DISTINCT Customer_ID) AS high_risk_customers
FROM aml_transactions
WHERE High_Risk_Customer_Flag = 1;

-- 8. Average risk score
SELECT AVG(Risk_Score) AS average_risk_score
FROM aml_transactions;

-- 9. Suspicious transaction rate
SELECT 
    ROUND(
        COUNT(CASE WHEN Is_Suspicious = 'Yes' THEN 1 END) * 100.0 / COUNT(*),
        2
    ) AS suspicious_transaction_rate
FROM aml_transactions;

-- 10. Total transaction amount from high-risk customers
SELECT 
    SUM(Transaction_Amount) AS high_risk_customer_transaction_amount
FROM aml_transactions
WHERE High_Risk_Customer_Flag = 1;

-- 11. Transaction amount by transaction type
SELECT 
    Transaction_Type,
    SUM(Transaction_Amount) AS total_amount
FROM aml_transactions
GROUP BY Transaction_Type
ORDER BY total_amount DESC;

-- 12. Transaction count by risk category
SELECT 
    Risk_Category,
    COUNT(*) AS transaction_count
FROM aml_transactions
GROUP BY Risk_Category
ORDER BY transaction_count DESC;

-- 13. Suspicious vs non-suspicious transactions
SELECT 
    Is_Suspicious,
    COUNT(*) AS transaction_count
FROM aml_transactions
GROUP BY Is_Suspicious;