import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime



## Credits to  https://github.com/sd3v/openinsiderData/blob/main/openinsider_scraper.py for base code

def get_data_for_current_date():
    """
    
    Gets the current dates data using beatifulsoup
    
    
    """
    # Set the start date and end date for the given month
    current_date = datetime.now()
    formatted_date = current_date.strftime("%m/%d/%Y")

 

    # Initialize an empty set to store the data for the month
    data = set()

    # Make a request to the website
    url = f'http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=-1&fdr={formatted_date}+-+{formatted_date}&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=5000&page=1'
    response = requests.get(url)
    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the rows in the table on the website
    rows = soup.find('table', {'class': 'tinytable'}).find('tbody').findAll('tr')
    field_names = ['transaction_date','trade_date', 'ticker', 'company_name', 'owner_name', 'Title' ,'transaction_type', 'last_price', 'Qty', 'shares_held', 'Owned', 'Value']
    # Loop through each row and extract the insider transaction data
    for row in rows:
        if not row.findAll('td'):
            continue
        insider_data = {}
        insider_data['transaction_date'] = row.findAll('td')[1].find('a').text.strip()
        insider_data['trade_date'] = row.findAll('td')[2].text.strip()
        insider_data['ticker'] = row.findAll('td')[3].find('a').text.strip()
        insider_data['company_name'] = row.findAll('td')[4].find('a').text.strip()
        insider_data['owner_name'] = row.findAll('td')[5].find('a').text.strip()
        insider_data['Title'] = row.findAll('td')[6].text.strip()
        insider_data['transaction_type'] = row.findAll('td')[7].text.strip()
        insider_data['last_price'] = row.findAll('td')[8].text.strip()
        insider_data['Qty'] = row.findAll('td')[9].text.strip()
        insider_data['shares_held'] = row.findAll('td')[10].text.strip()
        insider_data['Owned'] = row.findAll('td')[11].text.strip()
        insider_data['Value'] = row.findAll('td')[12].text.strip()
        # Add the Data to the Stack
        data.add(tuple(insider_data.values()))
    df = pd.DataFrame(data, columns=field_names)

    ## Changes

    df['last_price'] = pd.to_numeric(df['last_price'].str[1:].str.replace(',', ''))
    df['Qty'] = pd.to_numeric(df['Qty'].str[1:].str.replace(',', ''))
    df['Value'] = pd.to_numeric(df['Value'].str[2:].str.replace(',', ''))
    df['shares_held'] = pd.to_numeric(df['shares_held'].str.replace(',', ''))
    
    df.to_csv('./downloads/test.csv', index=False)

    
    return df

    
    
    





if __name__ == "__main__":
    get_data_for_current_date()