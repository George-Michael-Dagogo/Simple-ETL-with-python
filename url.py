import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd

#I downloaded the xlsx file containing the links from the drive and renamed it as test

test = pd.read_csv("test.csv")

def easy(link):
    import requests
    from bs4 import BeautifulSoup
    import numpy as np

    #the headers dictionary lets the site know the request is coming from a browser 

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

    r = requests.get(link, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    article_data = soup.find("title").text 

    article_content = soup.find("div", class_="td-post-content").text

    URL_ID = article_data.ljust(len(article_data)+100) + article_content
    #create a 
    text_file = open("URL_ID.txt", "a",encoding="utf-8")
    n = text_file.write(URL_ID)
    text_file.close()
        
for i in test.URL:
    easy(i)
print('done')


seee= pd.read_csv('Output Data Structure.csv')
def easy(link):
    import requests
    from bs4 import BeautifulSoup
    import numpy as np
    import syllables
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import re

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    r = requests.get(link, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    article_content = soup.find("div", class_="td-post-content").text
    diction= pd.read_csv('diction.csv')

    punc = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''

    n_word = diction.loc[diction['Negative'] != 0]
    p_word = diction.loc[diction['Positive'] != 0]
    pw = p_word.Word.to_string(index=False).replace('\n', ' ')
    nw = n_word.Word.to_string(index=False).replace('\n', ' ')

    positive_word=pw.split()
    negative_word=nw.split()

    n_word = diction.loc[diction['Negative'] != 0]
    p_word = diction.loc[diction['Positive'] != 0]

    text = article_content
    # Convert text to lowercase and split to a list of words
    tokens = word_tokenize(text.lower())
    # Remove stop words
    english_stopwords = stopwords.words('english')
    tokens_wo_stopwords = [t for t in tokens if t not in english_stopwords]

    positive_score = 0
    negative_score = 0
    for word in positive_word:
        if word in article_content.upper():
            positive_score += 1
        
    for word in negative_word:
        if word in article_content.upper():
            negative_score += 1 
        
    complex_count=0
    for i in article_content.split():
        if syllables.estimate(i) >=2 :
            complex_count+=1
        
    for e in article_content:
        if e in punc:
            article_content = article_content.replace(e, "")
              
    polarity_score = (positive_score - negative_score)/ ((negative_score + negative_score) + 0.000001)

    word_count = len(tokens_wo_stopwords)

    subjectivity_score = (positive_score + negative_score)/ ((word_count) + 0.000001)

    number_sentences = len(re.split(r'[.!?]+', article_content))

    average_sentence_length = word_count / number_sentences 

    perc_complex_words = complex_count / word_count

    fog_index = 0.4 * (average_sentence_length + perc_complex_words)

    avg_word_sentence = word_count / number_sentences

    syllable_word = syllables.estimate(article_content)

    pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
    pronouns = len(pronounRegex.findall(article_content))

    words = article_content.split()
    avg_word_len = sum(len(word) for word in words) / len(words)\

    df2 = pd.DataFrame({'URL':[link],
                        'POSITIVE SCORE': [positive_score],
                        'NEGATIVE SCORE' : [negative_score],
                        'POLARITY SCORE': [polarity_score],
                       'SUBJECTIVITY SCORE': [subjectivity_score],
                       'AVG SENTENCE LENGTH': [average_sentence_length],
                       'PERCENTAGE OF COMPLEX WORDS': [perc_complex_words],
                       'FOG INDEX': [fog_index],
                       'AVG NUMBER OF WORDS PER SENTENCE': [avg_word_sentence],
                       'COMPLEX WORD COUNT': [complex_count],
                       'WORD COUNT': [word_count],
                       'SYLLABLE PER WORD':[syllable_word],
                        'PERSONAL PRONOUNS':[pronouns],
                       'AVG WORD LENGTH': [avg_word_len]})
    df = seee.append(df2, ignore_index = True)
    df.to_csv('log.csv', mode='a', index=False, header=True)
    
        
for r in test.URL:
    easy(r)  