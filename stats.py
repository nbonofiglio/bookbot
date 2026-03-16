def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    total_counts = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char not in total_counts:
            total_counts[char] = 1
        else:
            total_counts[char] = total_counts[char] + 1
    return total_counts

def sort_on(char):
    return char["num"]

def sort_counts(counts):
    counts.sort(reverse=True, key=sort_on)
    return counts