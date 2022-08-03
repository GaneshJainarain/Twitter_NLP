from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

"""
We are using tweet data, the construction of a tweet can be broken down into four categories:
- Text data: "It is cold outside brr"
- Emojis
- Mentioning of a user: "@JaneDoe"
- Hyperlinks: "https:linktowebsite.com"
"""
tweet = "@RicheyJay today is so so hot, staying @ home 🥵 https://weather.com"

#Now we have the tweet, we will apply the roberta 
#model to see what is the emotion of the tweet

"""
But first we need to do some preprocessing for the model
"""
tweet_words = []
for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'

    elif word.startswith('http'):
        word = "http"
    tweet_words.append(word)
    
#Putting our tweet back together:
tweet_processed = " ".join(tweet_words)
print(tweet_processed)