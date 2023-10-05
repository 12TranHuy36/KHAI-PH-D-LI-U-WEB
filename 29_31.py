import re
import requests
import nltk
import re
import os
from bs4 import BeautifulSoup
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from underthesea import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')



src=f'D:\\29_31_BTNC3\câu5'
obj_list=os.listdir(src)

Content=""
L=[]
for i in obj_list:
    # Read file text
    f = open(src+"\\"+i, "r", encoding="utf-8")
    text=f.read()
    text_pre=text.replace("\n","")  # Remove the newline command
    text_pre=text_pre.lower() # Convert text to lowercase
    text_pre=re.sub(r'[^\w\s]','',text_pre) # Remove punctuation
    text_pre = re.sub("\d+", " ", text_pre) # Remove number
    text_pre = re.sub(r"[!@#$[]()]'", "", text_pre) # Remove character: !@#$[]()
    text_pre= word_tokenize(text_pre, format="text") #  Tokenizing
    
    path=os.path.dirname(__file__)
    f = open(path+r"\vietnamese-stopwords.txt", "r", encoding="utf-8")
    List_StopWords=f.read().split("\n")
    text_pre=" ".join(text for text in text_pre.split() if text not in List_StopWords)# Remove StopWords
    text_pre=text_pre.split(' ') 
    # print(text_pre)
    
    for j in range(len(text_pre)):
        Content+= text_pre[j]+"\n"
        L+=[text_pre[j]]
            
filename=os.path.join(f"D:\\29_31_BTNC3",'CauA_txl.txt')    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(Content)

print("Number of words: ",len(L))
# Compute the frequency of all words
frequency_dist = FreqDist(word.lower() for word in L)

## show only th top 50 results
print(frequency_dist.most_common(100))

## Consider words with length greater than 3 and plot
large_words = dict([(k,v) for k,v in frequency_dist.items() if len(k)>3])
frequency_dist = nltk.FreqDist(large_words)
frequency_dist.plot(50,cumulative=False)

## Build a word cloud
from wordcloud import WordCloud
wcloud = WordCloud().generate_from_frequencies(frequency_dist)
#plotting the wordcloud
import matplotlib.pyplot as plt
plt.imshow(wcloud, interpolation="bilinear")
plt.axis("off")
plt.show()