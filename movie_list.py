from requests_html import HTMLSession
from movie_fns import *
import sys

mainHTML=htmlstring('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

#if their arent 250 unique movies, this script
#is not reliable anymore
if two_fifty_check(mainHTML,'<a href="/title/')==-1:
	print('this script is not reliable anymore')
	sys.exit()
else:
	print('parsing..')

#get a list of the movie urls
movie=movie_urls(mainHTML)
movies=movie_info(movie)
print(movies)


"""
f = open('movielist.txt','w')
f.write(str(movies))
f.close

"""




	



