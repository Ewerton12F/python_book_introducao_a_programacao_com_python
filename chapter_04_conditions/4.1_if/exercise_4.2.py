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