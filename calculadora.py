# função para verificar se uma string é um número (tanto inteiro, negativo ou real)
def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

print('************************************** Python Calculator **************************************')
print('Selecione o número da operação desejada:')
print('\n1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

while True:
    opcao = input('Digite sua opção (1/2/3/4): ')
    if not opcao.isnumeric() or float(opcao) < 1 or float(opcao) > 5:
        continue

    while True:
        op1 = input('\nDigite o primeiro número: ')
        if not isnumber(op1):
            continue
        break

    while True:
        op2 = input('\nDigite o segundo número: ')
        if not isnumber(op2):
            continue
        break

    if opcao == '1':
        soma = float(op1) + float(op2)
        print('{0} + {1} = {2}'.format(op1, op2, soma))
        break

    if opcao == '2':
        sub = float(op1) - float(op2)
        print('{0} - {1} = {2}'.format(op1, op2, sub))
        break

    if opcao == '3':
        mul = float(op1) * float(op2)
        print('{0} * {1} = {2}'.format(op1, op2, mul))
        break

    if opcao == '4':
        div = float(op1) / float(op2)
        print('\n{0} / {1} = {2}'.format(op1, op2, div))
        break
