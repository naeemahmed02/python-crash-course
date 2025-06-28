"""
This tutorial covers string manipulation methods.
"""

text = """
In 2017, researchers at Google published a paper that proposed a novel neural network
architecture for sequence modeling. Dubbed the Transformer, this architecture outperformed
recurrent neural networks (RNNs) on machine translation tasks, both in terms of translation
quality and training cost.
In parallel, an effective transfer learning method called ULMFiT showed that training long
short-term memory (LSTM) networks on a very large and diverse corpus could produce state
of-the-art text classifiers with little labeled data.
These advances were the catalysts for two of today’s most well-known transformers: the
Generative Pretrained Transformer (GPT) and Bidirectional Encoder Representations from
Transformers (BERT). By combining the Transformer architecture with unsupervised learning,
these models removed the need to train task-specific architectures from scratch and broke
almost every benchmark in NLP by a significant margin. Since the release of GPT and BERT, a
zoo of transformer models has emerged; a timeline of the most prominent entries is shown in
"""

# Original Text Preview
print(text[:600])   # Displaying first 600 characters

# String Methods

# Convert the entire text to uppercase
text_in_uppercase = text.upper()  # Original text converted into all uppercase characters 
print(text_in_uppercase)

# Convert the entire text to lowercase
text_in_lowercase = text_in_uppercase.lower()   # Uppercase text converted into all lowercase characters
print(text_in_lowercase)

# Capitalize every first character of each word
titled_text = text_in_lowercase.title()    # First character of each word capitalized
print(titled_text)

# Capitalize only the first character of the entire string
capitalized_text = text.capitalize()  # Only the first character of the first word capitalized
print(capitalized_text)

# Count the occurrence of a specific word
word_count = text.count('Transformer')  # Count how many times 'Transformer' appears
print(f"'Transformer' appears {word_count} times")

# Find the first index of a word
first_index = text.find('Transformer')  # Return the index of first occurrence of 'Transformer'
print(f"'Transformer' first appears at index {first_index}")

# Replace a word with another word
replaced_text = text.replace('Transformer', 'Transformers')  # Replacing 'Transformer' with 'Transformers'
print(replaced_text)

# Remove whitespaces from the beginning and end
stripped_text = text.strip()  # Remove leading and trailing whitespace
print(stripped_text)

# Check if text starts with a specific word
starts_with = text.startswith('In 2017')  # Check if text starts with 'In 2017'
print(f"Text starts with 'In 2017': {starts_with}")

# Check if text ends with a specific word
ends_with = text.endswith('in\n')  # Check if text ends with 'in'
print(f"Text ends with 'in': {ends_with}")

# Split text into a list of words
split_text = text.split()  # Split the text into list of words using spaces
print(split_text[:10])  # Print first 10 words

# Join a list of words into a string
joined_text = ' '.join(split_text)  # Join the list back into a single string
print(joined_text[:300])  # Display first 300 characters

# Check if all characters are digits
digit_check = "2025".isdigit()  # Returns True if all characters are digits
print(f"Is '2025' all digits? {digit_check}")

# Check if all characters are alphabetic
alpha_check = "Google".isalpha()  # Returns True if all characters are letters
print(f"Is 'Google' all alphabetic? {alpha_check}")

# Check if all characters are lowercase
lower_check = "hello".islower()  # Returns True if all characters are lowercase
print(f"Is 'hello' all lowercase? {lower_check}")

# Check if all characters are uppercase
upper_check = "HELLO".isupper()  # Returns True if all characters are uppercase
print(f"Is 'HELLO' all uppercase? {upper_check}")

# Check if string is title-cased
title_check = titled_text.istitle()  # Returns True if all words start with uppercase
print(f"Is text title-cased? {title_check}")

# Check if string is alphanumeric (letters + numbers only)
alnum_check = "GPT3".isalnum()  # True if string contains only letters and numbers
print(f"Is 'GPT3' alphanumeric? {alnum_check}")

# Center the text with padding
centered = "NLP".center(20, '-')  # Center the string 'NLP' with '-' padding
print(centered)

# Left justify the string
left_justified = "Transformer".ljust(20, '*')  # Left justify with '*'
print(left_justified)

# Right justify the string
right_justified = "BERT".rjust(20, '*')  # Right justify with '*'
print(right_justified)

# Swap case of each letter
swapped_case = "Deep Learning".swapcase()  # Lowercase becomes uppercase and vice versa
print(swapped_case)

# Encode to bytes
encoded_text = text.encode('utf-8')  # Encode text to bytes
print(encoded_text[:60])  # Show part of the encoded byte string

# Check if text is a valid identifier (like variable name)
identifier_check = "transformer_1".isidentifier()  # True if string is a valid variable name
print(f"Is 'transformer_1' a valid identifier? {identifier_check}")
