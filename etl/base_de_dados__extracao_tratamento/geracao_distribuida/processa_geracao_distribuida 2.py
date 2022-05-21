from .modelo_geracao_distribuida import ModeloGeracaoDistribuida

import csv
import os
import sys


class ProcessaDadosGeracaoDistribuida:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def executa(self):
        conteudo_csv = []
        with open(self.caminho_arquivo, 'r', encoding='utf-16') as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=';')
            for i, linha in enumerate(arquivo_csv):
                if i ==  0:
                    # Linha de cabeçalho. Passo reto.
                    continue
                modelo_geracao = ModeloGeracaoDistribuida.from_linha_csv(linha)
                conteudo_csv.append(modelo_geracao)


if __name__ == '__main__':
    file_path = sys.argv[1][0]
    processador = ProcessaDadosGeracaoDistribuida(file_path)
    processador.executa()
