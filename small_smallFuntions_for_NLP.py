from matplotlib import pyplot
import nltk
'''
process:country list and  and its code
i/p:nothing
o/p:countries and countries code
'''

import pycountry

def Counteryandcode():
    for countrie in pycountry.countries:
        print(countrie)

Counteryandcode()


'''
sentences into sentence tokenize
i/p:Text
o/p:list of sentence
'''

from nltk.tokenize import sent_tokenize

def Texttosentences(news):
    string = sent_tokenize(news)
    print(string)

print("enter the news")
news = input()
Texttosentences(news)

'''
process:sentence into words tokenize
i/p:Text
o/p:list of words
'''
import nltk
from nltk.tokenize import word_tokenize


def sentencestoword(news):
    string = word_tokenize(news)
    print(string)


print("enter the news")
news = input()
sentencestoword(news)



'''
process:removing stopwords from sentence
i/p:Text
o/p:list of words after removing stopwords
'''

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def removingstopwords(news):
    string = word_tokenize(news)
    print("stopwords list:", set(stopwords.words("english")))
    stop_words = set(stopwords.words("english"))
    string = [w for w in string if not w in stop_words]
    print("After removing stop words", string)

print("enter the news")
news = input()
removingstopwords(news)



'''
process: from sentence words into stemming
i/p:Text
o/p:list of words after word stemming eg: many=mani
'''

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

def stemmerword(news):
    string = word_tokenize(news)
    stop_words = set(stopwords.words("english"))
    string = [w for w in string if not w in stop_words]
    porter = PorterStemmer()
    stems = []
    for t in string:
        stems.append(porter.stem(t))
    print(stems)

print("enter the news")
news = input()
stemmerword(news)


'''
process:from sentence words into lemmatizer
i/p:Text
o/p:list of words after word lemmatizer eg: corpora=corpus
'''

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def lemmatizerofword(news):
    string = word_tokenize(news)
    stop_words = set(stopwords.words("english"))
    string = [w for w in string if not w in stop_words]
    lemmatizer = WordNetLemmatizer()
    for j in string:
        print(lemmatizer.lemmatize(j))

print("enter the news")
news = input()
lemmatizerofword(news)


'''
processs:from sentence calculate word frequency
i/p:Text
o/p:plot of words
'''
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def frequencyofwords(news):
    string = word_tokenize(news)
    fdist = FreqDist()
    for word in string:
        fdist[word.lower()] += 1
    print(fdist)
    fdist.plot()

print("enter the news")
news = input()
frequencyofwords(news)
'''
process:synonyms for  each word
i/p:Text or word 
o/p:list of synonyms for each word
'''

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def synonymsofwords(news):
    string = word_tokenize(news)
    for strs in string:
        a = []
        for syn in wordnet.synsets(strs):
            for l in syn.lemmas():
                a.append(l.name())
        print("The word ", strs, "synonyms are :", a)

print("enter the news")
news = input()
synonymsofwords(news)