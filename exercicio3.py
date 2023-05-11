print('cauculadora versão 2.0')
n1 = int(input('informe o primeiro numero:'))
n2 = int(input('informe o segundo numero:'))
print(' + somar ')
print(' - subtração ')
print(' / dividir ')
print(' x multiplicar')
op = input(' escolha uma opção')
if op == '+':
    resultado = n1 + n2
    print(f'{n1} + {n2} = {resultado}')
if op == '-':
    resultado = n1 - n2
    print(f'{n1} - {n2} = {resultado}')
if op == '/':
    resultado = n1 / n2
    print(f'{n1} / {n2} = {resultado}')
if op == 'x':
    resultado = n1 * n2
    print(f'{n1} * {n2} = {resultado}')
