"""
Tata Steel Stock Price Analysis with Moving Averages

This notebook analyzes Tata Steel's stock price trends using 50-day and 200-day moving averages.
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Fetch Tata Steel stock data
tata_steel = yf.Ticker("TATASTEEL.NS")
data = tata_steel.history(period="5y")

# Drop unnecessary columns
data = data.drop(columns=["Dividends", "Stock Splits"], errors="ignore")
data = data.reset_index()

data["Date"] = pd.to_datetime(data["Date"])
data.set_index("Date", inplace=True)

# Calculate 50-day and 200-day Moving Averages
data["50_MA"] = data["Close"].rolling(window=50).mean()
data["200_MA"] = data["Close"].rolling(window=200).mean()

# Plot stock price with moving averages
plt.figure(figsize=(15, 8))
plt.plot(data.index, data["Close"], label="Stock Price", color="black", linewidth=1)
plt.plot(data.index, data["50_MA"], label="50-Day MA", color="red", linestyle="--", linewidth=0.5)
plt.plot(data.index, data["200_MA"], label="200-Day MA", color="green", linestyle="--", linewidth=0.5)

plt.title("Tata Steel Stock Price with 50 & 200 Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# Calculate Monthly Returns
data["Returns"] = data["Close"].resample('ME').ffill().pct_change()

# Plot returns distribution
plt.figure(figsize=(15, 8))
sns.histplot(data["Returns"].dropna(), bins=50, kde=True)
plt.title("Monthly Returns Distribution")
plt.show()

# Interpretation of Moving Averages
print("""
Key Insights from 50 & 200 Moving Averages:

1. **Bounce Back from MA (Support & Resistance)**
   - If the stock price bounces up after touching the 50-day MA, it indicates bullish strength.
   - If price bounces from the 200-day MA, it’s a strong bullish signal (trend continuation).
   - If price breaks below the 200-day MA, it’s a bearish sign (trend reversal).

2. **Golden Cross & Death Cross (Trend Change Signals)**
   - **Golden Cross**: When the 50-day MA crosses above the 200-day MA → Bullish trend (Buy Signal).
   - **Death Cross**: When the 50-day MA crosses below the 200-day MA → Bearish trend (Sell Signal).
""")
