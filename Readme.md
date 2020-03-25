Web Scraping

Web Scraping data from a Table in Web Page using python 

In this article, we are going to extract data from the table in a website
(<https://www.worldometers.info/coronavirus/>)  and store it into a CSV or JSON
and visualize using D3.js

What is web scraping?

In simple terms, it is the process of gathering information or data from
different webpages (HTML sources). The information or data thus gathered can be
used in building datasets or databases for different applications like (Data
Analysis, Building a price comparison application, etc.  )

Prerequisite:- 

1.  Basic understanding of Python 3.0 programming.

2.  Python 3.0 or above installed in your pc(Don’t forget to ADD python to the
    path while installing).

Libraries we are using:-

1.  BeautifulSoup.

2.  Pandas.

3.  Requests.

The following are the steps to proceed with the project.

Step-1:-  Creating the Virtualenv( Same for Windows and Linux ).

Creating the Virtualenv enables us to make our project independent (we install
all the libraries required for this project into this Virtualenv.)

1.  \#Upgrading pip  

2.  python -m pip install --upgrade pip  

3.  \#installing Virtalenv  

4.  pip install virtualenv  

5.  \#creating Virtualenv   

virtualenv [Name of environment] \#enter the name of env without [].  

1.  virtualenv env 

Step-2:- Activating the Virtualenv and installing the required libraries.

Windows:-

If required 

( Open Windows PowerShell as administrator and ‘Set Access for activating env in
PowerShell window By below command’.

  Set-ExecutionPolicy RemoteSigned )

Now to activate the env :- 

env/Scripts/activate  

![https://lh6.googleusercontent.com/AbU597LrgXm1rao3V9L-678A9b2_b2HMDPpTuoJpoGH-gi9oL-_RlPevVSZXn-MfjHdh3KlWsVgJHrwH5zChin-_zne0dnofzMJWH6ot1VLTz7eP5NQaj1E5L6Blo5xpi9axUSA](media/7a646b5e5dfed2d650a9a24280f055bc.png)

Now if the env is activated you will See (env) at the beginning of the next
line. 

**In Linux(env/bin/activate)   **

Installing Required  Libraries :-

1.  \#installing BeautifulSoup  

2.  pip install bs4  

3.  \#installing pandas.  

4.  pip install pandas   

5.  \#installing requests.  

6.  pip install requests   

It is always best practice to freeze required libraries to requirements.txt

>   pip freeze \> requirements.txt

![](media/31155605592d95e3bb6cc4f8a569a89c.png)

Step 3:- Open web page and navigate to the table you want to collect data from
\> right click \> click on Inspect.

![](media/ec3812ad514f2332555f487ffe6a7b4c.png)

u

understand the html structure now.

Step 4:- now procced with the program .

1.  \#importing libraries   

2.  **from** bs4 **import** BeautifulSoup  

3.  **import** requests  

4.  **import** pandas as pd  

5.  \#creating function   

6.  **def** getPageSource():  

7.      \# goto to url   

8.      url=requests.get("https://www.worldometers.info/coronavirus/")  

9.      \#get the html page   

10.     soup =BeautifulSoup(url.content)  

11.     \#Navigating to table you want.   

12.     table=soup.find("table", attrs={'id' : 'main_table_countries_today'})  

13.     rows=table.tbody.findAll('tr')  

14.     \#creating empty lists to store data   

15.     countries=[]  

16.     Old_cases=[]  

17.     New_cases=[]  

18.     Old_Deaths=[]  

19.     New_Deaths=[]  

20.     Total_recovered=[]  

21.     Active_cases=[]  

22.     \#scraping the data from each row of the table and storing into lists   

23.     **for** row **in** rows:  

24.         country = row.findAll('td')[0].text  

25.         Old_case = row.findAll('td')[1].text  

26.         New_case = row.findAll('td')[2].text  

27.         Old_Death = row.findAll('td')[3].text  

28.         New_Death = row.findAll('td')[4].text  

29.         recovered = row.findAll('td')[5].text  

30.         Active_case = row.findAll('td')[6].text  

31.         countries.append(country)  

32.         Old_cases.append(Old_case)  

33.         New_cases.append(New_case)  

34.         Old_Deaths.append(Old_Death)  

35.         New_Deaths.append(New_Death)  

36.         Total_recovered.append(recovered)  

37.         Active_cases.append(Active_case)  

38.     \#Creating the pandas DataFrame from lists   

39.     df = pd.DataFrame({'countries':countries,'Old_cases': Old_cases,'New_cases':New_cases,'Old_Deaths':Old_Deaths,'New_Deaths':New_Deaths,'Total_recovered':Total_recovered,'Active_cases':Active_cases})  

40.     \#replacing all the characters except digits with empty.  

41.     df['New_cases'].replace(regex=True,inplace=True,to_replace=r'\\D',value=r'')  

42.     df['New_Deaths'].replace(regex=True,inplace=True,to_replace=r'\\D',value=r'')  

43.     df['Old_cases'].replace(regex=True,inplace=True,to_replace=r'\\D',value=r'')  

44.     df['Old_Deaths'].replace(regex=True,inplace=True,to_replace=r'\\D',value=r'')  

45.     df['Total_recovered'].replace(regex=True,inplace=True,to_replace=r'\\D',value=r'')  

46.     df['Active_cases'].replace(regex=True,inplace=True,to_replace=r'\\D',value=r'')  

47.     \#Convering all the columns to numeric   

48.     df['New_cases']= pd.to_numeric(df['New_cases'])  

49.     df['Old_cases']= pd.to_numeric(df['Old_cases'])  

50.     df['New_Deaths']= pd.to_numeric(df['New_Deaths'])  

51.     df['Old_Deaths']= pd.to_numeric(df['Old_Deaths'])  

52.     df['Total_recovered']= pd.to_numeric(df['Total_recovered'])  

53.     df['Active_cases']= pd.to_numeric(df['Active_cases'])  

54.     \#filling NAN/None by Zeros   

55.     newdf=df.fillna(0)  

56.     \#naming the index column   

57.     newdf.index.name = 'Sl_No'  

58.     \#adding two columns of the dataframe   

59.     newdf['Total_cases']=newdf['Old_cases'] + newdf['New_cases']  

60.     newdf['Total_Deaths']=newdf['Old_Deaths'] + newdf['New_Deaths']  

61.     \#creating new dataframe with required columns   

62.     Data=newdf[['countries','Total_cases','Total_Deaths','Total_recovered','Active_cases']]  

63.     \#Saving data to csv    

64.     Data.to_csv('../Data.csv')  

65.     \#saving data in json format   

66.     Data.to_json('../Data.json',orient='records')  

67.     \#opening the D3.js chart html   

68.     html_file = open('../Chart.html', 'r')  

69.     \#reading its content   

70.     html_content = html_file.read()  

71.     \#coping text to temp vairable   

72.     replacecont=html_content  

73.     \#opening the json data file.  

74.     json_file = open('../Data.json','r')  

75.     \#reading the data from json file   

76.     json_content = json_file.read( )  

77.     \#replacing the string record in html   

78.     newrec=replacecont.replace('record',json_content)  

79.     \#Update new html with data to visiulize   

80.     update_html=open('../Chart2.html', 'w')  

81.     update_html.write(newrec)  

82.     \#empty the varibale and close the documents   

83.     replacecont=" "  

84.     update_html.close()  

85.     html_file.close()  

86. getPageSource()  
