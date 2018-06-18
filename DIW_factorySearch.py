import requests
from bs4 import BeautifulSoup

url = 'http://userdb.diw.go.th/results1.asp'
fname = 'data.html'

start_page = 1
end_page =  2 
all_page = end_page


def checkData(fclass):
	
	payload = {'CLASS':fclass,'pageno':'1'}
	r = requests.post(url, data=payload)
	#soup = BeautifulSoup(r.text,"html.parser",from_encoding="windows-874")
	soup = BeautifulSoup(r.text, "html.parser")
	form_data = soup.find_all("form")	
	pages = form_data[0].find_all("input")
	all_page = len(pages) - 9
	end_page = all_page

	
	return all_page;

def selectTr(table,fileName,start_rows):
	rows = table.find_all("tr")
	for row in range(start_rows,len(rows)):
		fileName.write(str(rows[row]))

def loadData(fclass,pno,fileName):
	payload = {'CLASS':fclass, 'pageno':pno} #'ISIC_CODE':'1311'
	r = requests.post(url, data=payload)
	soup = BeautifulSoup(r.text, "html.parser")
	dataList = soup.find_all("table")
	if (pno == 1):
		selectTr(dataList[0], fileName,0)
	else :
		selectTr(dataList[0], fileName,1)	

def start_program():
	fclass = input('INPUT TYPE OF FACTORY (\'022\') :')
	end_page = checkData(fclass)
	print ('There are %s  pages' % end_page)
	new_file = open(fclass + fname,'w')
	new_file.write('<table  border=1 cellspacing=0 cellpadding=3 width=95%>')
	for i in range(start_page,end_page + 1):
		print ('Generating page no : %s' % i)	
		loadData(fclass, i, new_file)
	new_file.write('</table>')
	new_file.close()
	print("got file :" + fclass+fname )	
	input('completed !.')

start_program()
