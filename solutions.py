# Given the following string: "race bear thing care keen trap tweet earth knee heart neek tewt"
# Write a function which takes as input this string and returns as
#  a result a dictionary of items, which contains the words from the given string as 
#  keys and as values a list with its anagrams from within the input string
#   if there are any (if there are not, an empty list shall be used as value for the specific keyword). 
#  Anagrams already found for a specific word shall not be considered new keys in the dictionary.

string = "race bear thing care keen trap tweet earth knee heart neek tewt"

def get_anagrams(string):
    words_list = string.split(" ")
    output = {}
    for word in words_list:
        for figure in words_list:
            if len(figure) == len(word) and sorted(figure) == sorted(word) and figure != word:
                output[figure] = word
    print(output)
        
        # dictionary = { figure: word for figure in words_list if len(figure) == len(word) and sorted(figure) == sorted(word) and figure != word }
        # non_dictionary = { figure: [] for figure in words_list if len(figure) != len(word) and figure != word }
        # if dictionary != {}:
        #     output.update(non_dictionary)
        #     output.update(dictionary)

    # final_output = { f_word: [].append(item) for f_word, item in output }
    # print(output)


get_anagrams(string)
# Hello mahia i know this isn't the absolute correct answer
# but if i had a little more time am sure i would be able to figure it out
# N.b: what is left to be implemented is make everything be in a single dictionary
# and return empty list if it's already an anagram of another
# Please do well to consider me, I would really appreciate and approval 
# Or few more hours

# Thanks
# Best regards
# Philip