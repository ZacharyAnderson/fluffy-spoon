# >>> example = 'foo bar baz bar baz bar'
# >>> top_k_words(phrase=example, k=0)
# []
# >>> top_k_words(phrase=example, k=1)
# ['bar']
# >>> top_k_words(phrase=example, k=2)
# ['bar', 'baz']
# >>> top_k_words(phrase=example, k=3)
# ['bar', 'baz', 'foo']
# >>> top_k_words(phrase=example, k=4)
# ['bar', 'baz', 'foo']


def top_k_words(string1, k):
    word_list =[]
    tmp_word = ""
    for ch in string1:
        if ch == " ":
            word_list.append(tmp_word)
            tmp_word = ""
        else:
            tmp_word += ch

    word_dict = {}
    for word in word_list:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sorted_by_value = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)
    output_list = []
    for i in range(k):
        if i < len(word_dict.keys()):
            output_list.append(sorted_by_value[i][0])
    return output_list




string1 = 'foo bar baz bar baz bar'
k=4

print(top_k_words(string1, k))


