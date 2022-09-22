n = int(input('zadaj n: '))

number_of_h = 1
number_of_spaces = n-2
print((n-1)*' ' + '*')
for riadok in range(0, n-2):
    print(number_of_spaces * " " + '*' + number_of_h * '-' + '*')
    number_of_spaces -= 1
    number_of_h += 2
print('*'*(n*2-1))
