# Loops com break

# exemplo 1

for numero in range(1, 11):
    if numero == 6:
       break
    else:
       print(numero)

print('Sai do Loop')
print('--------')

# exemplo 2

while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        break

print('----------')

for num in range(1, 11):
    if num == 6:
        continue  # pula
    print(num, end=" -> ")

print('\n----------')
