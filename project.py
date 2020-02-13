import requests
from bs4 import BeautifulSoup
import pandas as pd
num_1=int(input())
num_2=int(input())
name=[]
seat=[]
degree=[]
Arranging=[]
for i in range(num_1,num_2):
    URL  = 'https://www.natiga4dk.net/dakahlia/?type=num&k={0}&trteeb=t'.format(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results=soup.find_all("td")
    a=results[0].text
    b=results[1].text
    c=results[4].text
    d=results[8].text
    name.append(a)
    seat.append(b)
    degree.append(c)
    Arranging.append(d)
df = pd.DataFrame({'اسم الطالب':name , 'رقم الجلوس':seat ,'المجموع':degree , 'الترتيب على المدرسة':Arranging })
export_csv = df.to_csv (r'/home/osama/export_dataframe.csv', index = None, header=True)
