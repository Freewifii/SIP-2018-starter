'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

subjectivityList = []
polarityList = []

# Continue your program below! 
data = '{tweets_small.json}'
json_string = json.dumps(data)
tweettext = []
tweetstring = ""
for tweet in tweetData: 
    tweetblob = TextBlob(tweet["text"])
    polarityList.append(tweetblob.polarity)
    subjectivityList.append(tweetblob.subjectivity)
    tweetstring += tweet['text']
print(tweetstring)

tweetBlob = TextBlob(tweetstring)

word_dict = {}

for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict)


#print(tweetBlob.translate(to='es'))
    #print (tweettext ['text'])
#dictionary keys

my_list = polarityList
next_list = subjectivityList
print(sum(my_list)/len(my_list))
print(sum(next_list)/len(next_list))

# Textblob sample:
tb = TextBlob("You are a horrible computer scientist.")
#print(tb.sentiment)
#print(polarityList)
#print(subjectivityList)

import matplotlib.pyplot as plt

someList = [my_list]
plt.hist(someList, bins=[-1, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

someList = [next_list]
plt.hist(someList, bins=[-1, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()