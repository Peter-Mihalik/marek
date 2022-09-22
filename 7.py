number = input('zadaj cislo: ')

position = 1
sum = 0
for i in number:
    print(f'{str(position)}. cifra {i}')
    sum += int(i)
    position += 1

print('ciferny sucet je ' + str(sum))
