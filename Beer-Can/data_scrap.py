from urllib.request import urlopen
 
from bs4 import BeautifulSoup
import pandas as pd
import re

def is_id(table_row) :
    table_data = table_row.findAll('td')
    id_data = table_data[0].text
    id_value = get_id(id_data)
    if (len(table_data)==8 and id_value) :
        return True
    else :
        return False

def get_id(id_data) :
    val = re.match("^(\d{1,4})\.$", id_data)
    if (val and len(val.groups())==1) :
        return int(val.group(1))
    else :
        return None ;
     
def get_beer_data(html_data) :
    beer_data = []
    beer_tr = html_data.findAll('tr');
    for tablerow in beer_tr :
        if (is_id(tablerow)) :
            beer_v = tablerow.findAll('td')
            beer_value = {
                "id": get_id(beer_v[0].text),
                "name": beer_v[1].text,
                "brewery_name": beer_v[2].text,
                "brewery_location": beer_v[3].text,
                "style": beer_v[4].text,
                "size": beer_v[5].text,
                "abv": beer_v[6].text,    
                "ibu": beer_v[7].text
            }

            beer_data.append(beer_value)
    return beer_data

def clean_abv(value) :
    val = str(value).split('%')[0]
    try :
        return float(val)/100;
    except :
        return None


def str_to_int(value) :
    try :
        return int(value)
    except :
        return None

def strip_oz(value) :
    val = str(value).split('oz')[0]
    return val


	### Reading Url ####	
html = urlopen("http://craftcans.com/db.php?search=all&sort=beerid&ord=desc&view=text")
html_data = BeautifulSoup(html, 'html.parser')

	#### Get beer Data ####
beer_data_list = get_beer_data(html_data)

	##### Converting into dataframe####

beer_df = pd.DataFrame(beer_data_list)

	####### Cleaning Beer Data ########
beer_df['abv'] = beer_df['abv'].apply(clean_abv)	
beer_df['ibu'] = beer_df['ibu'].apply(str_to_int)
beer_df = beer_df.rename(columns={'size':'size(oz)'})
beer_df['size(oz)'] = beer_df['size(oz)'].apply(strip_oz)

	##### Write data to csv ###### 
beer_df.to_csv('beer.csv', sep=',')
print ('Done.')

