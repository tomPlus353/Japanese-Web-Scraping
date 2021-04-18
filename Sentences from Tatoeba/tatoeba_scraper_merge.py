#merge dictionaries

import shelve,os
#os.chdir("C:\\Users\\tomas\\Desktop\\Multi-Side Flashcard Project\\Scrape Sentences from Google")
from Scraped_Results_1 import sentenceDict2
from SentenceFinder2 import remaining
os.chdir("C:\\Users\\tomas\\Desktop\\Multi-Side Flashcard Project")
d1 = shelve.open('N1 Vocab Data')
vocab = d1['Vocab 1']
d1.close()
d2 = shelve.open('Raw Sentences')
sentences = d2['Raw Sentences 2']
d2.close
for i in remaining:
	if len(sentenceDict2[vocab[i][0]]) > 0:
		sentences[i] = sentenceDict2[vocab[i][0]]
		#print(sentenceDict2[vocab[i][0]])
		#print(sentences[i])
for i,s in enumerate(sentences):
	sentences[i] = list(set(s))

for i,s in enumerate(sentences):
	vocab[i].insert(3, s)
	#print(vocab[i])

d2 = shelve.open('Raw Sentences')
d2['Raw Sentences 3'] = sentences
d2.close

if all([True if len(word) == 8 else False for word in vocab]):
	d1 = shelve.open('N1 Vocab Data')
	d1['Vocab 2'] = vocab
	d1.close()
else:
	raise ValueError






