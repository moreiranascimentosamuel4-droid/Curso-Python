("Exercicio-1")
#print ('Olá mundo')

("Exercio-2")
# nome= input ('Seja Bem vindo,Qual o seu nome?')
#print ( 'É um prazer te conhecer!!, {} !' .format (nome))

("Exercicio-3")
#print ('--__desaio= soma__--_')
#ni1=  int (input ('Digite um numero'))
#ni2= int (input('Digite um numero'))

#soma = ni1 + ni2
#print ( 'a soma dos numeros é',soma )
"ou"
#print("a soma dos numeros {} e {} vale = {}".format(ni1,ni2,soma))
 
#Números#
# num=(int) = -7,7,-87
# num=(float) = 6.4,6.34,7.0
# num=(bool) = True,False
# num=(str) = ('Texto, ex:Olá')

'Exemplos'
(1)
#n= input ('Digite algo :') 
#print(n.isnumeric())
#confere se é numero ou não
(2)
#oi= input ('Digite algo :')
#print(oi.isalpha())
#confere se é letra
(3)
#opa3= input ('Digite algo:')
#print(opa3.isalnum())
#confere se é letra e numero junto
(4)
#opa= input ('Digite algo:')
#print(type(opa.isupper()))
#confere se esta maiusculo
(5)
#n = input('Digite algo: ')
#print(n.islower())
# Confere se está todo em minúsculas
(6)
#n = input('Digite algo: ')
#print(n.istitle())
# Confere se está no formato de título (Ex: “Python é Bom”)- ou Capitalizada
(7)
#n = input('Digite algo: ')
#print(n.isspace())
# Confere se contém apenas espaços em branco
(8)
#n = input('Digite algo: ')
#print(n.isdecimal())
# Confere se é decimal (números sem sinal nem ponto)
(9)
#n = input('Digite algo: ')
#print(n.isdigit())
# Confere se contém apenas dígitos (parecido com isnumeric)
(10)
#n = input('Digite algo: ')
#print(type(n))
# Mostra o tipo do dado digitado (sempre será string com input())
(11)
#n = input('Digite um número: ')
#n = int(n)  # converte para inteiro
#print(type(n))
# Mostra que agora é <class 'int'>
(12)
#txt = "Olá"  
#print(txt.isascii())
# ❌ False — o “á” NÃO faz parte da tabela ASCII



('Exercicio-4')
#print('_--_Desafio 04_--_')
#opa= input ('Digite algo:')
#print('O tipo primitivo desse valor é:', type(opa))
#print('Ele é uma letra ?', opa.isalpha())
#print('Ele é numerico ?',opa.isnumeric())
#print('Ele está maiusculo?',opa.isupper())
#print('Ele contem apenas espaços  ?', opa.isspace())
#print('Ele esta na escala ascii ?', opa.isascii())
#print('Está capitalizado ?',opa.istitle())
#"ou fazer todos eles com o format"
#n = input('Digite algo: ')
#print('Ele é um numero ? {}'.format(n.isnumeric())
 

('Operadores Aritméticos')
#+ - Adição 
#- - Subtração
#* - Multiplicação
#/ - Divisão 
#** - Potencia
#// - divisão inteira 
#% - Resto da divisão

"Ordem de precedencia"
(1)
'()'
'Resolve os parenteses'
(2)
'**'
'Resolve as potencias'
(3)
'*,/,//,%'
'Resove a multiploicação ou subtração ou divisão real ou a sobra da divisão'
(4)
'+,-'
'Resolve a soma ou subtração'

('Exemplo - 1')
(5+3*2 == 11)
#f= int(input(5+3*2))
#print(f)

('Exemplo - 2')
(3*5+4**2==31)
#s=int(input(3*5+4**2))
#print(s)

('Exemplo - 3')
(3*(5+4)**2==243)
#v=(3*(5+4)**2)
#print(v)
'outra forma de fazer Potencia'
#print(pow(4,3))

'Raíz Quadrada'
#g=int(input(144**(1/2)))
#print(g)

'Raíz Cubica'
#h=int(input(127**(1/3)))
#print(h)

'formas do format'
(1)
#nome= input('qual o seu nome ?')
#print('prazer em conhecer você {:20}!'.format(nome))
'cria um espaço entre os caracteres de 20 linhas'
(2)
#noma= input('qual o seu nome ?')
#print('prazer em conhecer você {:>20}!'.format(noma))
'Cria um espaço a direita do nome de 20 linhas'
(3)
#nome= input('qual o seu nome ?')
#print('prazer em conhecer você {:<20}!'.format(nome))
'Cria um espaço a esquerda'
(4)
#nome= input('qual o seu nome ?')
#print('prazer em conhecer você {:^20}!'.format(nome))
'Centraliza'
(5)
#nome= input('qual o seu nome ?')
#print('prazer em conhecer você {:=^20}!'.format(nome))
'Alem de centralizar coloca o sinal de igual em volta, ou outro sinal que vc colocar'


'Exemplos'
#del int
#n= int(input("Digite um número:"))
#sn2=int(input ('digite outro: '))
#so= n+sn2
#m= n*sn2
#d=n/sn2
#di=n//sn2
#po=n**sn2
#raíz=n**(1/2)
#print('OS resultados são, soma: {}, multiplicação :{}, divisão: {}, divisão inteira: {},potencia: {},raíz: {}'.format(so,m,d,di,po,raíz))
()
'(\n) - quebra a linha'

('Exercicio 5')
#del int
#no= int(input("Digite um número:"))
#print( 'analisando o valor de {}, seu antecessor é {} e seu sucessor é {}'.format(no,no -1, no +1))
'antecessor e sucessor'
('Exercicio 6')
#del int
#na= int(input("Digite um número:"))
#print('o Dobro é {} \n o Triplo  é {}\n e a Raís é {:.2f}'.format(na *2 ,na *3, na**(1/2) ))
'calcula o dobro o triplo e a raíz'
(':.2f- coloca o tanto de numeros que quero após a virgula')

('Exercicio 7')
#del int
#no= int(input("Digite um número:"))
#ni= int(input("Digite um número:"))
#print( ' Juntanto {}, e  {} A media é {:.1f}'.format(no,ni, (no+ni)/2))
'calcula a media'
('Exercicio 8')
#no=float(input ('digite uma distancia em metros:'))
#print( 'em centimetros {}\n e em milimetros {}\n e em km {} \n em hectômetro {}\n em decâmetro{} \n em decímetro {}'.format(no *100 ,no *1000,no /100,no /100 , no /10,no *10)) 
'transforma de cm ou m para os oustros metodos de medida'
('Exercicio 9')
#tabuada=int(input('digite um número e veja a sua tabuada:'))
#print('{} x {} = {}'.format(tabuada,1, tabuada*1))
#print('{} x {} = {}'.format(tabuada,2, tabuada*2))
#print('{} x {} = {}'.)format(tabuada,3, tabuada*3))
#print('{} x {} = {}'.format(tabuada,4, tabuada*4))
#print('{} x {} = {}'.format(tabuada,5, tabuada*5))
#print('{} x {} = {}'.format(tabuada,6, tabuada*6))
#print('{} x {} = {}'.format(tabuada,7, tabuada*7))
##print('{} x {} = {}'.format(tabuada,8, tabuada*8))
#print('{} x {} = {}'.format(tabuada,9, tabuada*9))
#print('{} x {} = {}'.format(tabuada,10, tabuada*10))
#print('-----_______---')
'Tabuada'

('Exercicio 10')
#dinheiro= float(input('digite sua quantia em R$'))
#print('Vc tem em em Dolar o valor de US${:.2f}'.format(dinheiro *0.1846))
'transforma de R$ para USD$'
('Exercicio 11')
#altura=float(input('Digite a altura dessa parede:'))
#largura=float(input('Agora a largura:'))
#metros=altura*largura
#print('O tamanho em Metros Quadrados é {:.0f} m² \n Então você usara {:.0f} litros.'.format(metros,metros/2))
'Calcula a area'
('Exercicio 12')
#produto=float(input('Qual o preço do seu produto ? R$'))
#desconto=produto - (produto * 25/100)
#print('O produto que custava R${:.2f},com o desconto de 25% ficou R${:.2f}'.format(produto,desconto))

('Exercicio 13')
#salario=float(input('Qual o valor do se salario ? R$'))
#aumento=salario + (salario*16/100)
#print('o salario que era R${:.2f}, com 16% de aumento agora está valendo R$ {:.2f}'.format(salario,aumento))

('Praticando o Exercicio 12 -13')
#valor=float(input('Qual o valor do Produto ? R$'))
#vista= valor -(valor*50/100)
#parcelado= valor + valor*15/100
#parcela=parcelado- parcelado* 50/100
#print('Se for a vista tera um desconto de 50% e tera o valor de R${:.2f}, mas se for parcelado tera um aumento de 15% e saíra com o valor de R${:.2f}\n se for parcelado em 2x pagara o valor de R${:.2f} por mês.'.format(vista,parcelado,parcela))
'os três calcula porcentagem'
('Exercicio 14')
#graus=float(input('Digite a temperatura em °C:'))
#firenit= (graus*9/5) +32
#print('A temperatura que era {:.1f} °C, Agora está {:.1f} °F'.format(graus,firenit))
"Calcula a temperatura"

('Exercico 15')
#aluguel=int(input('Quantos dias você está com o carro ?'))
#rodado=float(input('E quantos km você rodou ? '))
#print('O valor a se pagar é R${:.2f}'.format(aluguel *60 + rodado *0.15 ))
'Calcula o valor de aluguel'

('From e Import')
#import doce 'doce = Biblioteca'
'Ele importa uma biblioteca'
#from doce import pudim
'Importa a biblioteca mas puxa um item em expecifico da blibioteca'
'math = biblioteca de matematica'
('modulos de math ')
'ceil = arredonda para cima'
'floor = arredonda para baixo'
'trunc = elimina da virgula para frente'
'pow = potencia'
'sqrt = raíz quadrada'
'factorial = fatorial'
('utilizabdo a biblioteca')
#import math
#print(math.ceil(8.5))
'Importa a Biblioteca'
#from math import sqrt
#print(sqrt(16))
'Importa a biblioteca mas eu consigo utilizar apenas oq eu quero'
#from math import sqrt, ceil
#print(sqrt (144))
#print(ceil(132.8))
'já esse importa a biblioteca + os modulos que eu escolher'
#import math
#num=int(input('Digite um numero:'))
#print(' a raiz do numero {} é {:.0f}'.format(num,math.sqrt(num)))
'metodo mais facil de se fazer a conta' 
#import math
#numero=int(input('Digite um numero:'))
#raiz=math.sqrt(numero)
#print('a raíz do número {} é {}'.format(numero,math.floor(raiz)))
'Arredonda a raiz se ela for dar um numero com virgula para menor ex=6,55 para 6'
#import math
#numero=int(input('Digite um numero:'))
#raiz=math.sqrt(numero)
#print('a raíz do número {} é {}'.format(numero,math.ceil(raiz)))
'Arredonda a raiz se ela for dar um numero com virgula para maior ex=6,55 para 7'

#import emoji
#print (emoji.emojize("Ola, mundo :snake:"))
'Este importa a biblioteca de emojis'
#import emoji
#print(emoji.EMOJI_DATA.keys())
'Printa o nome de alguns emojis'

('Exercicio 16')
#import math
#numero=float(input("digite um numero com virgula:"))
#print('O valor inteiro desse numero é {}'.format(math.trunc(numero)))
'transforma de um numero com virgula pra inteiro'
'ou'
#numero=float(input("digite um numero com virgula:"))
#print('O valor inteiro desse numero é {}'.format(int(numero)))
'Esse faz o exercicio sem importar biblioteca'

('Exercicio 17')
#from math import sqrt
#co=float(input('Digite o valor do cateto oposto:'))
#ca=float(input('Digite o valor do cateto adjacente:'))
#hi=(co**2+ca**2)
#print('O valor da hipotenusa é {:.2f}'.format(sqrt(hi)))
'ou'
#from math import hypot,pow
#cateto=float(input('Digite o valor do cateto oposto:'))
#cateta=float(input('Digite o valor do cateto adjacente:'))
#hipotenusa= hypot(cateto,cateta)
#print('O valor da hipotenusa é {:.2f}'.format( hypot(hipotenusa)))
'ou'
#from math import hypot
#ca=float(input('Digite um valor:'))
#co=float(input('Digite outro:'))
#print('o valor de hipotenusa é {:.2f}'. format(hypot(ca,co)))
'ou'
#from math  import sqrt,pow
#ca=float(input("Digite um valor: "))
#co=float(input('Digite outro: '))
#hi = sqrt(pow(ca,2) + pow(co,2))
#print('O valor da hopotenusa é {:.2f}'.format(hi))

('mais um exemplo da atividade 17')
#from math import hypot
#ca=float(input('Digite um valor: '))
#co=float(input('Digite outro valor: '))
#hi1=hypot(ca,co)
#cateto=float(input('Digite mais o valor do cateto oposto: '))
#cateta=float(input('Digite agora o valor do cateto adjacente: '))
#hi2= hypot(cateto,cateta)
#hi3= hypot(cateta,ca)
#hi4= hypot(cateto,co)
#print('O resultado da hipotenusa é {:.2f}\n e da segunda é {:.2f} \n e o resultado entre cateto adjacente é {:.2f} e entre os catetos opostos é {:.2f}'.format(hi1,hi2,hi3,hi4))
'Cateto oposto, Catateto adjacente e Hipotenusa'

('Exercicio 18')
#from math import sin,cos,tan,radians
#angulo=int(input('Digite o valor do angulo :'))
#rad= radians(angulo)

#if angulo ==30:
# print('o seno de 30 é {:.2f} ' .format(sin(rad)))
# print('o cosseno de 30 é {:.2f}' .format(cos(rad)))
# print('e a tangente de 30 é {:.2f}'.format(tan(rad)))

#elif angulo ==45:
# print('o seno de 45 é {:.2f} ' .format(sin(rad)))
# print('o cosseno de 45 é {:.2f}' .format(cos(rad)))
# print('e a tangente de 45 é {:.2f}'.format(tan(rad)))

#elif angulo ==60:
# print('o seno de 60 é {:.2f} '.format(sin(rad)))
# print('o cosseno de 60 é {:.2f}' .format(cos(rad)))
# print('e a tangente de 60 é {:.2f}'.format(tan(rad)))

#else:
# print('digite um angulo valido')

'ou'
#from math import radians, sin,cos,tan
#angulo= float(input('Digite um angulo: '))
#rad=radians (angulo)
#sen= sin( radians(angulo))
#cose= cos( radians(angulo))
#tag= tan( radians(angulo))
#print('o angulo {} tem o resultado do seno {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(angulo,sen,cose,tag))

'ou'
#from math import radians, sin,cos,tan
#angulo= float(input('Digite um angulo: '))
#rad=radians (angulo)
#print('o angulo {} tem o resultado do seno {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(angulo,sin(radians(angulo)),cos(radians(angulo)), tan(radians(angulo))))
'Seno, Cosseno e Tangente'

('Exercicio 19')
#import random
#al1=input('aluno 1- ')
#al2=input('aliuno 2 -')
#al3=input('aluno 3- ')
#al4=input('aluno 4- ')
#alunos=[al1,al2,al3,al4]
#print('O aluno sorteado é {}'.format(random.choice(alunos)))
'ou'
#from random import choice
#al1=input('aluno 1- ')
#al2=input('aliuno 2 -')
#al3=input('aluno 3- ')
#al4=input('aluno 4- ')
#alunos=[al1,al2,al3,al4]
#print('O aluno sorteado é {}'.format(choice(alunos)))
'Sorteia um aluno'

('Exercicio 20')
#from random import shuffle
#nome1=input('Digite um nome para a ordem de apresentação : ')
#nome2=input('Digite outro : ')
#nome3=input('Digite mais um : ')
#nome4=input('mais um por favor : ')
#lista=[nome1,nome2,nome3,nome4]
#shuffle(lista)
#print('A ordem sorteada foi {}'.format(lista))
'não retorna nada ele apenas muda a lista original por isso quando a printamos novamente está alterada'

('ex')
#nome1=input('Digite um nome para a ordem de apresentação : ')
#nome2=input('Digite outro : ')
#nome3=input('Digite mais um : ')
#nome4=input('mais um por favor : ')
#lista=[nome1,nome2,nome3,nome4]
#print('A ordem sorteada foi {}'.format(sorted(lista)))
'Cria uma nova lista sem alterar a original'

('Exercicio 21')
#import pygame 
#import time
#pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load('jesus.mp3')
#pygame.mixer.music.play()
#print("Tocando música...")
#while pygame.mixer.music.get_busy():
 #time.sleep(1)
#print('A musica acabou...')

('Aula 09')
'ex'
#frase='Curso em video python'
#print(frase[1:6:2])
('Fatiamneto')
'escolhe oq vai printar e pula de dois em dois'
'print(frase(:5))'
'printa do 0 até a linha escolhida'  
'print(frase(15:))'
'printa da linha escolhida até o final'
'print(frase(15:;3))'
'printa da linha escolhida até o final e pula de 3 em 3'
('Análise')
'len(frase)'
'Mostra o comprimento da frase'
#frase.count('o')
'conta quantos letras ou palavras tem na str'
#frase.count('s,0,13')
'conta a letra ou frase das linhas que vc deseja, faz o fatiamento'
('Importante')
'no fatiamento o ultimo caratere é ignorado'
#frase.find('deo')
'identica quantas vezes esse conjunt foi utilizado dentro da str, e mostra onde ela foi iniciada'
#frase.find('android')
'analisa oq vc mandou e te retorna -1 pois não foi encontrado'
#curso in frase
'Identifica se tem a palavra pedida dentro da str, ele apenas diz se tem ou não e retorna true ou false'
('Transformação')
#frase.replace('Python','Android')
'troca a primeira palavra pela segunda que foi escolhida'
#frase.upper('eu')
'pega oq foi selecionado e transforma tudo em maisculo'
#frase=('EU Sou legal')
#frase=frase.lower()
#print(frase)
'pega oq foi selecionado e transforma em minusculo'
#frase.capitalize()
'Pega a frase deixa ela toda em minusculo e apenas a primeira letra em maisculo'
#frase.title()
'Diferente do capitalize, ele analiza a str e a primeira letra de todas as frases escritass(ele analisa atravez dos espaços)'
#frase.stip()
'remove todos os espacos que não são utilizados'
#frase.rstrip()
'Faz quase a msm coisa soq só tira os espaços a direita da str'
#frase.lstrip()
'Faz quase a msm coisa soq só tira os espaços a esquerda da str'
('Divisão')
#frase.split()
'divide a str, e meio que faz como se elas fossem divididas em outras listas(divide por palavras, a str não é mais uma palavta só)'
('ex split')
#frase = "Aprender Python é divertido"
#palavras = frase.split()        ['Aprender', 'Python', 'é', 'divertido']
#'-'.join(frase)
'Junta novamente a str e coloca o - para separa-las'
('Alguns exemplos')
#frase=('Curso em Video')
#print(frase.upper().count('O'))
'transforma a frase em maiusculo e conta quantos O tem nela'
#frase=('   Curso em Video    ')
#print(len(frase.strip()))
'conta quantos caractereres que tem a frase se contar os espaços que não são utilizados'
#frase=('curso em video')
#frase= frase.replace('curso','video')
#print(frase)
'altera a str original'
#print(frase.replace('video', 'curso'))
'enquanto esse só faz uma mudança, mas a original continua a msm'
#frase='Olá eu sou o Samuel'
#dividido=frase.split()
#print(dividido[0])
'divide e printa aquilo que eu escolher'
#juntar='_'.join(dividido)
#print(juntar)
'junta novamente e coloca _ entre as frases'
#frase=('Olá oi olá')
#dividido=frase.split()
#print(dividido[2] [1])
'seleciona a frase e mostra a letra escolhida'

('Praticando um pouco')
#from math import radians,sin,cos,tan
#numero=int(input('Digite um angulo : '))
#rad=radians(numero)
#print('''o seno é {:.1f}
#o cosseno é {:.1f} 
#e a tangente {:.1f}''' .format(sin(rad),cos(rad),tan(rad)))

('Exercicio 22')
#nome=str(input('Digite seu nome completo : ')).strip()
#mais=nome.upper()
#min=nome.lower()
#print('analizando seu nome...\n Seu nome Maisculo é {}\nMinusculo é {}'.format(mais,min))
#print('Tem {} letras ao total'.format(len(nome)-nome.count(' ')))
#split=nome.split()
#print('Seu primeiro nome {} tem {} letras'.format(split[0],len(split[0])))

('exercicio 23')
#numero=int(input('Digite um numero : '))
#print('Analizando o número {}:'.format(numero))
#print('Unidade {}'.format(numero //1 %10))
#print('Dezena {}'.format(numero //10 %10))
#print('Centena {}'.format(numero //100 %10))
#print('Milhar {}'.format(numero //1000 %10))

('Exercicio 24')
#cidade=('Curitiba')#pergunta=str(input('Qual cidade você nasceu ? ')).strip()
#if pergunta.lower() == cidade.lower():
# print('True')
#else:
#print('False')
'Meu jeito'
#cid=input('Em qual cidade você nasceu ? ' ).strip()
#print(cid[:8].upper() == 'CURITIBA')
'Jeito do Gustavo Guanabara'

('Desafio chat')
#nome=input('Digite o seu nome : ')
#idade=input('Digite a sua idade : ')
#prim=float(input('Digite a primeira nota: '))
#seg=float(input('Digite a segunda nota : '))

#print(f"\nNome: {nome}\nIdade: {idade}\nPrimeira nota: {prim}\nSegunda nota: {seg}")
#notas = (prim, seg)
#print(f"Notas: {notas}")
#media = (prim + seg) /2
#print(media)
#if media >= 7.0:
    #print("Aprovado")
#else:
    #print("Reprovado")