#the request library allows me to send a request and grab information from a website
import requests
import bs4

res = requests.get('http://www.example.com')
print(res.text)
soup = bs4.BeautifulSoup(res.text,'lxml')
#soup.select('title') returns a list of a tag object
print(soup.select('title'))
title_tag_list = soup.select('title')
print(title_tag_list)
print(title_tag_list[0])
#to get the text content of the title tag
print(title_tag_list[0].getText())

res = requests.get('https://en.wikipedia.org/wiki/Room_641A')
soup = bs4.BeautifulSoup(res.text,'lxml')
for item in soup.select('.mw-headline'):
    print(item.text)

res = requests.get('https://en.wikipedia.org/wiki/Cicada_3301')
soup = bs4.BeautifulSoup(res.text,'lxml')
image_info = soup.select('.thumbimage')
cicada = image_info[0]
#dictionary call
cicada_src = cicada['src']
print(cicada_src)
image_link = 'http:' + cicada_src
print(image_link)
cicada_img = requests.get(image_link,'lxml')
f = open('cicada_image_new.jpg','wb')
f.write(cicada_img.content)
f.close()
