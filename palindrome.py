phrase_input = input("Please enter a phrase here: ")
all_letters = "abcdefghijklmnopqrstuvwxyz"
no_chars = []
for letter in phrase_input.lower():
    if letter in all_letters:
        no_chars.append(letter)
reverse = no_chars[::-1]

if no_chars == reverse:
    print(phrase_input + " is a palindrome! 😃  Good for you!")
else:
    print(phrase_input + " is not a palindrome! 😔  Try again!")
    
    ## code did not work with non alphanumeric characters##
    # lowercase = (phrase_input.lower())
    # no_space = str(lowercase.replace(" ", ""))
    # no_chars = re.sub().no
    # reverse = str(no_space[::-1])