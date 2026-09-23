import pandas as pd
import numpy as np

# print("AML Transaction Monitoring Project")
# print("Python is working successfully!")

# ---------------------------------------------------------
# AML Transaction Monitoring Project
# Synthetic Banking Transaction Dataset Generator
# ---------------------------------------------------------

np.random.seed(42)

# ---------------------------------------------------------
# 1. Basic configuration
# ---------------------------------------------------------

NUM_TRANSACTIONS = 10000
NUM_CUSTOMERS = 1500

# ---------------------------------------------------------
# 2. Create customer master data
# ---------------------------------------------------------

customer_ids = [f"CUST{str(i).zfill(5)}"
		for i in range(1, NUM_CUSTOMERS+1)
]

first_names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rahul",
    "Rohan", "Karan", "Vikram", "Ankit", "Nikhil",
    "Aman", "Mohit", "Rohit", "Varun", "Yash",
    "Priya", "Ananya", "Aditi", "Neha", "Pooja",
    "Kavya", "Isha", "Sneha", "Riya", "Simran"
]

last_names = [
    "Sharma", "Verma", "Gupta", "Mehta", "Singh",
    "Kumar", "Joshi", "Agarwal", "Malhotra", "Bansal",
    "Chopra", "Kapoor", "Saxena", "Mishra", "Rathi",
    "Jain", "Shah", "Soni", "Yadav", "Patel"
]

customer_names = [
    f"{np.random.choice(first_names)} {np.random.choice(last_names)}"
    for _ in range(NUM_CUSTOMERS)
]

customer_data = pd.DataFrame({
		"Customer_ID": customer_ids,
                "Customer_Name": customer_names,
		"Customer_Age": np.random.randint(21,70,NUM_CUSTOMERS),
		"Account_Type": np.random.choice(["Savings","Current","Business"],
		NUM_CUSTOMERS, p=[0.60, 0.30, 0.10]),
		"Customer_Risk_Level": np.random.choice(["Low","Medium","High"],
		NUM_CUSTOMERS, p=[0.60,0.30,0.10])
})

# ---------------------------------------------------------
# 3. Create transaction-level data
# ---------------------------------------------------------

transaction_ids = [f"TXN{str(i).zfill(7)}"
		   for i in range(1,NUM_TRANSACTIONS+1)]

# Random transaction dates

transaction_dates = pd.to_datetime(
		     np.random.choice(
		     pd.date_range(start="2025-01-01",end="2026-06-30",freq="h"),
		     NUM_TRANSACTIONS))
countries = [ "India",
    "United States",
    "United Kingdom",
    "Singapore",
    "United Arab Emirates",
    "Germany",
    "France",
    "Canada",
    "Australia",
    "Hong Kong"]

transaction_types = [  "Cash Deposit",
    "Cash Withdrawal",
    "Bank Transfer",
    "International Transfer",
    "Card Payment",
    "Online Payment"]

channels = [ "Branch",
    "ATM",
    "Online Banking",
    "Mobile Banking",
    "Card"]

merchant_categories = [
    "Retail",
    "Travel",
    "Electronics",
    "Food",
    "Healthcare",
    "Jewelry",
    "Real Estate",
    "Financial Services"
]

df = pd.DataFrame({
     "Transaction_ID": transaction_ids,
     "Customer_ID": np.random.choice(
                    customer_ids,
                    NUM_TRANSACTIONS),
      "Transaction_Date": transaction_dates,
      "Transaction_Amount": np.round(
                            np.random.lognormal(
                                mean=8.5,
                                sigma=1.2,
                                size=NUM_TRANSACTIONS),
                                2),
       "Country": np.random.choice(
                  countries,
                  NUM_TRANSACTIONS,
                  p=[0.55,
                     0.08,
                     0.07,
                     0.06,
                     0.06,
                     0.04,
                     0.03,
                     0.03,
                     0.04,
                     0.04]),
 
        "Transaction_Type": np.random.choice(
                            transaction_types,
                            NUM_TRANSACTIONS,
                            p=[0.15,
            0.10,
            0.25,
            0.10,
            0.20,
            0.20]),

        "Channel": np.random.choice(
                   channels,
                   NUM_TRANSACTIONS,
                   p=[  0.15,
            0.10,
            0.25,
            0.25,
            0.25]),

        "Merchant_Category": np.random.choice(
                             merchant_categories,
                             NUM_TRANSACTIONS)
})

# Make most transaction amounts whole numbers
# Keep a small percentage with decimal values

decimal_mask = np.random.random(NUM_TRANSACTIONS) < 0.05

df.loc[~decimal_mask, "Transaction_Amount"] = (
    df.loc[~decimal_mask, "Transaction_Amount"].round(0)
)

df.loc[decimal_mask, "Transaction_Amount"] = (
    df.loc[decimal_mask, "Transaction_Amount"].round(2)
)

# ---------------------------------------------------------
# 4. Keep transaction amounts within a realistic range
# ---------------------------------------------------------

df["Transaction_Amount"]= np.clip(
                          df["Transaction_Amount"],500,5000000)

# ---------------------------------------------------------
# 5. Add customer information to transactions
# ---------------------------------------------------------

df= df.merge(
    customer_data,
    on = "Customer_ID",
    how= "left")

# ---------------------------------------------------------
# 6. Calculate customer transaction frequency
# ---------------------------------------------------------


df = df.sort_values(
    ["Customer_ID", "Transaction_Date"]
).reset_index(drop=True)

df["Previous_Transaction_Count"] = (
    df.groupby("Customer_ID").cumcount()
)


# ---------------------------------------------------------
# 7. Create synthetic AML behavioral indicators
# ---------------------------------------------------------

# Indicator 1: Large transaction

df["Large_Transaction_Flag"] = np.where(
                               df["Transaction_Amount"] >= 500000,1,0 )

# Indicator 2: International transaction

df["International_Transaction_Flag"] = np.where(
                                       df["Transaction_Type"] == "International Transfer",
                                       1,
                                       0)

# Indicator 3: High transaction frequency

df["High_Frequency_Flag"] = np.where(
                            df["Previous_Transaction_Count"] >= 10,
                            1,
                            0)

# Indicator 4: High-risk customer
df["High_Risk_Customer_Flag"] = np.where(
    df["Customer_Risk_Level"] == "High",
    1,
    0
)

# Indicator 5: High-value transaction
df["High_Value_Flag"] = np.where(
    df["Transaction_Amount"] >= 200000,
    1,
    0
)

# ---------------------------------------------------------
# 8. Create synthetic risk score
# ---------------------------------------------------------

df["Risk_Score"] = (
    10
    + df["Large_Transaction_Flag"] * 30
    + df["International_Transaction_Flag"] * 15
    + df["High_Frequency_Flag"] * 15
    + df["High_Risk_Customer_Flag"] * 20
    + df["High_Value_Flag"] * 10
    + np.random.normal(0, 4, NUM_TRANSACTIONS)
)

# Keep risk score between 0 and 100
df["Risk_Score"] = np.clip(
    np.round(df["Risk_Score"]),
    0,
    100
).astype(int)

# ---------------------------------------------------------
# 9. Convert risk score into risk category
# ---------------------------------------------------------

df["Risk_Category"] = np.select(
    [
        df["Risk_Score"] >= 55,
        df["Risk_Score"] >= 30
    ],
    [
        "High",
        "Medium"
    ],
    default="Low"
)

# ---------------------------------------------------------
# 10. Create suspicious transaction flag
# ---------------------------------------------------------

suspicious_condition = (
    (df["Risk_Score"] >= 55)
    |
    (
        (df["Transaction_Amount"] >= 300000)
        &
        (df["Transaction_Type"] == "International Transfer")
    )
    |
    (
        (df["High_Risk_Customer_Flag"] == 1)
        &
        (df["High_Frequency_Flag"] == 1)
    )
    |
    (
        (df["Large_Transaction_Flag"] == 1)
        &
        (df["International_Transaction_Flag"] == 1)
    )
)

df["Is_Suspicious"] = np.where(
    suspicious_condition,
    "Yes",
    "No"
)

# ---------------------------------------------------------
# 11. Sort transactions by date
# ---------------------------------------------------------

df = df.sort_values(
    "Transaction_Date"
).reset_index(drop=True)

# ---------------------------------------------------------
# 12. Save final dataset
# ---------------------------------------------------------

output_file = "aml_transactions.csv"

df.to_csv(
    output_file,
    index=False
)

# ---------------------------------------------------------
# 13. Display summary
# ---------------------------------------------------------

print()
print("==============================================")
print("AML TRANSACTION DATASET GENERATED")
print("==============================================")

print(f"Total Transactions: {len(df)}")
print(f"Total Customers: {df['Customer_ID'].nunique()}")

print(
    f"Suspicious Transactions: "
    f"{(df['Is_Suspicious'] == 'Yes').sum()}"
)

print(
    f"High-Risk Transactions: "
    f"{(df['Risk_Category'] == 'High').sum()}"
)

print(
    f"Average Risk Score: "
    f"{df['Risk_Score'].mean():.2f}"
)

print()
print(f"Dataset saved as: {output_file}")
print("==============================================")




