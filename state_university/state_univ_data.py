import re
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

def get_state(html_soup) :
	data = html_soup.findAll('h2')
	data = data[:len(data)-1]
	data = data[:len(data)-1]
	data = data[1:]
	state_array = []
	for dt in data :
		val = re.search(r'\[edit\]',dt.text)
		if(val) :
		    state_array.append(dt.text.split('[edit]')[0])
	return state_array


def get_state_wise_university_list(html_soup,state_array) :
	data = html_soup.findAll('h2')
	data = data[:len(data)-1]
	data = data[:len(data)-1]
	data = data[1:]
	state_array = []
	for dt in data :
		val = re.search(r'\[edit\]',dt.text)
		if(val) :
		    state_array.append(dt.text.split('[edit]')[0])
		    
	cont1 = html_soup.body('div',{'id' : 'content'})
	cont= cont1[0]
	cont2 = cont('div',{'id' : "bodyContent"})
	cont = cont2[0]
	cont3 = cont('div',{'id' : "mw-content-text"})
	cont = cont3[0]

	contu = cont.findAll('ul')
	val = 5
	i=0
	count =0
	stt_uni_list = []
	while (val<153) :
		contu1 = contu[val]
		contu2 = contu1('li')
		for ix in contu2 :
		    stt_uni = {
		        "state":state_array[count] ,
		        "University":ix.text
		    }
		    stt_uni_list.append(stt_uni)
		
		i = len(contu1('ul'))
		val = i+val+1
		if (val==110) :
		    count = count
		else :
		    count = count +1
	return stt_uni_list ;
	
	
    #### This Function drop repeated university list from dataframe #####
def drop_func(x) :
    val = re.search(r'\n\n',x)
    if(val) :
        return True
    else :
        return False

    #### This Function Clean and extract University between parentheses #####
def clear_row(x) :
    if (re.search(r'\(\(([A-Za-z0-9_ ]+)\)\)',x)) :
        val = re.search(r'\(\(([A-Za-z0-9_ ]+)\)\)',x).group(1)
        return val
    elif(re.search(r'\(',x)) :
        val = x.split('(')[0]
        return val
    else :
        return x

	
	### Reading Url ####	
html = urlopen("https://en.wikipedia.org/wiki/List_of_state_universities_in_the_United_States")
html_soup = BeautifulSoup(html, 'html.parser')

	#### Get state university Data ####
state_array = get_state(html_soup)
stt_uni_list = get_state_wise_university_list(html_soup ,state_array)
	##### Converting into dataframe####

state_df = pd.DataFrame(stt_uni_list)

	##### Cleaning of dataframe####
	
state_df = state_df[(state_df['University'].apply(drop_func))==False]	
state_df['University'] = state_df['University'].apply(clear_row)

	##### Write data to csv ###### 
state_df.to_csv('state_university.csv', sep=',')
print ('Done.')

