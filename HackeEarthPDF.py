from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import pdfkit

class Hackerearth(object):
	
	def __init__(self):
		print('Starting the process...')
		self.count = 0
		self.url = 'https://www.hackerearth.com'
		self.rel = '<link rel="stylesheet" href="style.css" />'
		self.ua = UserAgent()
		self.header = {'user-agent':self.ua.chrome}
		self.tutorialType = ['https://www.hackerearth.com/practice/basic-programming' # Basic Programming
		                    ,'https://www.hackerearth.com/practice/data-structures' # Data Strcutre
		                    ,'https://www.hackerearth.com/practice/algorithms' # Algorithm
		                    ,'https://www.hackerearth.com/practice/math' #Mathematics
		                    ]


	def getwebPageCode(self,link,retry=2):
		if retry == 0:
			return None
		try:
			response = requests.get(link,headers=self.header)
			if 500<=response.status_code<600:
				return getwebPageCode(link,retry-1)
			return response.content	
		except:
			return None	


	def initPage(self,link):
		self.pageCode = hackerearthObj.getwebPageCode(link)		
		
		if self.pageCode == None:
			return 0

		else:

			self.soup = BeautifulSoup(self.pageCode,'lxml')
		
			linkObj = self.soup.findAll('a',{'class':'block dark no-underline left-nav-link ellipsis'},href=True)

			self.allTutLink = []

			for item in linkObj:
				self.allTutLink.append(item['href'])

			return 1


	def getDataFromPage(self,filename):
	
		htmlCode = self.rel+'\n'


		for link in self.allTutLink:

			print('\nParsing page '+str(self.count))

			page = self.getwebPageCode(self.url+link)

			soup = BeautifulSoup(page,'lxml')

			head = soup.find('h1',{'class':'dark no-margin larger-24 weight-600'})

			headStr = str(head)

			htmlCode = htmlCode + headStr + '\n'

			body = soup.find('div',{'class':'right-section-content darker regular tutorial'}) 

			bodyStr = str(body)

			bodyStr = bodyStr.replace('$$','')

			bodyStr = bodyStr.replace('\le','')			

			htmlCode = htmlCode + bodyStr + '\n'

			htmlCode = htmlCode + '<br/><br/><br/><br/><hr/>'

			print('Done')

			self.count += 1

		with open('htmlf.html','w') as f:
			f.write(htmlCode)	

		pdfkit.from_url('htmlf.html',filename)	

		print('Book created : '+filename+'\n\n')


	def __des__(self):
		print('Ending the process...')



if __name__ == '__main__':
	
	hackerearthObj = Hackerearth()
	
	try:
		for link in hackerearthObj.tutorialType:
			if hackerearthObj.initPage(link):
				linkstr = str(link)
				#print(linkstr[linkstr.rfind(r'/')+1:len(linkstr)])
				hackerearthObj.getDataFromPage(linkstr[linkstr.rfind(r'/')+1:len(linkstr)]+'.pdf' )
			else:
				print('Unable to parse')	

	except Exception as e:
		print('Following problem arise :')
		print(str(e))

	finally:
		hackerearthObj.__des__()	
