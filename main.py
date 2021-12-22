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

#Below is an example of a function that compresses strings in an argument.

# def string_compression(compressed_string):
#     index = 0                                       #variable holding an integer value of 0
#     compressed = ''                                 #variable holding an empty string
#     string_length = len(compressed_string)          #variable is equal to the length of the string we want to compress
#     while index != string_length:                   #while integer value is not equal to the length of the string
#         count = 1                                   #variable "count" is set to 1
#         while (index < string_length -1) and (compressed_string[index] == compressed_string[index+1]): 
#             count = count + 1
#             index = index +1
#         if count == 1:
#             compressed += str(compressed_string[index])
#         else:
#             compressed += str(compressed_string[index]) + str(count)
#         index = index + 1
#     return compressed

#print(string_compression(example))
# we will need a variable to hold our current count
#need a varable to hold our final string = ""
#need a variable for last_character and this could start with the value of string[0]
# we can for loop over our string = we know this will loop over each individual letter 
# inside for loop we should have an if and an else = these will look at the previous letter to determine what to do
# if our current letter == our last letter then we would want to add to a counter 

# if letter == last_letter:
#   current_count += 1
# else:
# make a varable  += our str(current count) + last character variable
# reset counter to 0      counter variable = 0 
# set our last character variable to the current letter 

def compress_string(string_being_compressed):
    final_string = ''
    counter = 0
    previous_letter = ''
    character_count = 0
    string_length = len(string_being_compressed)
    for letter in string_being_compressed:
        counter += 1
        if previous_letter == '':
            previous_letter = letter
        else:

            if previous_letter == letter:
                character_count += 1
            else:
                character_count += 1
                final_string += str(character_count) + previous_letter
                character_count = 0
                previous_letter = letter

            if string_length == counter:
                character_count +=1
                final_string += str(character_count) + previous_letter
                
    print(final_string)

(compress_string(example))

def palindrome_finder(potential_palindrome):
    if potential_palindrome == reverse_a_string(potential_palindrome):
        print('It\'s a Palindrome!')
    else:
        print('Not a Palindrome!')

palindrome_finder(input('Please enter a word to check if it\'s a Palindrome.'))