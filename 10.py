from_n = int(input('zadaj od: '))
to_n = int(input('zadaj do: '))

from_lenght = len(str(from_n)) - 1
number_of_spaces = len(str(to_n)) - 1

for i in range(from_n, to_n + 1):
    number_of_numbers =
    string = number_of_spaces * ' ' + \
        f'{str(i)}  {str(i**2)}  {str(i**3)}  {str(i**4)}'
    number_of_spaces -= 1
    print(string)
