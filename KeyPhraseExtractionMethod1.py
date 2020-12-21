import pandas as pd
import RAKE
import operator
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
