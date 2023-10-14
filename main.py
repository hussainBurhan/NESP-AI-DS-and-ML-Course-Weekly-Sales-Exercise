# Import the necessary libraries
import numpy as np 
import pandas as pd

# Set seed for reproducibility
np.random.seed(seed=0)

# Generate random items sold
items_sold = np.random.randint(20,size=(5,3))

# Display the items sold
print(items_sold)

# Create a DataFrame for weekly sales
weekly_sales = pd.DataFrame(items_sold, index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], columns=['item1', 'item2', 'item3'])

# Display the weekly sales DataFrame
print(weekly_sales)

# Define item prices
item_price = np.array([12,8,11])

# Display item prices
print(item_price)

# Create a DataFrame for item prices
item_price_df = pd.DataFrame(item_price, columns=['item price'], index=['item1', 'item2', 'item3'])

# Display the item price DataFrame
print(item_price_df)

# Calculate total price
total_price = item_price.dot(items_sold.T)

# Display total price
print(total_price)

# Add a separator for clarity
print('x'*40)

# Add 'Total Sales' column to the weekly sales DataFrame
weekly_sales['Total Sales'] = total_price

# Display the updated weekly sales DataFrame
print(weekly_sales)
