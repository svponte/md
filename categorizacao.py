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
    pfEnade['QE_I23CAT'] = 0
    pfEnade.loc[pfEnade['QE_I23'] == 'A', 'QE_I23CAT'] = 1
    pfEnade.loc[pfEnade['QE_I23'] == 'B', 'QE_I23CAT'] = 2
    pfEnade.loc[pfEnade['QE_I23'] == 'C', 'QE_I08CAT'] = 3
    pfEnade.loc[pfEnade['QE_I23'] == 'D', 'QE_I08CAT'] = 4
    pfEnade.loc[pfEnade['QE_I23'] == 'E', 'QE_I08CAT'] = 5
    pfEnade['QE_I08CAT'] = pfEnade['QE_I08CAT'].astype(int)

    return pfEnade

