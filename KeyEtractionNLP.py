
#---------------------------PROBLEM STATEMENT 1-----------------------------------

#'-----------------METHOD 1-------------'

import re 
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.tokenize import word_tokenize

def canditate_phrase(sentences):
	phrases = []
	for line in sentences:
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

# calculating frequency and degree for each word/keyphrase in the text

def freq_degree(phrases):
	word_freq=defaultdict(int)
	word_degree=defaultdict(int)
	for phrase in phrases:
	    words=phrase.split(' ')     #will only split if theres more than one word
	    phrase_length=len(words)    #len of ['really','like'] = 2 and ['show'] = 1
	    for word in words:
	        word_freq[word]+=1           #counts frequency of each word in the text
	        word_degree[word]+=phrase_length
	return word_freq,word_degree

def word_score_cal(word_freq,word_degree):
	word_score=defaultdict(float)
	for word,freq in word_freq.items():
		degree = word_degree[word]
		score = ( 1.0 * degree ) / (1.0 * freq )
		word_score[word] = score
	return word_score

def phrase_scores_cal(phrases,word_score):
	phrase_scores=defaultdict(float)
	for phrase in phrases:
		words = phrase.split(' ')
		score = 0.0
		for word in words:
			score+=word_score[word]
			phrase_scores[phrase] = score
	return phrase_scores

def get_phrase_score(sentences):
	keywords=[]
	phrases=canditate_phrase(sentences)
	word_freq,word_degree=freq_degree(phrases)
	word_score=word_score_cal(word_freq,word_degree)
	phrase_scores=phrase_scores_cal(phrases,word_score)
	for k in sorted(phrase_scores,key = phrase_scores.get,reverse=True):
		if phrase_scores[k] > 3:
			keywords.append(k)
	return keywords

# response
f1 = open('textlist.txt','r')
f=f1.read()
# removing punctutations
text=re.sub(r'[^\w\s]','',str(f))   
sentences = nltk.sent_tokenize(text.lower())    #split the text in sentences
scores=get_phrase_score(sentences)
print("\n",scores)
f1.close()
# to use these keywords in problem statement2
f=open('keywords.txt','w')
for s in scores:
	f.write(str(s)+",")

print('---------------------------METHOD 2-------------------------------')

import RAKE
from rake_nltk import Rake
stop_dir='SmartStoplist.txt'
rake_object=RAKE.Rake(stop_dir)

def Sort_Tuple(tup):
	tup.sort(key=lambda x:x[1],reverse=True)
	return tup
f = open("textlist.txt", "r")
subtitles=f.read()
keywords=rake_object.run(subtitles)[:10]
print('keywords: ',keywords)

r=Rake() # uses stopwords for english from NLTK , and all puntuation characters
r.extract_keywords_from_text(subtitles)
print(r.get_ranked_phrases()[0:10])













