from bs4 import BeautifulSoup
import requests
import pandas as pd

def getPageSource():

    url=requests.get("https://www.worldometers.info/coronavirus/")
    soup =BeautifulSoup(url.content)
    table=soup.find("table", attrs={'id' : 'main_table_countries_today'})
    rows=table.tbody.findAll('tr')
    countries=[]
    Old_cases=[]
    New_cases=[]
    Old_Deaths=[]
    New_Deaths=[]
    Total_recovered=[]
    Active_cases=[]
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
    df = pd.DataFrame({'countries':countries,'Old_cases': Old_cases,'New_cases':New_cases,'Old_Deaths':Old_Deaths,'New_Deaths':New_Deaths,'Total_recovered':Total_recovered,'Active_cases':Active_cases})
    df['New_cases'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['New_Deaths'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['Old_cases'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['Old_Deaths'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['Total_recovered'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['Active_cases'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
    df['New_cases']= pd.to_numeric(df['New_cases'])
    df['Old_cases']= pd.to_numeric(df['Old_cases'])
    df['New_Deaths']= pd.to_numeric(df['New_Deaths'])
    df['Old_Deaths']= pd.to_numeric(df['Old_Deaths'])
    df['Total_recovered']= pd.to_numeric(df['Total_recovered'])
    df['Active_cases']= pd.to_numeric(df['Active_cases'])
    newdf=df.fillna(0)
    newdf.index.name = 'Sl_No'
    newdf['Total_cases']=newdf['Old_cases'] + newdf['New_cases']
    newdf['Total_Deaths']=newdf['Old_Deaths'] + newdf['New_Deaths']
    Data=newdf[['countries','Total_cases','Total_Deaths','Total_recovered','Active_cases']]
    Data.to_json('E:\Office Python Project\Data.json',orient='records')
    html_file = open('E:\Office Python Project\Chart.html', 'r')
    html_content = html_file.read()
    json_file = open('E:\Office Python Project\Data.json','r')
    json_content = json_file.read( )
    newrec=html_content.replace('record',json_content)
    
    new_html=open('E:\Office Python Project\Chart.html', 'w')
    new_html.write(newrec)
    new_html.close()
    html_file.close()

getPageSource()
