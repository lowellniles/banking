import pandas as pd

# Load the bank CSV file into aDataFrame
df1 = pd.read_csv('2025-bank-statement.csv')

# Display the DataFrame
print(df1.head())

# Let's remove the description, Comments, Check Number,
# and Balance columns.
df1 = df1.drop(columns=['Description','Comments','Check Number','Balance'])

# Now, let's convert the dollar 'Amount' column to numeric values.
df1['Amount'] = pd.to_numeric(df1['Amount'].str.replace('$', '').str.replace(',', ''), errors='coerce')

# Display the DataFrame to check the changes
print(df1)

# If it looks good, we can start analysis.
# For example, let's calculate the total amount spent and received.
total_spent = df1[df1['Amount'] < 0]['Amount'].sum()
total_received = df1[df1['Amount'] > 0]['Amount'].sum()
print(f'Annual Total Spent: ${total_spent:.2f}')
print(f'Annual Total Received: ${total_received:.2f}')

# Let's calculate our average monthly spending:
df1['Date'] = pd.to_datetime(df1['Date'])
df1['Month'] = df1['Date'].dt.to_period('M')
monthly_average_spending = df1[df1['Amount'] < 0].groupby('Month')['Amount'].sum() / 11  # Assuming the data is for 11 months
print(f'Average Monthly Spending: ${monthly_average_spending.sum():.2f}')