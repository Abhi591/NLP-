import re 
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.tokenize import word_tokenize

text = open('textlist.txt','r').read()
# removing punctutations
contents=re.sub(r'[^\w\s]','',str(text))   
sentences = nltk.sent_tokenize(contents.lower())    #split the text in sentences
# print(sentences)
phrases = []


for line in sentences:
    words = nltk.word_tokenize(line)      # split the text in words 
    phrase = ''
    for word in words:
        if word not in stopwords.words('english'):
            phrase+=word + ' '
        else:
            if phrase != '':
                phrases.append(phrase.strip())          
                phrase = ''

print("  Candidate Phrases : \n",phrases)

word_freq = defaultdict(int)       # defaultdict a valuable option for 
word_degree = defaultdict(int)     # handling missing keys in dictionaries if there's one
word_score = defaultdict(float)

for phrase in phrases:
    words = phrase.split(' ')     #will only split if theres more than one word
    phrase_length = len(words)    #len of ['like', 'show']=2  and ['show'] =1
    for word in words:
        word_freq[word]+=1           #counts frequency of each word in the text
        word_degree[word]+=phrase_length         

# print(word_freq)
# print(word_degree)

for word,freq in word_freq.items():
    degree = word_degree[word]
    score = ( 1.0 * degree ) / (1.0 * freq )
    word_score[word] = score

phrase_scores = defaultdict(float)


for phrase in phrases:
    words = phrase.split(' ')
    score = 0.0
    for word in words:
        score+=word_score[word]
    phrase_scores[phrase] = score

print('******** Candidate Phrases scored ****************')
for k in sorted(phrase_scores,key = phrase_scores.get,reverse=True):
    if phrase_scores[k] > 3:
    	print(k)
