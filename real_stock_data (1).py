import yfinance as yf
import pandas as pd

stocks = {
    "TCS": "TCS.BO",
    "RELIANCE": "RELIANCE.BO",
    "HDFC": "HDFCBANK.BO",
    "APPLE": "AAPL",
    "TESLA": "TSLA"
}

start_date = "2018-01-01"
end_date = "2023-12-31"

all_data = []

for name, ticker in stocks.items():
    print(f"Downloading {name}...")

    df = yf.Ticker(ticker).history(start=start_date, end=end_date)

    if df.empty:
        print(f"Skipped {name}")
        continue

    df.reset_index(inplace=True)
    df["Stock"] = name
    all_data.append(df)

final_df = pd.concat(all_data)
final_df = final_df[["Date","Open","High","Low","Close","Volume","Stock"]]

final_df.to_csv("stock_data_real.csv", index=False)

print("\nReal stock data downloaded successfully")
print(final_df["Stock"].value_counts())