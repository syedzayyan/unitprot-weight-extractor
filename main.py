import requests
from bs4 import BeautifulSoup

URL = "https://www.uniprot.org/uniprot/"
#  This is a list of proteins I needed/need. You can do whatever you want
someList = ["Q99460","P08865" ,"P10809" ,"V9HWB4" ,"P25054" ,"Q8N957" ,"P07355" ,"P25705" ,"P46063" ,"Q9NVP1" ,"Q4LE39" ,"Q562R1" ,"Q01850","Q9NZA1","O14578","Q16630","A0A0D9SEJ5","P17661","Q96JH7" ,"O75923","P68104","P14625" ,"O15083","O75822","P04406","P04899","P11142","P07900","P08238","P07910","Q6DN90" ,"O14782" ,"P02545","P02545" ,"P43243","P26038" ,"Q9UK51","Q6S8J3","Q15652" ,"Q15084","Q9P2E9","Q96E39","Q8N7X1","Q13523","P02768" ,"Q13838","Q15459","Q9UJZ1","P38646","Q9Y490","Q8NBS9","Q9NY65"]

print("Mass in KiloDaltons")

for x in someList:
  page = requests.get(URL + x)
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find("span", {'class':"sequence-field-header tooltiped", "title": "The mass of the unprocessed protein, in Daltons."}).next_sibling
  mass = int((results.text).replace(',', ''))
  mass_converted = mass / 1000
  print(x + ": " + str(mass_converted))

print("\nExit")