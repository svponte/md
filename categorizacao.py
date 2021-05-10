def doRenda(pfEnade):
    # TRATAR - RENDA - Categóricos
    pfEnade['Renda'] = pfEnade['QE_I08'].cat.codes  # Cria um grupo numérico a partir do categórica
    # del pfEnade['QE_I08']

    # DICIONÁRIO - Renda
    dicRenda = {'A' : 'Até 1,5 salário mínimo (até R$ 1.431,00)',
    'B' : 'De 1,5 a 3 salários mínimos (R$ 1.431,01 a R$ 2.862,00)',
    'C' : 'De 3 a 4,5 salários mínimos (R$ 2.862,01 a R$ 4.293,00)',
    'D' : 'De 4,5 a 6 salários mínimos (R$ 4.293,01 a R$ 5.724,00)',
    'E' : 'De 6 a 10 salários mínimos (R$ 5.724,01 a R$ 9.540,00)',
    'F' : 'De 10 a 30 salários mínimos (R$ 9.540,01 a R$ 28.620,00)',
    'G' : 'Acima de 30 salários mínimos (mais de R$ 28.620,00)',
    ' ' : '?'} 
    pfEnade['RendaDesc'] = [dicRenda[x] for x in pfEnade.QE_I08]
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
    ' ' : '?'}

    pfEnade['EscolaridadeDesc'] = [dicEscolaridade[x] for x in pfEnade.QE_I04]
    return pfEnade