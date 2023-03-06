medias_carros = {
    'BMW': {'gasolina': 9.8, 'alcool': 8.9},
    'AUDI': {'gasolina': 12.8, 'alcool': 10.9},
    'FIAT': {'gasolina': 26.8, 'alcool': 24.9},
    'FERRARI': {'gasolina': 13.8, 'alcool': 12.9}
}


reducoes_casos = {
    '4_portas': 0.5,
    '2_pessoas': 1.2,
    'bagageiro': 0.2
}


tipo_carro = input('Qual é o tipo do carro? (BMW, AUDI, FIAT ou FERRARI) ')
tipo_combustivel = input('Qual é o tipo de combustível? (gasolina ou alcool) ')
qtd_portas = int(input('Quantas portas o carro tem? '))
qtd_pessoas = int(input('Quantas pessoas vão viajar no carro? '))
tem_bagageiro = input('O carro tem bagageiro? (sim ou nao) ')


media_carro = medias_carros[tipo_carro][tipo_combustivel]


if qtd_portas > 4:
    media_carro -= reducoes_casos['4_portas']

if qtd_pessoas > 2:
    media_carro -= reducoes_casos['2_pessoas']

if tem_bagageiro == 'sim':
    media_carro -= reducoes_casos['bagageiro']


print(f'Tipo de combustível: {tipo_combustivel}')
print(f'Tipo de carro: {tipo_carro}')
print(f'Tipos de casos: {"-".join([k for k, v in reducoes_casos.items() if v != 0])}')
print(f'KM que o carro fará: {1/media_carro:.2f} km/L')