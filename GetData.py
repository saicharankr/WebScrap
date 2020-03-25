
#importing libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd

#creating function 
def getPageSource():

    # goto to url 
    url=requests.get("https://www.worldometers.info/coronavirus/")

    #get the html page 
    soup =BeautifulSoup(url.content)

    #Navigating to table you want. 
    table=soup.find("table", attrs={'id' : 'main_table_countries_today'})
    rows=table.tbody.findAll('tr')

    #creating empty lists to store data 
    countries=[]
    Old_cases=[]
    New_cases=[]
    Old_Deaths=[]
    New_Deaths=[]
    Total_recovered=[]
    Active_cases=[]

    #scraping the data from each row of the table and storing into lists 
    for row in rows:
        country = row.findAll('td')[0].text
        Old_case = row.findAll('td')[1].text
        New_case = row.findAll('td')[2].text
        Old_Death = row.findAll('td')[3].text
        New_Death = row.findAll('td')[4].text
        recovered = row.findAll('td')[5].text
        Active_case = row.findAll('td')[6].text
        countries.append(country)
        Old_cases.append(Old_case)
        New_cases.append(New_case)
        Old_Deaths.append(Old_Death)
        New_Deaths.append(New_Death)
        Total_recovered.append(recovered)
        Active_cases.append(Active_case)
    
    
    #Creating the pandas DataFrame from lists 
    df = pd.DataFrame({'countries':countries,'Old_cases': Old_cases,'New_cases':New_cases,'Old_Deaths':Old_Deaths,'New_Deaths':New_Deaths,'Total_recovered':Total_recovered,'Active_cases':Active_cases})
    
    #replacing all the characters except digits with empty.
    df['New_cases'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['New_Deaths'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['Old_cases'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['Old_Deaths'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['Total_recovered'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['Active_cases'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')

    #Convering all the columns to numeric 
    df['New_cases']= pd.to_numeric(df['New_cases'])
    df['Old_cases']= pd.to_numeric(df['Old_cases'])
    df['New_Deaths']= pd.to_numeric(df['New_Deaths'])
    df['Old_Deaths']= pd.to_numeric(df['Old_Deaths'])
    df['Total_recovered']= pd.to_numeric(df['Total_recovered'])
    df['Active_cases']= pd.to_numeric(df['Active_cases'])

    #filling NAN/None by Zeros 
    newdf=df.fillna(0)

    #naming the index column 
    newdf.index.name = 'Sl_No'

    #adding two columns of the dataframe 
    newdf['Total_cases']=newdf['Old_cases'] + newdf['New_cases']
    newdf['Total_Deaths']=newdf['Old_Deaths'] + newdf['New_Deaths']

    #creating new dataframe with required columns 
    Data=newdf[['countries','Total_cases','Total_Deaths','Total_recovered','Active_cases']]

    #Saving data to csv  
    Data.to_csv('../Data.csv')

    #saving data in json format 
    Data.to_json('../Data.json',orient='records')

    #opening the D3.js chart html 
    html_file = open('../Chart.html', 'r')

    #reading its content 
    html_content = html_file.read()

    #coping text to temp vairable 
    replacecont=html_content

    #opening the json data file.
    json_file = open('../Data.json','r')
    json_content = json_file.read( )
    newrec=replacecont.replace('record',json_content)
    replacecont=" "

    
    update_html=open('../Chart2.html', 'w')
    update_html.write(newrec)

    update_html.close()
    html_file.close()


getPageSource()
