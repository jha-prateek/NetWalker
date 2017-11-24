import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import sys
#sys.path.append('C:\Users\prate\PycharmProjects\NetWalker\Flask')
#from zxc import *
sample="Saurabh has to go to banglore"
class nlp(object):


	def process_content(self, sample_text):
	    
		try:
			train_text = state_union.raw("2005-GWBush.txt")
			#sample_text = state_union.raw("tr.txt")
		
			custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
			tokenized = custom_sent_tokenizer.tokenize(sample_text)		
		
			sent=""
		        for i in tokenized:
		            words = nltk.word_tokenize(i)
		            tagged = nltk.pos_tag(words)
			    chunkGram = r"""Chunk: {<.*>+}
		             }<IN|DT|TO|MD|LS|FW|CC|VBZ|VBD|PRP|VBG|RB|WRB|WP.?>+{"""
		            chunkParser = nltk.RegexpParser(chunkGram)
		            ar = chunkParser.parse(tagged)
			    sent=sent+str(ar)
			    #print(str)
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
			return nltk.word_tokenize(res)
			#pes = nltk.word_tokenize(res)
			#print pes		
			#return res
		except Exception as e:
	        	print(str(e))
# n=nlp()
# n.process_content(sample)
	
	#final_sent = process_content()
	#myList = nltk.word_tokenize(final_sent)
	#print myList


