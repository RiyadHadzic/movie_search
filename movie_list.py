from requests_html import HTMLSession

session = HTMLSession()

mainHTML = session.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

mainHTML = mainHTML.html.html

twofifty = mainHTML.count('<a href="/title/')

if (twofifty/2)!=250:
	print('this script is not reliable anymore')
	sys.exit()
else:
	print('parsing..')

count=0
discard=0

movie=[]

for x in range(0,len(mainHTML)-15):
	if mainHTML[x]=='<' and mainHTML[x+1]=='a' \
	and mainHTML[x+2]==' ' and mainHTML[x+3]=='h'\
	and mainHTML[x+4]=='r' and mainHTML[x+5]=='e'\
	and mainHTML[x+6]=='f' and mainHTML[x+7]=='='\
	and mainHTML[x+8]=='"' and mainHTML[x+9]=='/'\
	and mainHTML[x+10]=='t' and mainHTML[x+11]=='i'\
	and mainHTML[x+12]=='t' and mainHTML[x+13]=='l'\
	and mainHTML[x+14]=='e' and mainHTML[x+15]=='/':
		if discard%2==0:
			unique=''
			for y in range (x+16,len(mainHTML)-15):
				if mainHTML[y]=='/':
					break
				unique=unique+mainHTML[y]
			movie.append(unique)
			discard=discard+1
		else:
			discard=discard+1


movieData=[]
movies=[]
count=0
for x in movie:
	secondHTML=session.get('https://www.imdb.com/title/'+x)
	secondHTML=secondHTML.html.html
	
	title=''
	year=''
	rating=''
	genre=''
	index=0
	done=False
	genres=[]

	while done==False:
		if secondHTML[index]=='t' and secondHTML[index+1]=='i'\
		and secondHTML[index+2]=='t':
			index=index+6
			done==True
			break
		index=index+1	
	while secondHTML[index]!='(':
		title=title+secondHTML[index]
		index=index+1
	title=title.rstrip()
	index=index+1
	while secondHTML[index]!=')':
		year=year+secondHTML[index]
		index=index+1
	year=int(year)
	done=False
	oneortwo=0
	while done==False:
		if secondHTML[index]+secondHTML[index+1]\
		+secondHTML[index+2]+secondHTML[index+3]\
		+secondHTML[index+4]+secondHTML[index+5]\
		+secondHTML[index+6]+secondHTML[index+7]\
		+secondHTML[index+8]+secondHTML[index+9]\
		+secondHTML[index+10]+secondHTML[index+11]\
		+secondHTML[index+12]+secondHTML[index+13]\
		+secondHTML[index+14]=='aggregateRating':
			index=index+14
			while done==False:
				if secondHTML[index]+secondHTML[index+1]\
				+secondHTML[index+2]+secondHTML[index+3]\
				+secondHTML[index+4]+secondHTML[index+5]\
				+secondHTML[index+6]+secondHTML[index+7]\
				+secondHTML[index+8]+secondHTML[index+9]\
				+secondHTML[index+10]=='ratingValue':
					index=index+13
					if secondHTML[index+1]!='.':
						rating=secondHTML[index]
						rating=float(rating)
						break
					rating=secondHTML[index]+\
					secondHTML[index+1]+secondHTML[index+2]
					rating=float(rating)
					break
				index=index+1
			break
		index=index+1


	while secondHTML[index]+secondHTML[index+1]\
		+secondHTML[index+2]+secondHTML[index+3]\
		+secondHTML[index+4]!='genre':
		index=index+1
	while secondHTML[index]!='[':
		index=index+1
	while secondHTML[index]!=']':
		genre=genre+secondHTML[index]
		index=index+1
	genre=genre.replace('[','')
	genre=genre.replace(']','')
	genre=genre.replace('"','')
	genre=genre.replace(',',' ')
	
	genres=genres+genre.split(' ')

	movieData.extend((title,rating,year,genres))
	movies.append(movieData)
	movieData=[]

f = open('movielist.txt','w')
f.write(str(movies))
f.close





	



