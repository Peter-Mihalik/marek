n = int(input('zadajte pocet: '))

# pi = '4'
# number_of_plus = 0
# number_of_minus = 1
# plus = 0
# minus = 1

# for i in range(3, n * 2, 2):
#     number_of_minus = minus % 2
#     number_of_plus = plus % 2
#     pi += number_of_minus*'-' + number_of_plus*'+' + '4/' + str(i)
#     plus += 1
#     minus += 1
#     print(pi)

pi = 4
multiplayer = -1

for i in range(3, n * 2, 2):
    number = multiplayer * 4/i
    pi += number
    multiplayer = - multiplayer
print(pi)
