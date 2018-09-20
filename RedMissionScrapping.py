import bs4
import requests

res = requests.get('https://www.thegoldenbugs.com/blog')
soup = bs4.BeautifulSoup(res.text,'lxml')
#select the tag that contains the blog I want to scrap
blog = soup.select('pre')
text = blog[0]
blog_text = text.contents[0]
blog_lines = blog_text.split('-----')[1:]
result = ''
for sentence in blog_lines:
    result = result + sentence[0]
print(result)
