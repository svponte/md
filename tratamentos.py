import pandas as pd
def doIdade (pfEnade):
    # Calculando a idade
    # antes deste trecho
    # 130.127 registros
    # mínimo ano_fim_em 1111
    # máximo ano_in_grad 14

    pfEnade = pfEnade.query('ANO_FIM_EM > 1990')
    pfEnade = pfEnade.query('ANO_FIM_EM < 2020')
    pfEnade = pfEnade.query('ANO_IN_GRAD > 2010')
    pfEnade = pfEnade.query('ANO_IN_GRAD < 2020')
    pfEnade = pfEnade.query('ANO_IN_GRAD > ANO_FIM_EM')
    pfEnade["Tempo"] = pfEnade["ANO_IN_GRAD"] - pfEnade["ANO_FIM_EM"]
    del pfEnade['ANO_FIM_EM']
    del pfEnade['ANO_IN_GRAD']
    return pfEnade

def doRenda(pfEnade):
    # Há 6 registros na base que, cujas rendas não estão apresentadas
    pfEnade = pfEnade.query('QE_I08 != " "')
    return pfEnade

def doVazios(pfEnade):
    # TRATAR - Valores ausentes
    pfEnade.dropna(inplace=True)

    for col in ['CO_UF_CURSO', 'QE_I16']:
        pfEnade[col] = pd.to_numeric(pfEnade[col], errors='coerce')

    return pfEnade

def doPublicoPrivada(pfEnade):
    # TRATAR - Publico Privada
    # 0 = Pública
    # 1 = Privada
    pfEnade["Publica"] = pfEnade["CO_CATEGAD"]
    pfEnade.loc[pfEnade['Publica'] == 118, 'Publica'] = 1     # 118 = Pessoa Jurídica de Direito Privado - Com fins lucrativos - Sociedade Civil
    pfEnade.loc[pfEnade['Publica'] == 120, 'Publica'] = 1     # 120 = Pessoa Jurídica de Direito Privado - Sem fins lucrativos - Associação de Utilidade Pública
    pfEnade.loc[pfEnade['Publica'] == 121, 'Publica'] = 1     # 121 = Pessoa Jurídica de Direito Privado - Sem fins lucrativos - Fundação
    pfEnade.loc[pfEnade['Publica'] == 10005, 'Publica'] = 1   # 10005 = Privada com fins lucrativos
    pfEnade.loc[pfEnade['Publica'] == 10006, 'Publica'] = 1   # 10006 = Pessoa Jurídica de Direito Privado - Com fins lucrativos - Sociedade Mercantil ou Comercial
    pfEnade.loc[pfEnade['Publica'] == 10007, 'Publica'] = 1   # 10007 = Pessoa Jurídica de Direito Privado - Sem fins lucrativos - Associação de Utilidade Pública
    pfEnade.loc[pfEnade['Publica'] == 10008, 'Publica'] = 1   # 10008 = Privada sem fins lucrativos
    pfEnade.loc[pfEnade['Publica'] == 10009, 'Publica'] = 1   # 10009 = Pessoa Jurídica de Direito Privado - Sem fins lucrativos - Sociedade
    pfEnade.loc[pfEnade['Publica'] == 17634, 'Publica'] = 0   # 17634 = Fundação Pública de Direito Privado Municipal
    pfEnade.loc[pfEnade['Publica'] == 93, 'Publica'] = 0      # 93 = Pessoa Jurídica de Direito Público - Federal
    pfEnade.loc[pfEnade['Publica'] == 115, 'Publica'] = 0     # 115 = Pessoa Jurídica de Direito Público - Estadual
    pfEnade.loc[pfEnade['Publica'] == 116, 'Publica'] = 0     # 116 = Pessoa Jurídica de Direito Público - Municipal
    pfEnade.loc[pfEnade['Publica'] == 10001, 'Publica'] = 0   # 10001 = Pessoa Jurídica de Direito Público - Estadual
    pfEnade.loc[pfEnade['Publica'] == 10002, 'Publica'] = 0   # 10002 = Pessoa Jurídica de Direito Público - Federal
    pfEnade.loc[pfEnade['Publica'] == 10003, 'Publica'] = 0   # 10003 = Pessoa Jurídica de Direito Público - Municipal
    #pfEnade.groupby("Publica").count()
    del pfEnade['CO_CATEGAD']
    return pfEnade

def doHumanasExatas(pfEnade):
    # TRATAR - Humanas X Exatas 
    # 0 = Humanas
    # 1 = Exatas
    pfEnade.loc[pfEnade['CO_GRUPO'] == '5', 'Exatas'] = 1        # 5 = MEDICINA VETERINÁRIA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '6', 'Exatas'] = 1        # 6 = ODONTOLOGIA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '12', 'Exatas'] = 1      # 12 = MEDICINA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '17', 'Exatas'] = 0      # 17 = AGRONOMIA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '19', 'Exatas'] = 1      # 19 = FARMÁCIA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '21', 'Exatas'] = 0      # 21 = ARQUITETURA E URBANISMO
    pfEnade.loc[pfEnade['CO_GRUPO'] == '23', 'Exatas'] = 1      # 23 = ENFERMAGEM
    pfEnade.loc[pfEnade['CO_GRUPO'] == '27', 'Exatas'] = 1      # 27 = FONOAUDIOLOGIA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '28', 'Exatas'] = 1      # 28 = NUTRIÇÃO
    pfEnade.loc[pfEnade['CO_GRUPO'] == '36', 'Exatas'] = 1      # 36 = FISIOTERAPIA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '51', 'Exatas'] = 1      # 51 = ZOOTECNIA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '55', 'Exatas'] = 1      # 55 = BIOMEDICINA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '69', 'Exatas'] = 0      # 69 = TECNOLOGIA EM RADIOLOGIA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '90', 'Exatas'] = 0      # 90 = TECNOLOGIA EM AGRONEGÓCIOS
    pfEnade.loc[pfEnade['CO_GRUPO'] == '91', 'Exatas'] = 1      # 91 = TECNOLOGIA EM GESTÃO HOSPITALAR
    pfEnade.loc[pfEnade['CO_GRUPO'] == '92', 'Exatas'] = 1      # 92 = TECNOLOGIA EM GESTÃO AMBIENTAL
    pfEnade.loc[pfEnade['CO_GRUPO'] == '95', 'Exatas'] = 1      # 95 = TECNOLOGIA EM ESTÉTICA E COSMÉTICA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '3501', 'Exatas'] = 1    # 3501 = EDUCAÇÃO FÍSICA (BACHARELADO)
    pfEnade.loc[pfEnade['CO_GRUPO'] == '4003', 'Exatas'] = 0    # 4003 = ENGENHARIA DA COMPUTAÇÃO
    pfEnade.loc[pfEnade['CO_GRUPO'] == '5710', 'Exatas'] = 0    # 5710 = ENGENHARIA CIVIL
    pfEnade.loc[pfEnade['CO_GRUPO'] == '5806', 'Exatas'] = 0    # 5806 = ENGENHARIA ELÉTRICA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '5814', 'Exatas'] = 0    # 5814 = ENGENHARIA DE CONTROLE E AUTOMAÇÃO
    pfEnade.loc[pfEnade['CO_GRUPO'] == '5902', 'Exatas'] = 0    # 5902 = ENGENHARIA MECÂNICA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '6002', 'Exatas'] = 0    # 6002 = ENGENHARIA DE ALIMENTOS
    pfEnade.loc[pfEnade['CO_GRUPO'] == '6008', 'Exatas'] = 0    # 6008 = ENGENHARIA QUÍMICA
    pfEnade.loc[pfEnade['CO_GRUPO'] == '6208', 'Exatas'] = 0    # 6208 = ENGENHARIA DE PRODUÇÃO
    pfEnade.loc[pfEnade['CO_GRUPO'] == '6307', 'Exatas'] = 0    # 6307 = ENGENHARIA AMBIENTAL
    pfEnade.loc[pfEnade['CO_GRUPO'] == '6405', 'Exatas'] = 0    # 6405 = ENGENHARIA FLORESTAL
    pfEnade.loc[pfEnade['CO_GRUPO'] == '6410', 'Exatas'] = 0    # 6410 = TECNOLOGIA EM SEGURANÇA NO TRABALHO
    # del pfEnade['CO_GRUPO']
    #pfEnade['Exatas'].value_counts()
    pfEnade['Exatas'] = pfEnade['Exatas'].astype(int)
    #pfEnade['CO_GRUPO'].value_counts()
    return pfEnade

def doNota(pfEnade):
    # Mostra percetual de notas vazias
    pfEnade['NT_GER'].isnull().mean()
    # 10% das notas estão com valor vazio
    # Assumimos que, quem não tem nota, então a nota é zero
    pfEnade['NT_GER'].fillna(0, inplace=True)
    pfEnade['NT_GER'].isnull().mean()
    return pfEnade

def doMigracao(pfEnade):
    #TRATAR - Se foi migrado ou não
    pfEnade['Migrado'] = 0
    # CO_UF_CURSO - UF do Curso
    # QE_I16 - UF do Ensino Médio
    pfEnade.loc[pfEnade['CO_UF_CURSO'] != pfEnade['QE_I16'], 'Migrado'] = 1  
    return pfEnade



