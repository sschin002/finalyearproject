import sys
sys.stdout.reconfigure(encoding='utf-8')

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

nepali_text = "तपाईंलाई कस्तो छ ? म ठिकै छु ।"

# Tokenization
tokens = word_tokenize(nepali_text)

# Remove punctuation
translator = str.maketrans('', '', string.punctuation)
tokens = [token.translate(translator) for token in tokens]

# Lowercase
tokens = [token.lower() for token in tokens]

# Remove stopwords
nepali_stopwords = set(stopwords.words('nepali'))
filtered_tokens = [token for token in tokens if token not in nepali_stopwords]

print(filtered_tokens)
