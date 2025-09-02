def my_split(sentence, separator):
    result = []
    word = ""
    for char in sentence:
        if char == separator:
            result.append(word)
            word = ""
        else:
            word += char
    result.append(word)
    return result

def my_join(word_list, separator):
    result = ""
    for i in range(len(word_list)):
        result += word_list[i]
        if i < len(word_list) - 1:
            result += separator
    return result

def main():
    sentence = input("Please enter sentence:")
    words = my_split(sentence, " ")
    joined = my_join(words, ",")
    print(joined)
    for word in words:
        print(word)

    main()
