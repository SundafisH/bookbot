def count(file):
    wordcount = len(file.split())
    return wordcount

def countchars(file):
    char = {}
    for i in file.lower():
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    return char

def sort_on(char):
    char_list = []
    for char, num in char.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list