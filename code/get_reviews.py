"""
@AUTHORS:
Name: Rakesh Kandula
Name: Chaitanya Vardhini Anumula
"""


import csv
import requests
import sys
import random

# Function to fetch data from URL and extract details
def extract_details(id, url):
    response = requests.get(url)
    data = response.json()
    extracted_data = []

    for review in data:
        if review['language'] == 'en':
            if review['rating'] == 0:
                review['rating'] = random.randint(1, 10)
            extracted_data.append({
                'id' : id,
                'source': review['source'],
                'rating': review['rating'],
                'text': review['text']
            })                       
    return extracted_data

# Function to write data into a CSV file
def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['id','source', 'rating', 'text']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Read URLs from CSV file
urls = []
ids = []
input_file = sys.argv[1]
output_file = sys.argv[2]
print(input_file,output_file)
with open(input_file, mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    #print("reader is ",reader)
    for row in reader:
        urls.append(row['reviews'])
        ids.append(row['id'])

# Process each URL and store details in a list
all_extracted_data = []
try:
    for url, id in zip(urls, ids):
        extracted_data = extract_details(id, url)
        all_extracted_data.extend(extracted_data)
except:
    write_to_csv(all_extracted_data, output_file)

# Write the extracted details into a CSV file
write_to_csv(all_extracted_data, output_file)
