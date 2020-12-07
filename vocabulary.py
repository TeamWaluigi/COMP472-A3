def extract_vocabulary_original(data_set) -> any:
    entries = data_set["text"]
    vocabulary = set()

    for entry in entries:
        words = entry.split(" ")
        for word in words:
            formatted_word = word.lower()
            vocabulary.add(formatted_word)

    return vocabulary


def extract_vocabulary_filtered(data_set) -> any:
    entries = data_set["text"]
    vocabulary = set()
    word_frequency = dict()

    for entry in entries:
        words = entry.split(" ")
        for word in words:
            formatted_word = word.lower()

            if formatted_word in word_frequency:
                vocabulary.add(formatted_word)
            else:
                word_frequency[formatted_word] = 1

    return vocabulary
