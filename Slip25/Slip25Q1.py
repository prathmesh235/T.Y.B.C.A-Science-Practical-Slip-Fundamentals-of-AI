
text = input("Enter a string: ")

words = text.split()
frequency = {}

for word in words:
    word = word.lower()
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:")
for word, count in frequency.items():
    print(word, ":", count)
