
stock_prices = {
    "AAPL": 180,    # Apple Inc.
    "TSLA": 250,    # Tesla Inc.
    "GOOGL": 140,   # Alphabet Inc. (Google)
    "AMZN": 130,    # Amazon.com, Inc.
    "MSFT": 330     # Microsoft Corporation
}

# -----------------------------
# Display Available Stocks
# -----------------------------
print("===========================================")
print("        STOCK PORTFOLIO TRACKER            ")
print("===========================================\n")

print("Available Stocks and Their Prices (Per Share):\n")
for stock, price in stock_prices.items():
    print(f"{stock:<8} : ${price}")

# -----------------------------
# Initialize Portfolio Details
# -----------------------------
portfolio = {}
total_investment = 0

# -----------------------------
# User Input for Stocks
# -----------------------------
while True:
    stock_name = input("\nEnter Stock Symbol (or type 'done' to finish): ").upper()

    if stock_name == 'DONE':
        break

    if stock_name not in stock_prices:
        print("Invalid Stock Symbol! Please select from the available list.")
        continue

    try:
        quantity = int(input(f"Enter Quantity of {stock_name}: "))
    except ValueError:
        print("Invalid Input! Quantity must be a number.")
        continue

    # Update portfolio and total investment
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    investment_value = stock_prices[stock_name] * quantity
    total_investment += investment_value

    print(f"Added {quantity} shares of {stock_name} worth ${investment_value}")

# -----------------------------
# Display Portfolio Summary
# -----------------------------
print("\n===========================================")
print("              PORTFOLIO SUMMARY             ")
print("===========================================\n")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    print(f"{stock:<8} : {quantity} shares × ${price} = ${value}")

print("-------------------------------------------")
print(f"Total Investment Value: ${total_investment}")
print("===========================================\n")

# -----------------------------
# Save Portfolio to File
# -----------------------------
save_choice = input("Would you like to save this summary to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("Portfolio_Summary.txt", "w") as file:
        file.write("========== STOCK PORTFOLIO SUMMARY ==========\n\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock:<8} : {quantity} shares × ${price} = ${value}\n")
        file.write("-------------------------------------------\n")
        file.write(f"Total Investment Value: ${total_investment}\n")
        file.write("===========================================\n")
    print("\nPortfolio summary successfully saved to 'Portfolio_Summary.txt'.")

print("\nThank you for using the Stock Portfolio Tracker!")