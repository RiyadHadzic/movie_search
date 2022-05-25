The project inside of the folder movie_project_Riyad is 
suppose to display knowledge of the following:

1. Creating a script to gather information from a webpages HTML
source code and appending that data to a txt file in a format that
is simple.

2. using SQL and python to display infomation on a webpage given a 
users request.

The point of this project is not to show knowledge of front-end,CSS,
or JavaScript. Meaning, the website is very simple and possbily 
visually unappealing to some users. The point of the website is 
1 and 2 listed above.Due to a lack of time, I have ignored these 
things that are besides the point,but I can learn them upon request. 

Movie information is parsed by a Python script parse.py
from https://www.imdb.com/chart/top/?ref_=nv_mv_250

this script is reliable as of 5/5/2022. It may not be reliable
later. No tests have been written to ensure reliablity. Incase 
changes are made to the above link that would render this script
as insufficient, screenshots are taken to prove to employers that 
the script was once reliable. 

I did not use concurrency in this script, thus the script runs 
slowly. I did not time it but I estimate it took less than 
5 minutes to gather all of the data. Looking back, I would
implement concurrency to make the script faster.

Script does the following, in order:
1.determines a movie from the imbd.com url above.
2.Because the majority of movie information is not available in the 
above link, script then opens a seperate page with the totality
of movie information and appends it to a file movieinfo.txt

Movie format that will be appended to movieinfo.txt:
TITLE;Rating;Year;Genre1,Genre2,Genre3,...Genre_N;Duration

To run the script, in your environment type the following 
command:

'python -m pip install requests'



The following key will be used to search for the next movie:
'<a href="/title/' 
at the URL https://www.imdb.com/chart/top/?ref_=nv_mv_250

