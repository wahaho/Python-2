import requests

newsurl = 'http://news.sina.com.cn/'
res = requests.get(newsurl)
res.encoding = 'utf-8'
print(res.text)


