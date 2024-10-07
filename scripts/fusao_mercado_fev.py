import json
import csv

# FAZENDO ETAPA DE EXTRAÇÃO (LEITURA)

# Lendo o arquivo json a partir da pasta data_raw através de uma função
path_json = 'data_raw/dados_empresaA.json'

def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json
dados_json = leitura_json(path_json)
print(dados_json[0])



# Lendo o arquivo csv a partir da pasta data_raw através de uma função
path_csv = 'data_raw/dados_empresaB.csv'

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv
dados_csv = leitura_csv(path_csv)
print(dados_csv[0])


# Lendo os arquivos por meio de apenas uma função
def leitura_dados(path, tipo_arquivo):
    dados = []
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
    return dados

dados_json = leitura_dados(path_json, 'json')
print(dados_json[0])


dados_csv = leitura_dados(path_csv, 'csv')
print(dados_csv[0])

# Função para trazer as colunas dos dados
def get_columns(dados):
    return list(dados[-1].keys())

nome_colunas_json = get_columns(dados_json)
print(f"Os nomes das colunas de dados_json são : {nome_colunas_json}")


nome_colunas_csv = get_columns(dados_csv)
print(f"Os nomes das colunas de dados_csv são : {nome_colunas_csv}")


# Criando novos dados csv com os nomes corrigidos

def rename_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv




# ETAPA DE TRANFORMAÇÃO DOS DADOS 

key_mapping = {
    'Nome do Item':'Nome do Produto',
    'ClassificaÃ§Ã£o do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja':'Filial',
    'Data da Venda': 'Data da Venda'
}


dados_csv = rename_columns(dados_csv,key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(f"Os nomes das colunas corrigidas de dados_csv são : {nome_colunas_csv}")


# Função para trazer o tamanho dos dados
def size_data(dados):
    return len(dados)

tamanho_dados_json = size_data(dados_json)
print(f"O tamanho dos dados_json é : {tamanho_dados_json}")

tamanho_dados_csv = size_data(dados_csv)
print(f"O tamanho dos dados_csv é : {tamanho_dados_csv}")

# Função para unir os dois conjuntos de dados dados_json + dados_csv
def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

dados_fusao = join(dados_csv,dados_json)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)
print(nome_colunas_fusao)
print(tamanho_dados_fusao)

# Função para tranformar os dados para formato de tabela

def transformando_dados_tabela(dados,nomes_colunas):

    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

# Carregamento dos dados

dados_fusao_tabela = transformando_dados_tabela(dados_fusao,nome_colunas_fusao)

path_dados_combinados = 'data_processed/dados_combinados.csv'

def salvando_dados(dados,path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(dados)

salvando_dados(dados_fusao_tabela,path_dados_combinados)

print(path_dados_combinados)