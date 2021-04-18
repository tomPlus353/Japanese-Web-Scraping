import csv, os
os.chdir('C:\\Users\\tomas\\Desktop\\Multi-Side Flashcard Project\\Sentences from Tatoeba\\')
csv_handle = open("jpn_sentences.tsv",'r')
csv_read = csv.reader(csv_handle, delimiter="\t")
csvList = list(csv_read)
#print(len(csvList))
#print(f"Row 1, column 3: {csvList[0][2]}",f"Row 1, column 1: {csvList[0][0]}")
tatoebaDict = {}
for row in csvList: 
	tatoebaDict[row[0]] = row[2]


import shelve

os.chdir('C:\\Users\\tomas\\Desktop\\Multi-Side Flashcard Project\\')
d = shelve.open("N1 vocab data")
vocab = d['Vocab 1']
d.close()
#print(len(vocab))
#sentence matching.
#create a list matching sentences for each word
#first match my kanji, then match by kana, then match by kanji minus a ru at the end(or similar)
#Else append 'Sentence not found'
#NOTE -> you want to get some sort of autoconjugator for words
#refine this list to one sentence if 1) that sentence that has other words from vocab in it. (the most words)
#2) if length is 1 then no need to refine.
listOfLists = []
from progress.bar import ChargingBar
endings = {'しい':['しく','しな'],
"う":["って","った","わない",'い','え'],
"つ":["って","った","た",'ち','て'],
'いる':['いた','いて','い','いま','いない','いろ'],
'える':['えた','えて','え','えま','えない','えろ'],
"る":["って","て","った","た",'り','れ','ま','ない','ろ'],
"く":["いて","いた","か","き","け"],
"ぐ":["いで","いだ","が","ぎ","げ"],
"ぬ":["んで","んだ","な","に","ね"],
"ぶ":["んで","んだ","ば","び","べ"],
"む":["んで","んだ","ま","み","め"],
"す":["して","した","さ","し","せ"]}
with ChargingBar(max=len(vocab)) as bar:
	for word in vocab:
		nestedList = []
		for code in tatoebaDict:
			#print(f"DEBUGGING\nWord index zero = {word[0]}\nType of word index zero = {type(word[0])}")
			#print(f"DEBUGGING\nContents of current key = {tatoebaDict[code]}\nType of content at current key = {type(tatoebaDict[code])}")
			if word[0] in tatoebaDict[code]:
				#print("DEBUGGING: IF")
				nestedList.append(tatoebaDict[code])
			elif word[0][-1] in list(endings.keys()):
				for subend in endings[word[0][-1]]:
					tempWord = word[0][:-1] + subend
					if tempWord in tatoebaDict[code]:
						#print("DEBUGGING: ELIF2")
						if tatoebaDict[code] not in nestedList:
							nestedList.append(tatoebaDict[code])
			elif word[1] in tatoebaDict[code]:
				#print("DEBUGGING: ELIF1")
				nestedList.append(tatoebaDict[code])
		if len(nestedList) == 0:
			nestedList.append('Sentence not found.')
			#print('Sentence not found.')
		listOfLists.append(nestedList)
		#print(f"LENGTH of listOfLists:{len(listOfLists)} ")
		bar.next()

#print('LENGTH:\n',len(listOfLists),'CONTENTS:\n',listOfLists)
newData = shelve.open('Raw Sentences')
newData['Raw Sentences 2'] = listOfLists
newData.close()