# Objective: Write a Python script that processes hardcoded data, analyzes it, and outputs a summary report.

# Data Structure: Use a list of tuples or dictionaries to represent your data. Each element should contain information about a product, structured as follows: (ProductID, ProductName, Category, Price).

# Requirements:

# Hardcoded Data: Instead of reading from a file, define your data within the script. Use at least 6 products across at least 3 different categories.
# python
# Copy code
# products = [
#     (101, "Pencil", "Stationery", 1.20),  #CHATGPT4 MADE THIS ERROR.....
#     (102, "Notebook", "Stationary", 2.50),
#     (103, "Desk Lamp", "Furniture", 23.99),
#     (104, "Stapler", "Office Supplies", 5.75),
#     (105, "Monitor", "Furniture", 199.99),
#     (106, "Pen", "Stationery", 1.50)
# ]
# Analyze Data:

# Calculate the average price of products in each category.
# Identify the most expensive product in each category.
# Output:

# Print a summary report to the console. For each category, list the average price and the name of the most expensive product.
# Ensure categories are listed alphabetically in the report.
# Expected Outcome:

# Your script should output a report similar to the one below, but the content will depend on your hardcoded data.

# yaml
# Copy code
# Category: Furniture
# - Average Price: $111.99
# - Most Expensive Product: Monitor

# Category: Office Supplies
# - Average Price: $5.75
# - Most Expensive Product: Stapler

# Category: Stationery
# - Average Price: $1.73
# - Most Expensive Product: Notebook
# Evaluation Criteria:

# Correct implementation of data structures to represent the given data.
# Accurate calculation of average prices and identification of the most expensive products.
# Proper sorting and formatting of the output.

products = [
    (101, "Pencil", "Stationery", 1.20),
    (102, "Notebook", "Stationary", 2.50),
    (103, "Desk Lamp", "Furniture", 23.99),
    (104, "Stapler", "Office Supplies", 5.75),
    (105, "Monitor", "Furniture", 199.99),
    (106, "Pen", "Stationery", 1.50)
]

category_prices = {}
most_expensive = {}

for product in products:
    id, name, category, price = product
    if category in category_prices:
        category_prices[category].append(price)
    else:
        category_prices[category] = [price]

for category, prices in category_prices.items():
    avg_price = sum(prices) / len(prices)
    most_expensive[category] = max(prices)

sorted_categories = sorted(category_prices.keys())

output_result = ""
for category in sorted_categories:
    output_result += f"{category} ${round(avg_price, 2)} {most_expensive[category]}\n"

print(output_result)
