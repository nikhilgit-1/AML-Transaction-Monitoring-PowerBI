## Script to validate AML transaction dataset
import pandas as pd

df = pd.read_csv('aml_transactions.csv')

total_amount = df['Transaction_Amount'].sum()
total_transactions = len(df)
suspicious_count = len(df[df['Is_Suspicious'] == "Yes"])
risk_categories = df.groupby('Risk_Category').size()

print(f"total transaction amount: {total_amount}")
print(f"total transactions: {total_transactions}")
print(f"Suspicious Transactions in Python: {suspicious_count}")
print(f"risk categories: {risk_categories}")
print('High-Risk Transactions:', (df['Risk_Category']=='High').sum())
print(df.loc[df['Risk_Category']=='High', ['Transaction_ID','Customer_ID','Transaction_Amount','Country','Transaction_Type','Risk_Score','Risk_Category','Is_Suspicious']].to_string(index=False))
