"""
Word Occurrences
Count number of times each word appear in a sentence given by user
"""

text_to_check = input("Give me a text!: ")

# split string to list
text_list = text_to_check.split()

# new dictionary for counting word to count
word_count = {}

for word in text_list:
    count = word_count.get(word, 0)
    # Count up if word occur
    word_count[word] = count + 1

text_list = list(word_count.keys())

# list all words appeared in the sentence
max_length = max((len(word) for word in text_list))
for word in text_list:
    print(f"{word:{10}} : {word_count[word]}")
