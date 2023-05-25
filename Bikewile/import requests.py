import requests
from bs4 import BeautifulSoup
import csv


url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)# requesting access to get the html text


soup=BeautifulSoup(page.content,'html.parser') # we want the content so using it
print(soup.prettify)
#print(soup.text)
#images scraping
img1=[]
image=soup.findAll('div',class_="imageWrapper")
#print(image)
for i in image:
    j=i.img['src']#source of image location.
    img1.append(j)
    print(img1)
#we got images now to store in '''
#links
'''links=[]
link=soup.findAll('div',class_='bikeDescWrapper')
print(link)
for i in link:
    j= i.a['href']
    links.append(j)
print(links)'''

#text
'''links=[]
link=soup.findAll('div',class_='bikeDescWrapper')
print(link)
for i in link:
    j= i.a.text
    links.append(j)
print(links)'''

#using csv we have to store the data
with open('il.csv','w')as csv_file:
    write=csv.writer(csv_file)
    write.writerow(image)
    for i in image:
        j=i.img['src']#source of image location.
        img1.append(j)
    write.writerow(img1)
































