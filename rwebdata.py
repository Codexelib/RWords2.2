# =========================packages and modules=========================

from bs4 import BeautifulSoup
import requests
import os

#os.system('clear')

def ClearList(list):
	list.remove('GenerateRandomWords')
	list.remove('Words')
	list.remove('Tweet')
	list.remove('')
	list.remove('')
	list.remove('RandomWord')
	list.remove('AllWords')

kelimeler = []
database = []

# =========================get html content=========================

pages = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for page in pages:
	r = requests.get('https://randomword.com/words/' + page + '.html')
	""" print(r.content) indentleri ayarlanmamis sayfa """ 
	soup = BeautifulSoup(r.content, features="lxml")
	""" print(soup.prettify()) indent ayarlanmis sayfa """

# =========================clear tags & escape blocks=========================


	kelimeKaynak = soup.find_all('li')
	for kelimeK in kelimeKaynak:
		text = kelimeK.text
		edited1 = text.replace('\n','')
		edited2 = edited1.replace('\t','')
		edited3 = edited2.replace(' ','')
		kelimeler.append(edited3)

# =========================clear unused indexs=========================

	ClearList(kelimeler)
	for kelime in kelimeler:
		database.append(kelime)      
		

