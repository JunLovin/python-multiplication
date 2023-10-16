# Mini program in python

n = int(input("Write any number that you want to know multiplication table\n"))

for i in range(1,13):
    result = n * i
    print(f'{n} * {i} = {result}')