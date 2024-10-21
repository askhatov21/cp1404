def count_words(text):
    """The function count to words"""
    words = text.split()
    word_counts = {}
    """Count occurrences of each words"""
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_word_counts = sorted(word_counts.items())
    longest_word_length = max(len(word) for word, _ in sorted_word_counts)
    for word, count in sorted_word_counts:
        print(f'{word:{longest_word_length}} : {count}')
"""Ask the user input"""
input_text = input('Text:')
count_words(input_text)


