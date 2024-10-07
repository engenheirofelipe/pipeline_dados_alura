#  Classe dados. Definir como vai ser construída, como sair da ideia para uma coisa real. Então tem que instanciar a classe em um objeto
import json
import csv

class Dados:

    def __init__(self,path,tipo_dados) :# Função para construir, Self é a maneira que o python representa o objeto. O objeto é representado pelo self. Alem disso o path vai ser usado no construtor e o tipo dos dados
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()

    # Lendo o arquivo json a partir da pasta data_raw através de uma função


    def leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json
 



    # Lendo o arquivo csv a partir da pasta data_raw através de uma função


    def leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv
  


    # Lendo os arquivos por meio de apenas uma função
    def leitura_dados(self):
        dados = []
        if self.tipo_dados == 'csv':
            dados = self.leitura_csv()
        elif self.tipo_dados == 'json':
            dados = self.leitura_json()

        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'
        return dados
    
    def get_columns(self):
        return list(self.dados[-1].keys())
    
    
    def rename_columns(self,key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        self.dados = new_dados
        self.nome_colunas = self.get_columns()

    def size_data(self):
        return len(self.dados)

       
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)

        return Dados(combined_list, 'list')

    def transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela
    
    def salvando_dados(self,path):
        dados_combinados_tabela = self.transformando_dados_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(dados_combinados_tabela)