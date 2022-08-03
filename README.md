# Twitter Sentimental Analysis using NLP(Natural Language Processing)

- "A multilingual XLM-roBERTa-base model trained on ~198M tweets and finetuned for sentiment analysis. The sentiment fine-tuning was done on 8 languages (Ar, En, Fr, De, Hi, It, Sp, Pt) but it can be used for more languages".

### Downloading the model from the hugging face website

```python
pip install transformers
```
- To convert the output of the model to probability scores
```python
pip install scipy
```

### We are using tweet data, the construction of a tweet can be broken down into four categories:
- Text data: "It is cold outside brr"
- Emojis: 🙏🏽
- Mentioning of a user: "@JaneDoe"
- Hyperlinks: "https:linktowebsite.com"

- Preprocessesing Phase
```python
"
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
```