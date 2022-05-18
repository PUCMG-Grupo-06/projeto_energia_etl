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
del(dadosTarifa[0])

# Converte string de datas em objeto data
for i in range(0,len(dadosTarifa)-1):
    dadosTarifa[i][4] = dt.datetime.strptime(dadosTarifa[i][4],'%Y-%m-%d').date() #revisar numero coluna quando mudar arquivo fonte
    dadosTarifa[i][5] = dt.datetime.strptime(dadosTarifa[i][5],'%Y-%m-%d').date()
#converte numero para float
    dadosTarifa[i][15] = float(dadosTarifa[i][15].replace(',','.')) #revisar numero coluna quando mudar arquivo fonte
    dadosTarifa[i][16] = float(dadosTarifa[i][16].replace(',','.')) #revisar numero coluna quando mudar arquivo fonte
# Converte preco coluna
    if dadosTarifa[i][13] == 'R$/kW':
        dadosTarifa[i][15] = dadosTarifa[i][15]*1000
        
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
        if dadosTarifa[i][4] <= mes and dadosTarifa[i][5] >= mes:  #revisar numero coluna quando mudar arquivo fonte
            dbTarifa.append([])
            dbTarifa[k].append(l)
            l = l + 1
            dbTarifa[k].append(dt.datetime.strptime(mes.strftime('%Y-%m-%d'),'%Y-%m-%d').date())
            for j in range(2,len(dadosTarifa[i])):
                dbTarifa[k].append(dadosTarifa[i][j])
            k = k + 1

##SAVE TO CSV
# field names 
fields = ['id','Mes','DatGeracaoConjuntoDados','DscREH', 'SigAgente',
          'NumCNPJDistribuidora', 'DatInicioVigencia', 'DatFimVigencia',
          'BaseTarifaria', 'DscSubGrupo', 'DscModalidadeTarifaria',
          'DscClasse', 'DscSubClasse', 'DscDetalhe', 'NomPostoTarifario',
          'UnidadeTerciaria', 'SigAgenteAcessante', 'VlrTUSD', 'VlrTE']
# data rows of csv file
dirNovoCsv = 'E:\\Google Drive\\Educação\\#BANCO DE DADOS\\Projeto\\Tarifa\\Tarifa.csv'
with open(dirNovoCsv, 'w', newline='',  encoding='utf-8') as arq:
    # using csv.writer method from CSV package
    writer = csv.writer(arq, delimiter = ';')
    writer.writerow(fields)
    writer.writerows(dbTarifa)
    




 
