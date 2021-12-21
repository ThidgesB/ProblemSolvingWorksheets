#I'm still not sure exactly what a "Slice" is, but this formula iterates over letters designated by the integer(index position) within the brackets.
#since the integer is set to -1, it starts at the last letter in the string, and goes backwards one by one, and returns the string that way.
#if we were to change that number within the brackets to -2, with would skip every other letter in teh string, and return the letters it did not skip.
#I.E. [::-2] would print "suSka", however it always starts at the -1 index position. 
#a positive number would have a similar effect, however it always starts at Index position 0

def reverse_a_string(reversed_string):
    return reversed_string[::-1]

favorite_game = 'Dark Souls'

print(reverse_a_string(favorite_game))