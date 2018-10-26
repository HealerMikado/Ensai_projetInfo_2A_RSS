import win32console
import feedparser
import urllib.request

win32console.SetConsoleCP(65001)
win32console.SetConsoleOutputCP(65001)

proxy = urllib.request.ProxyHandler ({'https': 'proxy-rie.http.insee.fr:8080'})

d = feedparser.parse("https://www.courrierinternational.com/feed/category/6260/rss.xml", handlers=proxy)
 
for post in d.entries :
    print(post["summary"])
