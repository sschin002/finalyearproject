from indicnlp.tokenize import indic_tokenize

# Read the text file
with open('translated_nepali_captions.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize a list to store tokenized data
tokenized_data = []

# Iterate through each line
for line in lines:
    # Split by comma
    image_id, caption = line.strip().split(',', 1)
    
    # Tokenize the caption using Indic NLP library
    caption_tokens = indic_tokenize.trivial_tokenize(caption, lang='hi')
    
    # Append the tokenized data
    tokenized_data.append((image_id, caption_tokens))

# Print the tokenized data
for image_id, caption_tokens in tokenized_data:
    print(f"Image ID: {image_id}")
    print("Caption Tokens:", caption_tokens)
    print()
