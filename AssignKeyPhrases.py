
#---------------------------PROBLEM STATEMENT 2-----------------------------------

import re 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def canditate_phrase(line):
	phrases = []
	words = nltk.word_tokenize(line)        #split the text in words
	phrase = ''
	for word in words:
		if word not in stopwords.words('english'):
			phrase+=word + ' '
		else:
			if phrase != '':
				phrases.append(phrase.strip())
				phrase = ''
	return phrases
# # response
f = open('textlist2.txt','r')
file=f.read()
# removing punctutations
text=re.sub(r'[^\w\s]','',str(file))   
sentence= nltk.sent_tokenize(text.lower())    #split the text in sentences
f1=open('keywords.txt','r')
keywords=f1.read()
keywords=keywords.split(",")
for k in keywords:
	score=canditate_phrase(str(sentence))
	for i in score:
		if i==k:
			print(k)