from Scraped_Results_1 import sentenceDict
import re 
regex = re.compile(r'<.+?>|\\r|\\n|\u3000|\u2009|\r\n?|\r+?|\n+?')
regQuote = re.compile(r'&quot;?')

def cleaner(dictWithList):
	for key in dictWithList:
		if len(dictWithList[key]) > 0: #therefore item should be str.
			for index, item in enumerate(dictWithList[key]):
				dictWithList[key][index] = re.sub(regex,'',item)
				copy = dictWithList[key][index]
				dictWithList[key][index] = re.sub(regQuote,'"',copy)
		dictWithList[key] = list(set(dictWithList[key])) #duplicate removal
	return dictWithList

newDict = cleaner(sentenceDict)
print(newDict)
