word = input('zadaj slovo: ')
n = int(input('zadaj n: '))

number_of_spaces = 0
for i in range(0, n):
    number_of_spaces = i % 4*4
    print(' ' * number_of_spaces + word)
