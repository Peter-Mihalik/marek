from_n = int(input('zadaj od: '))
to_n = int(input('zadaj do: '))

string = ''
for i in range(from_n, to_n + 1):
    string += f'<{str(i)}> '
print(string)
