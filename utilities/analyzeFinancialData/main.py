import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# Step 1: Load the data
data = pd.read_csv('../../src/csv_files/BTCUSDT.csv')

look_forward = 5

# Convert 'open_time' to datetime for better plotting
data['open_time'] = pd.to_datetime(data['open_time'])

# Calculate the EMA crossover
data['EMA_Crossover_Signal'] = data['EMA_50'] > data['EMA_200']


# Calculate the price increase
data['Price_Increase'] = data['close'].shift(-look_forward) > data['close']

# Calculate the EMA crossover success (EMA crossover followed by a price increase)
data['EMA_Crossover_Success'] = data['EMA_Crossover_Signal'] & data['Price_Increase']

fig, ax1 = plt.subplots()

# Plot the close price
ax1.plot(data['open_time'], data['close'], color='black')

# Plot the EMA_50 and EMA_200
ax1.plot(data['open_time'], data['EMA_50'], color='blue', label='EMA_50')
ax1.plot(data['open_time'], data['EMA_200'], color='orange', label='EMA_200')

# Create a new axis for the signals
ax2 = ax1.twinx()

# Plot the EMA crossover signals
ax2.plot(data['open_time'], data['EMA_Crossover_Signal'], color='red', label='EMA Crossover Signal', alpha=0.5)

# Plot the successful price increase signals
ax2.plot(data['open_time'], data['EMA_Crossover_Success'], color='green', label='EMA Crossover Success', alpha=0.5)

# Set the y-axis labels
ax1.set_ylabel('Price and EMA', color='gray')
ax2.set_ylabel('Signals', color='gray')

# Set the x-axis to display dates in a readable format
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Display the legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()

