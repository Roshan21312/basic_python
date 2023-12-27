import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_company_list(page):
    url = f'https://www.screener.in/screens/356009/bse-nse-company-list/?page={page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract company names and any other relevant information
    company_names = [a.text for a in soup.find_all('a', {'class': 'company-link'})]
    
    return company_names

# Set the range of pages you want to scrape
start_page = 1
end_page = 2

# Create an empty list to store the data for all companies
all_company_names = []

# Iterate over each page
for page in range(start_page, end_page + 1):
    # Fetch the list of companies on the page
    company_list = get_company_list(page)
    all_company_names.extend(company_list)

# Create a DataFrame with the list of company names
df = pd.DataFrame({'Company Name': all_company_names})

# Save the DataFrame to an Excel file
df.to_excel('company_list.xlsx', index=False)

# Save the DataFrame to a CSV file
df.to_csv('company_list.csv', index=False)
