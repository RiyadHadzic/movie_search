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
			movie.append('http://www.imdb.com/title/'+url)

			leftindex=hstring[:x:]

			hstring=hstring[x::]

		else:
			discard=discard+1
			leftindex=hstring.find('<a href="/title/') +\
			len('<a href="/title/')
			hstring=hstring[leftindex::]
	return movie

def movie_info(movieurl):
	movies=[]
	for x in movieurl:
		moviehtml=htmlstring(x)
		movie=[]
		movie.append(get_title(moviehtml))
		movies.append(movie)
	return movies

def get_title(moviestring):
	leftindex=moviestring.find('"name"')
	leftindex=leftindex+len('"name"')
	moviestring=moviestring[leftindex::]
	leftindex=moviestring.find('"')
	moviestring=moviestring[leftindex::]
	x=moviestring.find('"')
	title=moviestring[:x-1:]
	return title

