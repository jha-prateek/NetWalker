import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import sys
sys.path.append('C:\Users\prate\PycharmProjects\NetWalker\Flask')
from zxc import *

print text

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("tr.txt")
# sample_text = text

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
	sent=""
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
	    chunkGram = r"""Chunk: {<.*>+}
             }<IN|DT|TO|MD|LS|FW|CC|VBZ|VBD|PRP|VBG|RB|WRB|WP.?>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            ar = chunkParser.parse(tagged)
	    sent=sent+str(ar)
	    #print(ar)
	res=""
	tok=nltk.word_tokenize(sent)
	x="abc"
	for i in tok:
		if x=="Chunk":
			j=i
			while(not(j==')') and ('/' in j)):
				res=res+" "+j[:j.index('/')]
				#print res
				j=tok[tok.index(j)+1]
			x="abc"
		if i=="Chunk":
			x="Chunk"
	print res
	return res
    except Exception as e:
        print(str(e))


final_sent = process_content()
myList = nltk.word_tokenize(final_sent)
print myList