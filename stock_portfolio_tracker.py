# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 350,
    "AMZN": 130
}

total_investment = 0

print("=== STOCK PORTFOLIO TRACKER ===")

n = int(input("How many stocks do you own? "))

for i in range(n):
    stock = input("\nEnter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"Value of {stock}: ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved to portfolio.txt")
