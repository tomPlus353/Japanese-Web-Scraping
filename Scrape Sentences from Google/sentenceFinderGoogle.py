"""TODO
- find the sentence in subList that has a nice length
    -Do this by removing sentences with ? or ! in them
- that sick list comprehension comes from stackoverflow 16032832

"""
import requests
from googlesearch import search
import random
"""from bs4 import BeautifulSoup"""
query = input("Enter Japanese word here: ")
pageList = []
#this loop should load the contents of all 10 results into the pageList[]
for j in search(query, tld="co.jp", lang="jp", num=10, stop=10):
    r = requests.get(j)
    text = r.text
    pageList.append(text)
    print(j)


sentenceList = []
for page in pageList:
    subList = [sentence + '。' for sentence in page.split('。') if query in sentence and len(sentence) <= 40]
    if subList:
        sentenceList.append(random.choice(subList))
    
for sentence in sentenceList:
    print(sentence)
