#I'm still not sure exactly what a "Slice" is, but this formula iterates over letters designated by the integer(index position) within the brackets.
#since the integer is set to -1, it starts at the last letter in the string, and goes backwards one by one, and returns the string that way.
#if we were to change that number within the brackets to -2, with would skip every other letter in teh string, and return the letters it did not skip.
#I.E. [::-2] would print "suSka", however it always starts at the -1 index position. 
#a positive number would have a similar effect, however it always starts at Index position 0

def reverse_a_string(reversed_string):
    return reversed_string[::-1]

favorite_game = 'dark souls'
example = 'aaabbbbbccccaacccbbbaaabbbaaa'

print(reverse_a_string(favorite_game))

#Utilizing the Title() function, we can capitalize the first letter of every word in a string.
#However, strings with numbers may cause issues. Looking into this

def capitalize_each_word_in_string(capitalized_string):
    return capitalized_string.title()

print(capitalize_each_word_in_string(favorite_game))

#We can call a function within a function (I think it's called recursion) and print the result to the terminal.
#The example below capitalizes the first characters in the string, backwards. 
#Maybe there's a way I can get it to work for the new string, instead of capitalizing the first letters of each word in the old string. Will research.

print(reverse_a_string(capitalize_each_word_in_string(favorite_game)))

def string_compression(compressed_string):
    index = 0                                       #variable holding an integer value of 0
    compressed = ''                                 #variable holding an empty string
    string_length = len(compressed_string)          #variable is equal to the length of the string we want to compress
    while index != string_length:                   #while integer value is not equal to the length of the string
        count = 1                                   #variable "count" is set to 1
        while (index < string_length -1) and (compressed_string[index] == compressed_string[index+1]): 
            count = count + 1
            index = index +1
        if count == 1:
            compressed += str(compressed_string[index])
        else:
            compressed += str(compressed_string[index]) + str(count)
        index = index + 1
    return compressed

#print(string_compression(example))

#the above example is complex and I dont fully udnerstand it yet, let's try something else.
#StackOverflow forum suggests I use a python function called zlib, lets test it here:

import zlib

comp = zlib.compress(example)
print(comp)
