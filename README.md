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
