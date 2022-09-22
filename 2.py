word = input('zadaj slovo: ')
number_of_letters = 1
for letter in word:
    print(letter * number_of_letters)
    number_of_letters += 1
