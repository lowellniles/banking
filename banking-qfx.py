import pandas as pd
from ofxparse import OfxParser
import gc

# Clean up previous data
try:
    del df
except NameError:
    pass
gc.collect()

def qfx_to_dataframe(filename):
    """Parse QFX file and return transactions as DataFrame"""
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

df = qfx_to_dataframe('2025-bank-statement.qfx')
print(df.head())
print(df.info())

# If it looks good, we can start analysis.
# For example, let's calculate the total amount spent and received.
total_spent = df[df['amount'] < 0]['amount'].sum()
total_received = df[df['amount'] > 0]['amount'].sum()
print(f'Annual Total Spent: ${total_spent:.2f}')
print(f'Annual Total Received: ${total_received:.2f}')

# Let's calculate our average monthly spending:
df['Month'] = df['date'].dt.to_period('M')
monthly_average_spending = df[df['amount'] < 0].groupby('Month')['amount'].sum() / 11  # Assuming the data is for 11 months
print(f'Average Monthly Spending: ${monthly_average_spending.sum():.2f}')
