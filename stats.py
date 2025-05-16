def get_wordcount(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def get_each_letter_count(file_contents):
    file_contents = file_contents.lower()
    letter_count = {}
    for letter in file_contents:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def sorted_letter_count(letter_count):
    letter_list = []
    for char, count in letter_count.items():
        letter_list.append({"char": char, "num": count})
    letter_list.sort(key=lambda x: x["num"], reverse=True)
    for letter in letter_list:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
        print(f"{letter['char']}: {letter['num']}")