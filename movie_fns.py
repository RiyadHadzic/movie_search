from requests_html import HTMLSession

#returns a string of the HTML code for a given url
def htmlstring(url):
	session=HTMLSession()
	htmlString=session.get(url)
	htmlString=htmlString.html.html
	return htmlString

#check if there are 250 unique entires
def two_fifty_check(hstring,check):
	twofifty=hstring.count(check)
	if (twofifty/2)!=250:
		return -1
	else:
		return 1

#this fn gives url of all movies
def movie_urls(hstring):
	discard=0
	count=500
	movie=[]
	for x in range(0,count):
		if discard%2==0:
			discard=discard+1

			#get a new hstring starting at the 
			#the first position of the part of the
			#URL that identifies a specific movie
			leftindex=hstring.find('<a href="/title/')
			hstring=hstring[leftindex::]
			leftindex=len('<a href="/title/')
			hstring=hstring[leftindex::]

			#get the very last characted of the part
			#of the URL that identifies a specific movie
			x=hstring.find('/')
			url=hstring[:x:]

			#append unique URL
			movie.append('https://www.imdb.com/title/'+url)

			leftindex=hstring[:x:]

			hstring=hstring[x::]

		else:
			discard=discard+1
			leftindex=hstring.find('<a href="/title/') +\
			len('<a href="/title/')
			hstring=hstring[leftindex::]
	return movie

def get_title(moviestring):
	leftindex=moviestring.find('<title>')
	leftindex=leftindex+len('<title>')
	moviestring=moviestring[leftindex::]
	leftindex=moviestring.find('(')

	title=moviestring[:leftindex:]
	title.rstrip()
	return title

def movie_info(movieurl):
	movies=[]
	for x in movieurl:
		moviehtml=htmlstring(x)
		movie=[]
		movie.append(get_title(moviehtml))
		movies.append(movie)
	return movies
