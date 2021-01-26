import requests

resp = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/')

norte = 0
sul = 0
nordeste = 0
sudeste = 0
co = 0

for primaryResponse in resp.json():
    current = primaryResponse['regiao']['id']
    if current == 1:
        norte += 1
    elif current == 2:
        nordeste += 1  
    elif current == 3:
        sudeste += 1
    elif current == 4:
        sul += 1
    else:
        co +=1



f = open("csv/estados.csv", "w")
f.write("Região, Qtd. Estados\nNorte,{}\nNordeste,{}\nSudeste,{}\nSul,{}\nCentro Oeste,{}\n".format(norte, nordeste, sudeste, sul, co))
f.close()

print('norte = {} | sul = {} | nordeste = {} | sudeste = {} | centro oeste = {}'.format(norte, sul, nordeste, sudeste, co))