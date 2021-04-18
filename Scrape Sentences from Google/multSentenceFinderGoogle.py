"""TODO
- find the sentence in subList that has a nice length
    -Do this by removing sentences with ? or ! in them
- that sick list comprehension comes from stackoverflow 16032832

"""
import requests
from googlesearch import search
import random
import os
import shelve
"""from bs4 import BeautifulSoup"""

os.chdir("C:\\Users\\tomas\\Desktop\\Multi-Side Flashcard Project")
d2 = shelve.open('Remaining Vocab')
listRemain = d2['Remaining']
sentenceDict = {} # 

for word in listRemain:
	query = word[0]
	pageList = []
	#Part 1 - this loop should load the contents of all 10 results into the pageList[]
	for j in search(query, tld="co.jp", lang="jp", num=10, stop=10):
		try:
		    r = requests.get(j)
		    text = r.text
		    pageList.append(text)
		    print(j)
		#exceptions that tend to arise when there is a problem with one URL.
		except:
			print('Some random exception that I don\'t fucking know about occured. Sue me you fucking nerds!')
		# except RemoteDisconnected:
		# 	print('RemoteDisconnected')
		# except HTTPError:
		# 	print('HTTPError')
		# except URLError:
		# 	print('URL_Error')
		# except  HTTPException:
		# 	print("HTTPException")

		# except  http.client.RemoteDisconnected:
		# 	print('Error: http.client.RemoteDisconnected')
		# except  urllib3.exceptions.ProtocolError:
		# 	print('Error: urllib3.exceptions.ProtocolError')
		# except  requests.exceptions.ConnectionError:
		# 	print('Error: requests.exceptions.ConnectionError:')

	#Part 2 search page for keyword.
	sentenceList = [] # refreshes with each main loop
	for page in pageList:
	    subList = [sentence + '。' for sentence in page.split('。') if query in sentence and len(sentence) <= 40]
	    sentenceList.extend(subList)
	sentenceDict[query] = sentenceList # pesists sentenceList outside of the loop
	print(f"{query}:{sentenceDict[query]}")
print(sentenceDict) # can copy and paste results if they are good.
#for sentence in sentenceList:
#    print(sentence)
