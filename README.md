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
- Emojis 🙏🏽
- Mentioning of a user: "@JaneDoe"
- Hyperlinks: "https:linktowebsite.com"

