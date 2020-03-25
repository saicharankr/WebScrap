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

https://lh6.googleusercontent.com/AbU597LrgXm1rao3V9L-678A9b2_b2HMDPpTuoJpoGH-gi9oL-_RlPevVSZXn-MfjHdh3KlWsVgJHrwH5zChin-_zne0dnofzMJWH6ot1VLTz7eP5NQaj1E5L6Blo5xpi9axUSA

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

understand the html structure now.
