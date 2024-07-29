import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
url='https://crypto.com/price/ethereum'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
value=soup.find("span",{"class":"css-13hqrwd"})
value=value.get_text()
r_value=str(value)
r_value=r_value.replace("USD","")
r_value=r_value.replace("$","")
r_value=r_value.replace(",","")
r_value_float=float(r_value)
print(r_value_float)
print(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
file=open("v/v.txt","w")