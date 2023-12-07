"""
@AUTHORS:
Name: Rakesh Kandula
Name: Chaitanya Vardhini Anumula
"""

import pandas as pd
import random
import sys

# Read the CSV file into a pandas DataFrame
file_path = sys.argv[1]  
data = pd.read_csv(file_path)

# Create a mapping of locations to price ranges
location_price_ranges = {}

# CSV file has a column named 'location' that contains location information
for location in data['location'].unique():
    # Define price range for each location
    location_price_ranges[location] = (100,200) 

# Function to assign cost based on location's price range
def assign_cost(location):
    min_price, max_price = location_price_ranges[location]
    return random.randint(min_price, max_price)

# Add a 'Cost' column by applying the assign_cost function based on location
data['Cost'] = data['location'].apply(assign_cost)

#append the updated data to CSV file
data.to_csv(file_path, index=False)
