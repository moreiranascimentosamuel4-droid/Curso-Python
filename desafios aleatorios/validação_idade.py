from datetime import datetime

idade = int(input('Qual a sua idade? '))
data = input('Digite sua data de nascimento (dd/mm/aaaa): ')

# Converter a string em data real
data_nasc = datetime.strptime(data, "%d/%m/%Y")

# Data limite (31/12/2007)
limite = datetime.strptime("31/12/2007", "%d/%m/%Y")

if idade < 18:
    if data_nasc <= limite:
        print(f'Você digitou que sua idade era {idade} mas na verdade é maior de idade')
    else:
        print(f'Você digitou que sua idade era {idade} e você realmente é menor de idade')
else:
    if data_nasc <= limite:
        print(f'Você digitou que sua idade era {idade} e você realmente é maior de idade')
    else:
        print(f'Você digitou que sua idade era {idade} mas na verdade é menor de idade mentiroso!!')