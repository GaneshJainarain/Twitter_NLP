from transformers import AutoTokenizer,
    AutoModelForSequenceClassification
from scipy.special import softmax

"""
We are using tweet data, the construction of a tweet can be broken down into four categories:
- Text data: "It is cold outside brr"
- Emojis
- Mentioning of a user: "@JaneDoe"
- Hyperlinks: "https:linktowebsite.com"
"""
tweets = " "