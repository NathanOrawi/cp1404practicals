"""
program to count the occurrences of words in a string

Word Occurrences
Estimate: 20 minutes
Actual: 41 minutes
"""

string = input("Enter phrase: ")
words = sorted(string.split())

word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

max_length = max(len(name) for name in list(word_to_count.keys()))
for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
