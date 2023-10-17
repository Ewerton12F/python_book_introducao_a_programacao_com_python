# Python Book (PT-BR) - Introdução à Programação com Python

Python Programming Language

## Chapter 4 - Conditions

### 4.1 - If

[program_4.1.py](chapter_04_conditions/4.1_if/program_4.1.py)

```python
# Programa 4.1 - Lê dois valores e imprime qual é o maior

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print('O primeiro valor é o maior!')
if b > a:
    print('O segundo valor é o maior!')
if a == b:
    print('Os números são iguais!')
```

[program_4.2.py](chapter_04_conditions/4.1_if/program_4.2.py)

```python
# Programa 4.2 - Carro novo ou velho, dependendo da idade

idade = int(input('Digite a idade do seu carro: '))

if idade <= 3:
    print('Seu carro é novo')
if idade > 3:
    print('Seu carro é velho')
```

[exercise_4.2.py](chapter_04_conditions/4.1_if/exercise_4.2.py)

```python
# Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
# foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
# 80 km/h.

veloc = int(input('Informe a velocidade: '))

if veloc > 80:
    ultrap = veloc - 80
    multa = ultrap * 5
    print(f'Você ultrapassou a velocidade permitida em {ultrap}km e a multa é R${multa}')
if veloc <= 80:
    print(f'Você está no limite da velocidade!')
```

[program_4.3.py](chapter_04_conditions/4.1_if/program_4.3.py)

```python
# Programa 4.3 - Cálculo do Imposto de Renda

salario = float(input('Digite o salário para cálculo do imposto: '))
base = salario
imposto = 0

if base > 3000:
  imposto = imposto + ((base - 3000) * 0.35)
  base = 3000
if base > 1000:
  imposto = imposto + ((base - 1000) * 0.20)

print(f'Salário: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}')
```

[exercise_4.3.py](chapter_04_conditions/4.1_if/exercise_4.3.py)

```python
# Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
# e o menor.

n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
n3 = int(input('Informe o 3º número: '))

if n1 > n2:
    maior = n1
if n1 > n3:
    maior = n1

if n2 > n1:
    maior = n2
if n2 > n3:
    maior = n2

if n3 > n1:
    maior = n3
if n3 > n2:
    maior = n3

#

if n1 < n2:
    menor = n1
if n1 < n3:
    menor = n1

if n2 < n1:
    menor = n2
if n2 < n3:
    menor = n2

if n3 < n1:
    menor = n3
if n3 < n2:
    menor = n3

print(f'O número {maior} é o maior e o número {menor} é o menor.')
```

[exercise_4.4.py](chapter_04_conditions/4.1_if/exercise_4.4.py)

```python
# Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e
# calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule
# um aumento de 10%. Para os inferiores ou iguais, de 15%.


salario = float(input('Informe o salário: '))

if salario > 1250:
  sal_maior = salario + (salario * 0.1)
  print(f'O salário é maior que R$1.250,00. O novo salário será de R${sal_maior:6.2f}')
if salario < 1250:
  sal_menor = salario + (salario * 0.15)
  print(f'O salário é menor que R$1.250,00. O novo salário será de R${sal_menor:6.2f}')
```