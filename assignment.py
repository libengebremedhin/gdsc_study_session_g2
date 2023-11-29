
def get_user_input():
    return input("Enter a paragraph of text:\n")

def tokenize_text(text):
    return text.split()

def calculate_word_frequencies(words):
    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies

def display_word_frequencies(word_frequencies):
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {frequency}")

def display_top_n_words(word_frequencies, n):
    top_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:n]
    for word, frequency in top_words:
        print(f"{word}: {frequency}")

def search_word(word, word_frequencies):
    if word in word_frequencies:
        print(f"The word '{word}' appears {word_frequencies[word]} times.")
    else:
        print(f"The word '{word}' is not found in the text.")

def analyze_text_advanced(words):
    longest_word = max(words, key=len)
    print(f"The longest word is: {longest_word}")

    avg_word_length = sum(len(word) for word in words) / len(words)
    print(f"The average word length is: {avg_word_length:.2f}")

text = get_user_input()
words = tokenize_text(text)
word_frequencies = calculate_word_frequencies(words)

print("\nWord Frequencies:")
display_word_frequencies(word_frequencies)

n = int(input("\nEnter the value of N for top N words: "))
print(f"\nTop {n} Words:")
display_top_n_words(word_frequencies, n)

search_word_input = input("\nEnter a word to search in the text: ")
search_word(search_word_input, word_frequencies)

print("\nAdvanced Analysis:")
analyze_text_advanced(words)
