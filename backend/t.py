import sys
sys.stdout.reconfigure(encoding='utf-8')
import sys
sys.stdout.reconfigure(encoding='utf-8')

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

file_path = 'translated_nepali_captions.txt'  # Replace with the actual path to your text file

tkn=[]
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()  # Remove leading and trailing whitespace
        if line:  # Check if the line is not empty
            parts = line.split(',')
            if len(parts) >= 2:
                image_id = parts[0]
                description = ' '.join(parts[1:])
                print("Image ID:", image_id)
                print("Description:", description)

# print(tokens)
# for element in tokens:

