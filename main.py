import requests
import os

if not os.path.exists('images'):
    os.makedirs('images')
    print('A pasta images foi adicionada ao seu dispositivo!')

site = input('Url: ')
n_valor = int(input('quantidade de caracteres (ex. 000 = 3): '))
start = int(input('inicio: '))
end = int(input('fim: '))

if not 'https://' in site:
    if 'www.' in site:
        site = 'http://' + site
    else:
        site = 'http://www.' + site

count = 1

for i in range(start, end+1):
    try:
        resp = requests.get(f'{site}{i:0>{n_valor}}.jpg')

    except:
        print(f'Falha ao baixar a imagem! ({site}{i:0>{n_valor}}.jpg)')

    else:
        with open(f'images/{count:0>{n_valor}}.png', 'wb') as image:
            image.write(resp.content)

        print(f'Sucesso! ({site}{i:0>{n_valor}}.jpg)')
        count += 1
