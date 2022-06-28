import pandas as pd
import datetime as dt
import csv

# ABERTURA E LEITURA DE ARQUIVO
dirTarifa = 'E:\\Google Drive\\Educação\\#BANCO DE DADOS\\Projeto\\Tarifa\\1-UTF8-tarifas-homologadas-distribuidoras-energia-eletrica.csv'
arqTarifa = open(dirTarifa,'rb')
textoTarifa = arqTarifa.read()  #lê em bytes
textoTarifa = str(textoTarifa, encoding='utf-8') #transforma os bytes de volta pra str

dadosTarifa = []
linhas = textoTarifa.split('\n')
for linha in linhas:
    colunas = linha.split(';')
    dadosTarifa.append(colunas)

# Salva e deleta linha de cabecalho
header = dadosTarifa[0]
del(dadosTarifa[0])

# Converte string de datas em objeto data
for i in range(len(dadosTarifa)-1,-1,-1):
    dadosTarifa[i][4] = dt.datetime.strptime(dadosTarifa[i][4],'%Y-%m-%d').date() #revisar numero coluna quando mudar arquivo fonte
    dadosTarifa[i][5] = dt.datetime.strptime(dadosTarifa[i][5],'%Y-%m-%d').date()
#converte numero para float
    dadosTarifa[i][15] = float(dadosTarifa[i][15].replace(',','.')) #revisar numero coluna quando mudar arquivo fonte
    dadosTarifa[i][16] = float(dadosTarifa[i][16].replace(',','.')) #revisar numero coluna quando mudar arquivo fonte
# Converte preco coluna
    if dadosTarifa[i][13] == 'R$/kW':
        dadosTarifa[i][15] = dadosTarifa[i][15]*1000
# Deleta linhas com DscBaseTarifaria = Base Economica
    if dadosTarifa[i][6] == 'Base Econômica' or dadosTarifa[i][14] != 'Não se aplica':
        del dadosTarifa[i]

# Deleta colunas desnecessárias
colunasDescartadas = [14, 13, 12, 11, 10, 9, 6, 1, 0] #de trás pra frente para manter os indices
for j in colunasDescartadas:
    del(header[j])
    for i in range(0,len(dadosTarifa)):
        del(dadosTarifa[i][j])

# Pivota Tabela
meses = pd.date_range('2018-01-01','2021-12-31',freq='MS').strftime("%Y-%m-%d").tolist() #DEFINIR JANELA DE TEMPO DA BASE DE DADOS AQUI
for i in range(0,len(meses)):
    meses[i] = dt.datetime.strptime(meses[i],'%Y-%m-%d').date() #transforma meses em objeto data para comparacao

dbTarifa = [[]]
k = 0
l = 1
for mes in meses:
    for i in range(0,len(dadosTarifa)-1):
        print(mes, i)
        if dadosTarifa[i][2] <= mes and dadosTarifa[i][3] >= mes:  #revisar numero coluna quando mudar arquivo fonte
            dbTarifa.append([]) # cria nova linha
            dbTarifa[k].append(l) # adiciona coluna ID
            l = l + 1
            dbTarifa[k].append(dt.datetime.strptime(mes.strftime('%Y-%m-%d'),'%Y-%m-%d').date()) # adiciona coluna mes
            for j in range(0,len(dadosTarifa[i])):
                dbTarifa[k].append(dadosTarifa[i][j]) # adiciona restante das colunas
            k = k + 1

header = ['id','Mes'] + header #atualiza para incluir as duas novas colunas

# SALVA NOVO CSV
dirNovoCsv = 'E:\\Google Drive\\Educação\\#BANCO DE DADOS\\Projeto\\Tarifa\\Tarifa.csv'
with open(dirNovoCsv, 'w', newline='',  encoding='utf-8') as arq:
    # usando metodo csv.writer do pacote CSV
    writer = csv.writer(arq, delimiter = ';')
    writer.writerow(header)
    writer.writerows(dbTarifa)