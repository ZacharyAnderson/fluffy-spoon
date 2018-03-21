def anagrams(word, words):
    '''
    For this function, I will evaluate each word character by character
    adding up the total of their ascii values. If the ascii value sum is
    the same then they must include the same letters.
    '''
    word_sum = 0
    is_anagrams = []
    #Evaluate the ascii sum of word
    for char in word:
        word_sum += ord(char)
    '''
    In this loop we wll evaluate the sum of the word
    then test if the ascii sum of word is equal to it
    if that is true we will append it to the list.
    '''
    for word in words:
        word_total = 0
        for char in word:
            word_total += ord(char)
        if word_total == word_sum:
            is_anagrams.append(word)
    return is_anagrams

'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
    'abba' & 'baab' == true
    'abba' & 'bbaa' == true
    'abba' & 'abbba' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
    anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
    anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
    anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''