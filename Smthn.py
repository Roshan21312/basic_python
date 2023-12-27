import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(0,120):

    url = 'https://www.screener.in/screens/356009/bse-nse-company-list/?page={0}'.format(i*100)  
    response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the relevant data from the HTML using BeautifulSoup
# Replace these with the actual HTML elements where the data is located on the screener.in website
name = soup.find('span', {'class': 'company-name'}).text.strip()
market_cap = soup.find('div', {'class': 'market-cap'}).text.strip()
pe_ratio = soup.find('div', {'class': 'current-pe'}).text.strip()
cmp=soup.find()



# Create a DataFrame to store the data
data = {'Name': [name], 'Market Cap': [market_cap], 'P/E Ratio': [pe_ratio]}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('company_data.xlsx', index=False)

