def count_words(input_string):
    words = input_string.split()
    return len(words)
input_string = "Hello, how are you doing today?"
word_count = count_words(input_string)
print(f"The number of words in the string is: {word_count}")
