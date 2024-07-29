#zob
#des que ca baisse bcp il te dit BAM faut acheter
#zob

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

url='https://coinmarketcap.com/fr/currencies/ethereum/'
last=0
while True:
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    value=soup.find("span",{"class":"sc-65e7f566-0 clvjgF base-text"})
    value=value.get_text()
    r_value=str(value)
    r_value=r_value.replace("USD","")
    r_value=r_value.replace("$","")
    r_value=r_value.replace("€","")
    r_value=r_value.replace(",","")
    r_value_float=float(r_value)
    if last!=0 and last!=r_value:
        print('différence')
    print(r_value)
    last=r_value
    #print(r_value_float)
    date=datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    filedate=open(f"v/{date}.txt","w+")
    filelast=open(f"v/last.txt","w+")
    filedate.write(r_value)
    filelast.write(r_value)
    filedate.close()
    filelast.close()