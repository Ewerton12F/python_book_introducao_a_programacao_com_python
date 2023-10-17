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

