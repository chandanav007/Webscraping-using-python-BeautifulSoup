import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name= []
Prices =[]
Description=[]
Reviews=[]
for i in range(2,20):
    url="https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as= "+ str(i)

    r=requests.get(url)
#print(r)

    soup=BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")

    names=box.find_all("div",class_="_4rR01T")
#print(names)
    for i in names:
        name = i.text
        Product_name.append(name)

    print(Product_name)
#print(len(Product_name))

    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Prices.append(name)

#print(Prices)
#print(len(Prices))

    desc =box.find_all("ul",class_="_1xgFaf")


    for i in desc:
        name=i.text
        Description.append(name)

#print(Description)

    reviews =box.find_all("div",class_="_3LWZlK")

    for i in reviews:
        name=i.text
        Reviews.append(name)

#print(Reviews)
#print(len(Reviews))

df= pd.DataFrame({"Product Name": Product_name,"Prices": Prices, "Description":Description,"Reviews":Reviews})
print(df)

df.to_csv("C:/Users/chandana/Desktop/Webscraping Projects using Python/Flipkart_mbiles_under_500001.csv")