def duplicate_encode(word):
    lower_word = word.lower()
    result_dict ={}
    result_list = []
    for char in lower_word:
        if char in result_dict:
            result_dict[char] +=1
        else:
            result_dict[char] =1
    for char in lower_word:
        if result_dict[char] > 1:
            result_list.append(")")
        else:
            result_list.append("(")
    return str("".join(result_list))

print(duplicate_encode("din"))
