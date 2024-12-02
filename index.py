import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Set date range
start_date = '2021-01-01'
# Set end_date to the most recent available date (e.g., '2023-10-31')
end_date = '2024-12-01'

# Fetch data from FRED
fedfunds = web.DataReader('FEDFUNDS', 'fred', start_date, end_date)
unrate = web.DataReader('UNRATE', 'fred', start_date, end_date)
pcepilfe = web.DataReader('PCEPILFE', 'fred', start_date, end_date)

# Calculate year-over-year Core PCE Inflation Rate
pcepilfe['Core PCE Inflation Rate'] = pcepilfe['PCEPILFE'].pct_change(periods=12) * 100

# Merge data
data = pd.concat([fedfunds, unrate, pcepilfe['Core PCE Inflation Rate']], axis=1)
data.columns = ['Federal Funds Rate', 'Unemployment Rate', 'Core PCE Inflation Rate']

# Drop rows where any of the columns are NaN
data.dropna(inplace=True)

# Filter data from 2022-01-01 onwards
data = data[data.index >= '2022-01-01']

# Create a figure with two subplots: one for the graph and one for the table
fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Plot on the first subplot
axs[0].plot(data.index, data['Federal Funds Rate'], label='Federal Funds Rate')
axs[0].plot(data.index, data['Core PCE Inflation Rate'], label='Core PCE Inflation Rate')
axs[0].plot(data.index, data['Unemployment Rate'], label='Unemployment Rate')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Percentage (%)')
axs[0].set_title('U.S. Federal Funds Rate, Core PCE Inflation Rate, and Unemployment Rate')
axs[0].legend()
axs[0].grid(True)

# Prepare the data for the table (display the last 10 rows)
table_data = data.tail(36)

# Hide axes for the table subplot
axs[1].axis('tight')
axs[1].axis('off')

# Create the table
table = axs[1].table(cellText=table_data.round(2).values,
                     colLabels=table_data.columns,
                     rowLabels=table_data.index.strftime('%Y-%m-%d'),
                     loc='center')

# Adjust table font size
table.set_fontsize(10)
table.scale(1, 1.5)  # Adjust table scaling if needed

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot with the table
plt.show()