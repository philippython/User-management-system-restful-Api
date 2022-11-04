# Given the following string: "race bear thing care keen trap tweet earth knee heart neek tewt"
# Write a function which takes as input this string and returns as
#  a result a dictionary of items, which contains the words from the given string as 
#  keys and as values a list with its anagrams from within the input string
#   if there are any (if there are not, an empty list shall be used as value for the specific keyword). 
#  Anagrams already found for a specific word shall not be considered new keys in the dictionary.


string = "race bear thing care keen trap tweet earth knee heart neek tewt"

def get_anagrams(string):
    words_list = string.split()
    output = { word : ( [].append(word) if else []) for word in words_list }
    # final = { key:value.append(key) for key, value in output if len(key) == len()}
    print(output)
    # print(final)]
        

get_anagrams(string)
