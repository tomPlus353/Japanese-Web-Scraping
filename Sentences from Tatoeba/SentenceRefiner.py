from Scraped_Results_1 import sentenceDict2
import shelve,os
os.chdir("C:\\Users\\tomas\\Desktop\\Multi-Side Flashcard Project")
d1 = shelve.open('N1 Vocab Data')
vocab = d1['Vocab 1']
d1.close()
d2 = shelve.open('Raw Sentences')
sentences = d2['Raw Sentences']
d2.close



#B. refine this list to one sentence if 1) that sentence that has other words from vocab in it. (the most words)
#2) if length is 1 then no need to refine.
