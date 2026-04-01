import pandas as pd
from ofxparse import OfxParser
import gc # Garbage collector to free up memory if needed

def qbo_to_dataframe(filename):
    """Parse QBO file and return transactions as DataFrame"""
    transactions = []
    
    with open(filename, 'rb') as f:
        ofx = OfxParser.parse(f)
    
    for account in ofx.accounts:
        for transaction in account.statement.transactions:
            transactions.append({
                'date': transaction.date,
                'amount': float(transaction.amount),
                'description': transaction.payee,
                'type': transaction.type,
                'id': transaction.id,
            })
    
    df = pd.DataFrame(transactions)
    df['date'] = pd.to_datetime(df['date'])
    return df

# Usage
# Clean up any existing DataFrame to free memory before loading new data
try:
    del df1
except NameError:
    pass
gc.collect()

df1 = qbo_to_dataframe('2025-bank-statement.qbo')
print(df1.head())
print(df1.info())

# If it looks good, we can start analysis.
# For example, let's calculate the total amount spent and received.
total_spent = df1[df1['amount'] < 0]['amount'].sum()
total_received = df1[df1['amount'] > 0]['amount'].sum()
print(f'Annual Total Spent: ${total_spent:.2f}')
print(f'Annual Total Received: ${total_received:.2f}')

# Let's calculate our average monthly spending:
df1['Month'] = df1['date'].dt.to_period('M')
monthly_average_spending = df1[df1['amount'] < 0].groupby('Month')['amount'].sum() / 11  # Assuming the data is for 11 months
print(f'Average Monthly Spending: ${monthly_average_spending.sum():.2f}')