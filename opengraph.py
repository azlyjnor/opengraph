import argparse, urllib.request
from newspaper import Article
from bs4 import BeautifulSoup

# parse user inputed url as an argument
parser = argparse.ArgumentParser()
parser.add_argument('-u',action='store',dest='url',default=None,help='Specify your URL. Eg. -u http://example.com',required=True)

results = parser.parse_args()

url = results.url

# fake user agent to bypass web filters
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = {'User-Agent': user_agent}

# get article body, authors, text and date
# article.top_image  // i'm using og:image instead but either one is fine.
article = Article(url)
article.download()
article.parse()
article.publish_date # depends on web structure. some won't show.
article.authors
article.text

#additional code for opengraph extraction
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html = response.read()
soup = BeautifulSoup(html, 'lxml')

title = soup.find('meta', property='og:title')['content']
desc = soup.find('meta', property='og:description')['content']
url = soup.find('meta', property='og:url')['content']
img = soup.find('meta', property='og:image')['content']

print(
"Title:",' ',title,'\n',
"Description:",' ',desc,'\n',
"Url:",' ',url,'\n',
"Featured Image:",' ',img,'\n',
"Author(s):",' ',article.authors,'\n',
sep=''
)

print (article.text)
