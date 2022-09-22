n = int(input('zadaj n: '))

string = '* '
number_of_stars = 2
for i in range(1, n):
    string += number_of_stars * '*' + ' '
    number_of_stars += 1

print(string)
