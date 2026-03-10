import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aayush@2004",
    database="dwdm_stock"
)

query = """
SELECT
    f.open_price,
    f.high_price,
    f.low_price,
    f.volume,
    f.close_price
FROM fact_stock_price f
"""

df = pd.read_sql(query, conn)

print("Dataset Loaded:")
print(df.head())

# Features and target
X = df[['open_price','high_price','low_price','volume']]
y = df['close_price']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, predictions)
print("\nModel MSE:", mse)

# Plot prediction vs actual
plt.scatter(y_test, predictions)
plt.xlabel("Actual Close Price")
plt.ylabel("Predicted Close Price")
plt.title("Stock Price Prediction")
plt.show()