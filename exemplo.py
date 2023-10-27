'''
Executar no terminal a instrução:
pip install requests
OU
py -3.11 -m pip install requests
'''
import requests

try:
    cep = input('Informe o CEP:')
    url = f'https://viacep.com.br/ws/{cep}/json/' 

    resposta = requests.get(url)        # realiza a requisição

    if resposta.status_code == 200:     # verifica o codigo de retorno: ok(200)
        dicionario = resposta.json()    # gera um dicionario a partir da resposta da API

        if 'erro' in dicionario:
            print('CEP inexistente')
        else:
            print(f'Rua: {dicionario["logradouro"]}')
            print(f'Complemento: {dicionario["complementpo"]}')
            print(f'Bairro: {dicionario["bairro"]}')
            print(f'Cidade: {dicionario["localidade"]}')
            print(f'Estado: {dicionario["uf"]}')

    
    elif resposta.status_code == 400:       # Bad request
        print('ERRO:o cep deve ter 8 caracteres')

except ConnectionError:
    print('ERRO: não foi possível conectar a API')
except Exception as mensagem:
    print(f'ERRO: {mensagem}')