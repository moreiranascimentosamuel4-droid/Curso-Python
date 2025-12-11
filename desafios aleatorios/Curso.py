idade = int(input('Qual a sua idade? '))
#cpf = int(input('e seu cpf : '))

data = (input('digite a sua data de nascimento: '))
if idade < 18:
 if data <= '31/12/2007':
     print(f'Você digitou que sua idade era {idade} mas na verdade é maior')
 else:
      print(f'Você digitou que sua idade era {idade} e você realmente é menor')
else:
    if data <= '31/12/2007':
     print(f'Você digitou que sua idade era {idade} e você realmente é maior')
    else:
      print(f'Você digitou que sua idade era {idade} mas na verade é menor mentiroso!!')
#conferir cpf para puxar a idade e ver se é maior ou menor.
