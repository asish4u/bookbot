def get_book_text(path):
    with open(path, 'r') as file:
        text = file.read()
    return text

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_frequency(text):
    char_frequency = {}
    for char in text.lower():
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

def sort_on(di):
    return di["num"]

def get_list_of_char(text):
    counts = get_character_frequency(text)
    sorted_count = []
    for i in counts:
        if i.isalpha():
            sorted_count.append({"char": i, "num": counts[i]})
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count
