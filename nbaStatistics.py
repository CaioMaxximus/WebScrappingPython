import pandas as pd
import requests 
from bs4 import BeautifulSoup

def get_nba_data_years(year_begin, year_final):
    
    data = pd.DataFrame()
    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'
    for year in range(year_begin, year_final + 1):
        req = requests.get(base_url.format(year))
        if(req.status_code == 200):
            print('Ok')
            object_req = BeautifulSoup(req.content,'html.parser')
            table = object_req.find('table')
            table_str =str(table)
            local_df = pd.read_html(table_str)[0]
            local_df['Year'] = year
            data = data.append(local_df)
        else:
            print('Req year : %d Failed' %(year),
                   '----    ----' ,
                    sep = '/n')
    return data

print(get_nba_data_years(2016, 2018).head())        