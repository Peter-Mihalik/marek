n = int(input('zadaj n: '))

number_of_stars = 1
number_of_spaces = n-1
for riadok in range(0, n):
    print(number_of_spaces * " " + number_of_stars * '*')
    number_of_spaces -= 1
    number_of_stars += 2
