# In[107]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install prettytable')


# In[65]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://presidentofindia.nic.in/former-presidents.htm')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6', 'p'])
print('List all the header tags :', *titles, sep='\n\n')


# In[43]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[44]:


from bs4 import BeautifulSoup
import requests


# In[45]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[46]:


page


# In[47]:


soup= BeautifulSoup(page.content)
soup


# In[75]:


team_name= soup.find_all('span', class_="u-hide-phablet")
team_name


# In[98]:


rankings= soup.find_all('tr',class_="table-body")
rankings


# In[99]:


content=soup.find_all('div', class_="rankings-block__container full rankings-table")


# In[103]:


content


# In[110]:


from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable


def Menu():
	print('\n1. Men \n2. Women\n')
	gen=Gender()
	print('\n1. Team Rankings \n2. Player Ranking\n')
	tp=TeamOrPlayer()
	
	mode=''
	val=''
	
	if gen=='mens':
		print('\n1. Test\n2. ODI\n3. T20\n')
		mode=Mode()

	if tp=='player-rankings':
		if mode=='':
			print('\n1. ODI\n2. T20\n')
			mode=Mode2()
		print('\n1. Batting\n2. Bowling\n3. All-Rounder\n')
		val=Value()
	
	return gen,tp,mode,val


def Gender():
	gender=input('Enter your choice:')
	code={'1':'mens','2':'womens'}

	if gender in code:
		return code[gender]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Gender();


def TeamOrPlayer():
	choice=input('Enter your choice:')
	tp={'1':'team-rankings','2':'player-rankings'}
	
	if choice in tp:
		return tp[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return TeamOrPlayer();

	
def Mode():
	choice=input('Enter your choice:')
	word={'1':'/test','2':'/odi','3':'/t20i'}
	
	if choice in word:
		return word[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Choice();


def Mode2():
	choice=input('Enter your choice:')
	word={'1':'/odi','2':'/t20i'}
	
	if choice in word:
		return word[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Choice();


def Value():
	choice=input('Enter your choice:')
	val={'1':'batting','2':'bowling','3':'all-rounder'}
	
	if choice in val:
		return val[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Value()


def URL():
	gen,tp,mode,val=Menu()
	url='https://www.icc-cricket.com/rankings/'+gen+'/'+tp+mode+'/'+val
	header=gen.upper() +' ' +mode[1:].upper() + ' ' + val.upper()
	print('\n{:<15}  {:<30}\n{:<15}  {:<30}'.format('',tp.upper(),'',header))
	return url,tp


def SOUP(url,tp):
	try:
		res=requests.get(url)
		soup=BeautifulSoup(res.text,'lxml')
		a= soup.find_all('tr',{'class':'table-body'})
		data={}
			
		for i in a :
			team=[]
			name=''
			rating=''

			try:
				rank=int(i.contents[1].text)
			except:
				pass
			
			try:	
				name=i.contents[3].text.replace('\n','')
				name=" ".join(name.split())
				if rank==1 and tp=='player-rankings':
					name=name[0:-3]
			except:
				pass

			try:
				rating=i.contents[9].text
			except:
				if rank==1 :
					rating=i.contents[5].text
				else:
					rating=i.contents[7].text
			
			team.extend([name,rating])
			data[rank]=team
		
		return data

	except:
		return SOUP(url,tp)


def Print(data):
	print('\nRANKING \t TEAM\t\t\t\tRATING')
	for i in sorted(data):
		print('{:<10}       '.format(i),end='')
		for j in range(len(data[i])):
			print('{:<26}'.format(data[i][j]),end='     ')
		print()


def main():
	
	url,tp=URL()
	data=SOUP(url,tp)
	Print(data)	


if __name__=='__main__':
	main()


# In[113]:


from bs4 import BeautifulSoup
import requests


# In[114]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[115]:


page


# In[116]:


soup= BeautifulSoup(page.content)
soup


# In[126]:


paper= soup.find_all('a', class_="sc-5smygv-0 fIXTHm")
paper


# In[123]:


author=soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO")
author


# In[124]:


date=soup.find_all('span', class_="sc-1thf9ly-2 dvggWt")
date


# In[129]:


title=soup.find_all('h2', class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")
title


# In[169]:


import pandas as pd
df = pd.DataFrame({'Paper Title':title, 'Author':author, 'Published Date': date, 'Paper URL': paper})
df


# In[133]:


from bs4 import BeautifulSoup
import requests


# In[213]:


page=requests.get('https://www.cnbc.com/world/?region=world')
page


# In[242]:


soup= BeautifulSoup(page.content)
soup


# In[253]:


links=soup.find_all('div', class_="RiverThumbnail-imageThumbnail")
links


# In[252]:


headlines = soup.find_all('div', class_="RiverHeadline-headline RiverHeadline-hasThumbnail")
headlines


# In[230]:


time= soup.find_all('div',class_="ArticleHeader-time")
time


# In[251]:


print (len(headlines),len(links))


# In[254]:


import pandas as pd
df = pd.DataFrame({'Headline':headlines,'Links': links})
df


# In[255]:


from bs4 import BeautifulSoup
import requests


# In[256]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[257]:


page


# In[258]:


soup= BeautifulSoup(page.content)
soup


# In[271]:


name=[]
for i in soup.find_all('a', class_="restnt-name ellipsis"):
    name.append(i.text)
name


# In[270]:


loc=[]
for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    loc.append(i.text)
loc


# In[273]:


price=[]
for i in soup.find_all('span', class_="double-line-ellipsis"):
    price.append(i.text.split('|')[0])
price


# In[277]:


image=[]
for i in soup.find_all('img', class_="no-img"):
    image.append(i.get('data-src'))
image


# In[278]:


rating=[]
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[306]:


cuisine=[]
for i in soup.find_all('span', class_="double-line-ellipsis"):
    cuisine.append(i.text[25:45])
cuisine


# In[307]:


print (len(name),len(loc), len(price), len(image),len(rating),len(cuisine))


# In[308]:


import pandas as pd
df = pd.DataFrame({'Restaurant name':name, 'Cuisine':cuisine, 'Location': loc, 'Ratings': rating, 'Image URL':image})
df


# In[ ]:




