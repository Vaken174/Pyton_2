def count_words():
    text = input("Введите строку: ")
    word_list = text.lower().split()

    unique_words = set(word_list)

    frequency = {word: word_list.count(word) for word in unique_words}

    for word, quantity in frequency.items():
        print(f"{word}: {quantity}")

count_words()