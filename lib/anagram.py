# your code goes here!
# iterate over each word in the list to determine if a word has the same amount of letters. 
# if word has the same amount of letters iterate over the letters to determine if all letters are matching
# if all letters are matching the word is an anagram

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        origin_sorted = sorted(self.word)
        return [word for word in words if sorted(word) == origin_sorted]
    

#if sorted(word) doesn't equal an original sorted word then an empty list will be return. 
#list comprehension operates that way - the return of an empty list is built in 
#based on how it is written. 
#match method
#init method initializes an instance of Anagram class with a given word
# origin_sorted stores the sorted characters of the origianl worl
#the list comprehension iterates over each word in the words list, 
#sorts each word and checks if it matches origin_sorted

#the sorted() function is used to sort the characters of both the orginal
# word and each candidate word. 