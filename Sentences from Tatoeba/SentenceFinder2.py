import shelve,os
os.chdir("C:\\Users\\tomas\\Desktop\\Multi-Side Flashcard Project")
d1 = shelve.open('N1 Vocab Data')
vocab = d1['Vocab 1']
d1.close()
d2 = shelve.open('Raw Sentences')
sentences = d2['Raw Sentences 2']
d2.close
remaining = [index for index, value in enumerate(sentences) if value[0] =='Sentence not found.']
print(len(remaining)) #246
print(len(sentences),len(vocab)) #3476 for both
listRemain = []
for i in remaining:
	#print(sentences[i], ":", vocab[i])
	listRemain.append(vocab[i])
d3 = shelve.open('Remaining Vocab')
d3['Remaining'] = listRemain
d3.close()
#print(vocab[remaining[0]][0][:-1])
#endings = {'しい':['しく','しな']"う":["って","った","わない",'い','え'],"つ":["って","った",'ち','て'],"る":["って","て","った","た",'り','れ','ます','ません'],"く":["いて","いた",'き','け'],"ぐ":["いで","いだ",'ぎ','げ'],"ぬ":["んで","んだ",'に','ね'],"ぶ":["んで","んだ",'び','べ'],"む":["んで","んだ",'み','め'],"す":["して","した",'し','せ']}

