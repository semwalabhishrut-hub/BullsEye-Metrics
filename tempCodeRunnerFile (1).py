import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12,6))

# Sort data by date
df = df.sort_values("full_date")

for stock in df["stock_name"].unique():
    subset = df[df["stock_name"] == stock]
    subset = subset.sort_values("full_date")

    plt.plot(
        subset["full_date"],
        subset["close_price"],
        label=stock,
        linewidth=1
    )

plt.title("Stock Price Trend Over Time (2018–2024)")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()
plt.grid(True)

plt.show()