import pandas as pd
def doRenda(pfEnade):
    dicRenda = doRendaDIC()
    pfEnade['RendaDIC'] = [dicRenda[x] for x in pfEnade.QE_I08]
    return pfEnade

def doEscolaridade(pfEnade):
    # TRATAR - ESCOLARIDADe dos pais - Categóricos
    pfEnade['EPai'] = pfEnade['QE_I04'].cat.codes  # Cria um grupo numérico a partir do categórica
    
    # DICIONARIO ESCOLARIDADE DO PAI
    dicEscolaridade = {'A' : 'Nenhuma',
    'B' : 'Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série)',
    'C' : 'Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série)',
    'D' : 'Ensino Médio',
    'E' : 'Ensino Superior - Graduação',
    'F' : 'Pós-graduação',
    ' ' : 'Não Informado'}

    pfEnade['EscolaridadeDesc'] = [dicEscolaridade[x] for x in pfEnade.QE_I04]
    return pfEnade

def mapear_coluna(df, data_dict, coluna):
    tmp = data_dict.query("NOME == @coluna")['CATEGORIAS'].str.split('=', expand=True).dropna()
    if tmp.shape[0] <= 1: #work-around for NU_IDADE
        return {i:i for i in sorted(df[coluna].unique())}
        
    tmp.iloc[:, 0] = tmp.iloc[:, 0].str.strip().astype(df[coluna].dtype)
    tmp.iloc[:, 1] = tmp.iloc[:, 1].str.strip().str.upper()
    return tmp.set_index(0).iloc[:,0].to_dict()
    
def doRendaDIC():
    # DICIONÁRIO - Renda
    dicRenda = {'A' : '< 1,5 salary',
    'B' : '1,5 to 3 salary',
    'C' : '3 to 4,5 salary',
    'D' : '4,5 to 6 salary',
    'E' : '6 to 10 salary',
    'F' : '10 to 30 salary',
    'G' : '> 30 salary'  } 
    return dicRenda

def doQE_I08DIC():
    # DICIONÁRIO - Renda
    dicRenda = {'< 1,5 salary','1,5 to 3 salary','3 to 4,5 salary','4,5 to 6 salary','6 to 10 salary','10 to 30 salary','> 30 salary'  } 
    return dicRenda

    #dicRenda = {'A' : 'Até 1,5 salário mínimo (até R$ 1.431,00)',
    #'B' : 'De 1,5 a 3 salários mínimos (R$ 1.431,01 a R$ 2.862,00)',
    #'C' : 'De 3 a 4,5 salários mínimos (R$ 2.862,01 a R$ 4.293,00)',
    #'D' : 'De 4,5 a 6 salários mínimos (R$ 4.293,01 a R$ 5.724,00)',
    #'E' : 'De 6 a 10 salários mínimos (R$ 5.724,01 a R$ 9.540,00)',
    #'F' : 'De 10 a 30 salários mínimos (R$ 9.540,01 a R$ 28.620,00)',
    #'G' : 'Acima de 30 salários mínimos (mais de R$ 28.620,00)'
    #' ' : 'Não Informado'}
  
def doHEstudoDIC():
    # DICIONÁRIO - Horas de Estudo
    dicHEstudo = {'A' : 'None',
    'B' : '1 to 3',
    'C' : '4 to 7',
    'D' : '8 to 12',
    'E' : '> 12',
    ' ' : 'Não Informado'}
    return dicHEstudo

    #dicHEstudo = {'A' : 'Nenhuma, apenas assisto às aulas',
    #'B' : 'De uma a três',
    #'C' : 'De quatro a sete',
    #'D' : 'De oito a doze',
    #'E' : 'Mais de doze',
    #' ' : 'Não Informado'}
    
def doSexoDIC():
    # DICIONÁRIO - Sexo
    dicSexo = {'M' : 'Male', 'F' : 'Female'}
    return dicSexo

def doMigradoDIC():
    # Migrad
    dicMigrado = {'0' : 'Nativo', '1' : 'Migrante'}
    return dicMigrado

def doPublicaDIC():
    # Publica / privada
    dicPublica = {'0' : 'Public', '1' : 'Private'}
    return dicPublica
    
def doCategoricos(pfEnade):
    # Cria um grupo numérico a partir do categórica
    # pfEnade['QE_I08CAT'] = pfEnade['QE_I08'].sort_values(by=['QE_I08']).cat.codes  # Cria um grupo numérico a partir do categórica
    pfEnade['QE_I08CAT'] = 0
    pfEnade.loc[pfEnade['QE_I08'] == 'A', 'QE_I08CAT'] = 1
    pfEnade.loc[pfEnade['QE_I08'] == 'B', 'QE_I08CAT'] = 2
    pfEnade.loc[pfEnade['QE_I08'] == 'C', 'QE_I08CAT'] = 3
    pfEnade.loc[pfEnade['QE_I08'] == 'D', 'QE_I08CAT'] = 4
    pfEnade.loc[pfEnade['QE_I08'] == 'E', 'QE_I08CAT'] = 5
    pfEnade.loc[pfEnade['QE_I08'] == 'F', 'QE_I08CAT'] = 6
    pfEnade.loc[pfEnade['QE_I08'] == 'G', 'QE_I08CAT'] = 7
    pfEnade['QE_I08CAT'] = pfEnade['QE_I08CAT'].astype(int)

    # pfEnade['QE_I23CAT'] = pfEnade['QE_I23'].cat.codes 
    # Quantas horas por semana, aproximadamente, você dedicou aos estudos, excetuando as horas de aula?	
    pfEnade['QE_I23CAT'] = 0
    pfEnade.loc[pfEnade['QE_I23'] == 'A', 'QE_I23CAT'] = 1
    pfEnade.loc[pfEnade['QE_I23'] == 'B', 'QE_I23CAT'] = 1
    #pfEnade.loc[pfEnade['QE_I23'] == 'C', 'QE_I23CAT'] = 3
    #pfEnade.loc[pfEnade['QE_I23'] == 'D', 'QE_I23CAT'] = 4
    #pfEnade.loc[pfEnade['QE_I23'] == 'E', 'QE_I23CAT'] = 5
    #pfEnade['QE_I23CAT'] = pfEnade['QE_I23CAT'].astype(int)

    # BOM ALUNO
    pfEnade['BomAluno'] = 0
    pfEnade.loc[pfEnade['NT_GER'] > 50, 'BomAluno'] = 1
    pfEnade['BomAluno'] = pfEnade['BomAluno'].astype(int)

    # BAIXA RENDA
    pfEnade['BaixaRenda'] = 0
    pfEnade.loc[pfEnade['QE_I08'] == 'A', 'BaixaRenda'] = 1
    pfEnade.loc[pfEnade['QE_I08'] == 'B', 'BaixaRenda'] = 1
    pfEnade.loc[pfEnade['QE_I08'] == 'C', 'BaixaRenda'] = 0
    pfEnade.loc[pfEnade['QE_I08'] == 'D', 'BaixaRenda'] = 0
    pfEnade.loc[pfEnade['QE_I08'] == 'E', 'BaixaRenda'] = 0
    pfEnade.loc[pfEnade['QE_I08'] == 'F', 'BaixaRenda'] = 0
    pfEnade.loc[pfEnade['QE_I08'] == 'G', 'BaixaRenda'] = 0
    pfEnade['BaixaRenda'] = pfEnade['BaixaRenda'].astype(int)
    

    # Sexo
    pfEnade['Sexo'] = pfEnade['TP_SEXO'].cat.codes  


    # Mora com Família
    pfEnade['Familia'] = pfEnade['QE_I07'].cat.codes  # Quantas pessoas da sua família moram com você?
    
    pfEnade['Solo'] = 0
    pfEnade.loc[pfEnade['QE_I07'] == 'A', 'Solo'] = 1
    pfEnade.loc[pfEnade['QE_I07'] == 'B', 'Solo'] = 1
    pfEnade.loc[pfEnade['QE_I07'] == 'C', 'Solo'] = 1
    pfEnade.loc[pfEnade['QE_I07'] == 'D', 'Solo'] = 0
    pfEnade.loc[pfEnade['QE_I07'] == 'E', 'Solo'] = 0
    pfEnade.loc[pfEnade['QE_I07'] == 'F', 'Solo'] = 0
    pfEnade.loc[pfEnade['QE_I07'] == 'G', 'Solo'] = 0
    pfEnade['Solo'] = pfEnade['Solo'].astype(int)
    
    # Recém Formado
    pfEnade['RecemFormado'] = 0
    pfEnade.loc[pfEnade['Tempo'] == 1, 'RecemFormado'] = 1
    pfEnade['RecemFormado'] = pfEnade['RecemFormado'].astype(int)

    #Novinho
    pfEnade['Jovem'] = 0
    pfEnade.loc[pfEnade['NU_IDADE'] <= 24, 'Jovem'] = 1
    pfEnade['Jovem'] = pfEnade['Jovem'].astype(int)

    # Sustentno
    pfEnade['Sustento'] = 0
    pfEnade.loc[pfEnade['QE_I09'] == 'A', 'Sustento'] = 1
    pfEnade.loc[pfEnade['QE_I09'] == 'B', 'Sustento'] = 1
    pfEnade.loc[pfEnade['QE_I09'] == 'C', 'Sustento'] = 0
    pfEnade.loc[pfEnade['QE_I09'] == 'D', 'Sustento'] = 0
    pfEnade.loc[pfEnade['QE_I09'] == 'E', 'Sustento'] = 0
    pfEnade.loc[pfEnade['QE_I09'] == 'F', 'Sustento'] = 0
    pfEnade.loc[pfEnade['QE_I09'] == 'G', 'Sustento'] = 0
    pfEnade['Sustento'] = pfEnade['Sustento'].astype(int)

    #IDdaes # 
    pfEnade['intervalos_idades'] = pd.cut(pfEnade['NU_IDADE'], 
        bins=[0, 17, 19, 21, 25, 30, 35],  
        labels=['Ate 17','Entre 17 e 19','Entre 19 e 21','Entre 21 e 25','Entre 30 e 35' ,'Acima de 35'])
    pfEnade['Age'] = pfEnade['intervalos_idades'].cat.codes 
    


    # dataset['intervalos_idades'] = dataset.cut(dataset['Nu_idade'], bins=[0, 17, 19, 21, 25, 30, 35], labels=['Ate 17','Entre 17 e 19','Entre 19 e 21','Entre 21 e 25','Entre 25 e 30','Entre 30 e 35' ,'Acima de 35'])


    return pfEnade
    

def doRaiz(pfEnade):
    pfEnade['BomAlunoRAIZ'] = pfEnade['NT_GER'].astype(int) # .cat.codes 
    pfEnade['CO_REGIAO_CURSORAIZ'] = pfEnade['CO_REGIAO_CURSO'].astype(int) # .cat.codes 
    pfEnade['JovemRAIZ'] = pfEnade['NU_IDADE'].astype(int) # .cat.codes 
    pfEnade['MigradoRAIZ'] = pfEnade['Migrado'].astype(int) # .cat.codes 
    pfEnade['SoloRAIZ'] = pfEnade['QE_I07'].cat.codes 
    pfEnade['ExatasRAIZ'] = pfEnade['Exatas'].astype(int) # .cat.codes 
    pfEnade['QE_I23CATRAIZ'] = pfEnade['QE_I23'].cat.codes 
    pfEnade['BaixaRendaRAIZ'] = pfEnade['QE_I08'].cat.codes 
    pfEnade['SustentoRAIZ'] = pfEnade['QE_I09'].cat.codes 
    pfEnade['SexoRAIZ'] = pfEnade['TP_SEXO'].cat.codes 
    return pfEnade
def doDESCategoriza(pfEnade):

    return pfEnade

