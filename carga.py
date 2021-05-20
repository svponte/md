import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


def doCarga(arquivo):
    # Carrega dataframe
    cols = ['CO_CATEGAD', 'CO_GRUPO', 'TP_SEXO', 'ANO_FIM_EM', 'ANO_IN_GRAD', 
        'QE_I08', 'QE_I16', 'QE_I17', 'QE_I04', 'QE_I05', 'CO_UF_CURSO', 
        'NT_GER', 'QE_I23', 'QE_I07', 'CO_REGIAO_CURSO', 'NU_IDADE', 'QE_I09']
    pfEnade = pd.read_csv(arquivo, usecols=cols, sep = ';', decimal=",", low_memory=False, \
        dtype={'CO_GRUPO':'category', 'TP_SEXO':'category', 'QE_I08':'category', \
            'QE_I16':'category','QE_I17':'category','QE_I04':'category', \
            'QE_I05':'category','CO_UF_CURSO':'category', 
            'NT_GER':'float', 'QE_I23':'category', 'QE_I07':'category', 'QE_I09':'category'})
    #pfEnade["Indice"] = pfEnade.index + 1
    
    # ## NORMALIZAÇÔES
    pfEnade.dropna(inplace=True)
    pfEnade = pfEnade.query('ANO_FIM_EM > 2004')
    pfEnade = pfEnade.query('ANO_FIM_EM < 2020')
    pfEnade = pfEnade.query('ANO_IN_GRAD > 2010')
    pfEnade = pfEnade.query('ANO_IN_GRAD < 2020')
    pfEnade = pfEnade.query('ANO_IN_GRAD > ANO_FIM_EM')
    
    dfRemove = pfEnade.loc[(pfEnade['QE_I08'] == ' ')]
    pfEnade = pfEnade.drop(dfRemove.index)
    pfEnade['QE_I08'] = pfEnade['QE_I08'].str.strip().astype('category')

    pfEnade = pfEnade.query('NT_GER > 1')
    pfEnade = pfEnade.query('NT_GER < 87')
    
    pfEnade['QE_I23'] = pfEnade['QE_I23'].str.strip().astype('category')  
    pfEnade = pfEnade.query('QE_I23 != ""')
    pfEnade['QE_I23'] = pfEnade['QE_I23'].str.strip().astype('category')

    return pfEnade

def doCargaFull(arquivo):
    # Carrega dataframe
    cols = ['CO_CATEGAD', 'CO_GRUPO', 'TP_SEXO', 'ANO_FIM_EM', 'ANO_IN_GRAD', 
        'QE_I08', 'QE_I16', 'QE_I17', 'QE_I04', 'QE_I05', 'CO_UF_CURSO', 
        'NT_GER', 'QE_I23', 'QE_I07', 'NU_IDADE']
    pfEnade = pd.read_csv(arquivo, usecols=cols, sep = ';', decimal=",", low_memory=False, \
        dtype={'CO_GRUPO':'category', 'TP_SEXO':'category', 'QE_I08':'category', \
            'QE_I16':'category','QE_I17':'category','QE_I04':'category', \
            'QE_I05':'category','CO_UF_CURSO':'category', 
            'NT_GER':'float', 'QE_I23':'category', 'QE_I07':'category', 'NU_IDADE':'int'})
    pfEnade["Indice"] = pfEnade.index + 1
    return pfEnade
    

def doCargaTodos(arquivo):
    # Carrega dataframe

    pfEnade = pd.read_csv(arquivo, sep = ';', decimal=",", low_memory=False, \
        dtype={'CO_GRUPO':'category', 'TP_SEXO':'category', 'QE_I08':'category', \
            'QE_I16':'category','QE_I17':'category','QE_I04':'category', \
            'QE_I05':'category','CO_UF_CURSO':'category', 
            'NT_GER':'float', 'QE_I23':'category', 'QE_I07':'category'})
    pfEnade["Indice"] = pfEnade.index + 1

    # ## NORMALIZAÇÔES
    pfEnade.dropna(inplace=True)
    pfEnade = pfEnade.query('ANO_FIM_EM > 2004')
    pfEnade = pfEnade.query('ANO_FIM_EM < 2020')
    pfEnade = pfEnade.query('ANO_IN_GRAD > 2010')
    pfEnade = pfEnade.query('ANO_IN_GRAD < 2020')
    pfEnade = pfEnade.query('ANO_IN_GRAD >= ANO_FIM_EM')
    
    dfRemove = pfEnade.loc[(pfEnade['QE_I08'] == ' ')]
    pfEnade = pfEnade.drop(dfRemove.index)
    pfEnade['QE_I08'] = pfEnade['QE_I08'].str.strip().astype('category')

    pfEnade = pfEnade.query('NT_GER > 1')
    pfEnade = pfEnade.query('NT_GER < 87')
    
    pfEnade['QE_I23'] = pfEnade['QE_I23'].str.strip().astype('category')  
    pfEnade = pfEnade.query('QE_I23 != ""')
    pfEnade['QE_I23'] = pfEnade['QE_I23'].str.strip().astype('category')
    return pfEnade







    # Carrega TUDO
    #pfEnade = pd.read_csv(arquivo, sep = ';', low_memory=False)
    
    
    # Método de seleção auternativo
    #cols = ['CO_CATEGAD', 'CO_GRUPO', 'TP_SEXO', 'ANO_FIM_EM', 'ANO_IN_GRAD', 'QE_I08', 'QE_I16', 'QE_I17', 'QE_I04', 'QE_I05', 'CO_UF_CURSO']
    #pfSelecionados = pfEnade.filter(items=cols)
    
    # 12 = MEDICINA / # 5710 = ENGENHARIA CIVIL
    # pfEnade = pfEnade.query('CO_GRUPO == 12 or CO_GRUPO == 5710')
    # pfEnade = pfEnade[pfEnade['CO_CATEGAD'].isin([12, 5710])] 

    # # NOME	Nº	TIPO	TAMANHO	DESCRIÇÃO	
    # del pfEnade['NU_ANO'] #	1 - N - 4 - Ano de realização do exame	
    # del pfEnade['CO_IES'] #	2 - N - 5 - Código da IES (e-MEC)	
    # # del pfEnade['CO_CATEGAD'] #	3 - N - 5 - Código da categoria administrativa da IES	
    # del pfEnade['CO_ORGACAD'] #	4 - N - 5 - Código da organização acadêmica da IES	
    # # del pfEnade['CO_GRUPO'] #	5 - N - 4 - Código da Área de enquadramento do curso no Enade	
    # # del pfEnade['CO_CURSO'] #	6 - N - 7 - Código do curso no Enade	
    # del pfEnade['CO_MODALIDADE'] #	7 - N - 1 - Código da Modalidade de Ensino	
    # del pfEnade['CO_MUNIC_CURSO'] #	8 - N - 7 - Código do município de funcionamento do curso	
    # # del pfEnade['CO_UF_CURSO'] #	9 - N - 2 - Código da UF de funcionamento do curso	
    # del pfEnade['CO_REGIAO_CURSO'] #	10 - N - 1 - Código da região de funcionamento do curso	
    # del pfEnade['NU_IDADE'] #	11 - N - 2 - Idade do inscrito em 24/11/2019	
    # # del pfEnade['TP_SEXO'] #	12 - C - 1 - Sexo	
    # # del pfEnade['ANO_FIM_EM'] #	13 - N - 4 - Ano de conclusão do Ensino Médio	
    # # del pfEnade['ANO_IN_GRAD'] #	14 - N - 4 - Ano de início da graduação	
    # del pfEnade['CO_TURNO_GRADUACAO'] #	15 - N - 1 - Código do turno de graduação	
    # del pfEnade['TP_INSCRICAO_ADM'] #	16 - N - 1 - Forma pela qual foi realizada a inscrição	
    # del pfEnade['TP_INSCRICAO'] #	17 - N - 1 - Tipo de inscrição	
    # del pfEnade['NU_ITEM_OFG'] #	18 - N - 1 - Número de itens da parte objetiva da Formação Geral	
    # del pfEnade['NU_ITEM_OFG_Z'] #	19 - N - 1 - Número de itens da parte objetiva da Formação Geral que foram excluídos devido a anulação	
    # del pfEnade['NU_ITEM_OFG_X'] #	20 - N - 1 - Número de itens da parte objetiva da Formação Geral que foram excluídos devido ao coeficiente ponto-bisserial menor que 0,20	
    # del pfEnade['NU_ITEM_OFG_N'] #	21 - N - 1 - Número de itens da parte objetiva da Formação Geral que não se aplicam ao grupo de curso	
    # del pfEnade['NU_ITEM_OCE'] #	22 - N - 2 - Número de itens da parte objetiva de Componente Específico	
    # del pfEnade['NU_ITEM_OCE_Z'] #	23 - N - 2 - Número de itens da parte objetiva de Componente Específico que foram excluídos devido a anulação	
    # del pfEnade['NU_ITEM_OCE_X'] #	24 - N - 1 - Número de itens da parte objetiva de Componente Específico que foram excluídos devido ao coeficiente ponto-bisserial menor que 0,20	
    # del pfEnade['NU_ITEM_OCE_N'] #	25 - N - 1 - Número de itens da parte objetiva de Componente Específico que não se aplicam ao grupo de curso	
    # del pfEnade['DS_VT_GAB_OFG_ORIG'] #	26 - C - 8 - Vetor que representa o gabarito original de Formação Geral	
    # del pfEnade['DS_VT_GAB_OFG_FIN'] #	27 - C - 8 - Vetor que representa o gabarito final de Formação Geral	
    # del pfEnade['DS_VT_GAB_OCE_ORIG'] #	28 - C - 27 - Vetor que representa o gabarito original de Componente Específico	
    # del pfEnade['DS_VT_GAB_OCE_FIN'] #	29 - C - 27 - Vetor que representa o gabarito final de Componente Específico	
    # del pfEnade['DS_VT_ESC_OFG'] #	30 - C - 8 - Vetor que representa a escolha de resposta da parte objetiva da Formação Geral	
    # del pfEnade['DS_VT_ACE_OFG'] #	31 - C - 8 - Vetor que representa os acertos da parte objetiva na Formação Geral	
    # del pfEnade['DS_VT_ESC_OCE'] #	32 - C - 27 - Vetor que representa a escolha de resposta da parte objetiva do Componente Específico	
    # del pfEnade['DS_VT_ACE_OCE'] #	33 - C - 27 - Vetor que representa os acertos da parte objetiva do Componente Específico	
    # del pfEnade['TP_PRES'] #	34 - N - 3 - Tipo de presença no Enade	
    # del pfEnade['TP_PR_GER'] #	35 - N - 3 - Tipo de presença na prova	
    # del pfEnade['TP_PR_OB_FG'] #	36 - N - 3 - Tipo de presença na parte objetiva na formação geral	
    # del pfEnade['TP_PR_DI_FG'] #	37 - N - 3 - Tipo de presença na parte discursiva na formação geral	
    # del pfEnade['TP_PR_OB_CE'] #	38 - N - 3 - Tipo de presença na parte objetiva no componente específico	
    # del pfEnade['TP_PR_DI_CE'] #	39 - N - 3 - Tipo de presença na parte discursiva no componente específico	
    # del pfEnade['TP_SFG_D1'] #	40 - N - 3 - Tipo de situação da questão 1 da parte discursiva da formação geral	
    # del pfEnade['TP_SFG_D2'] #	41 - N - 3 - Tipo de situação da questão 2 da parte discursiva da formação geral	
    # del pfEnade['TP_SCE_D1'] #	42 - N - 3 - Tipo de situação da questão 1 da parte discursiva do componente específico	
    # del pfEnade['TP_SCE_D2'] #	43 - N - 3 - Tipo de situação da questão 2 da parte discursiva do componente específico	
    # del pfEnade['TP_SCE_D3'] #	44 - N - 3 - Tipo de situação da questão 3 da parte discursiva do componente específico	
    # del pfEnade['NT_GER'] #	45 - N - 4 - Nota bruta da prova - Média ponderada da formação geral (25%) e componente específico (75%). (valor de 0 a 100)	
    # del pfEnade['NT_FG'] #	46 - N - 4 - Nota bruta na formação geral - Média ponderada da parte objetiva (60%) e discursiva (40%) na formação geral. (valor de 0 a 100)	
    # del pfEnade['NT_OBJ_FG'] #	47 - N - 4 - Nota bruta na parte objetiva da formação geral. (valor de 0 a 100)	
    # del pfEnade['NT_DIS_FG'] #	48 - N - 4 - Nota bruta na parte discursiva da formação geral. (valor de 0 a 100)	
    # del pfEnade['NT_FG_D1'] #	49 - N - 3 - Nota da questão 1 da parte discursiva da formação geral - Média ponderada da parte de Língua Portuguesa (20%) e Conteúdo (80%) da Questão 1 da parte discursiva (valor de 0 a 100)	
    # del pfEnade['NT_FG_D1_PT'] #	50 - N - 3 - Nota de Língua Portuguesa da questão 1 da parte discursiva da formação geral. (valor de 0 a 100)	
    # del pfEnade['NT_FG_D1_CT'] #	51 - N - 3 - Nota de Conteúdo da questão 1 da parte discursiva da formação geral. (valor de 0 a 100)	
    # del pfEnade['NT_FG_D2'] #	52 - N - 3 - Nota da questão 2 da parte discursiva na formação geral - Média ponderada da parte de Língua Portuguesa (20%) e Conteúdo (80%) da Questão 2 da parte discursiva. (valor de 0 a 100)	
    # del pfEnade['NT_FG_D2_PT'] #	53 - N - 3 - Nota de Língua Portuguesa da questão 2 da parte discursiva da formação geral. (valor de 0 a 100)	
    # del pfEnade['NT_FG_D2_CT'] #	54 - N - 3 - Nota de Conteúdo da questão 2 da parte discursiva da formação geral. (valor de 0 a 100)	
    # del pfEnade['NT_CE'] #	55 - N - 4 - Nota bruta no componente específico - Média ponderada da parte objetiva (85%) e discursiva (15%) no componente específico. (valor de 0 a 100)	
    # del pfEnade['NT_OBJ_CE'] #	56 - N - 4 - Nota bruta na parte objetiva do componente específico. (valor de 0 a 100)	
    # del pfEnade['NT_DIS_CE'] #	57 - N - 4 - Nota bruta na parte discursiva do componente específico. (valor de 0 a 100)	
    # del pfEnade['NT_CE_D1'] #	58 - N - 3 - Nota da questão 1 da parte discursiva do componente específico. (valor de 0 a 100)	
    # del pfEnade['NT_CE_D2'] #	59 - N - 3 - Nota da questão 2 da parte discursiva do componente específico. (valor de 0 a 100)	
    # del pfEnade['NT_CE_D3'] #	60 - N - 3 - Nota da questão 3 da parte discursiva do componente específico. (valor de 0 a 100)	
    # del pfEnade['CO_RS_I1'] #	61 - C - 1 - 1 - Qual o grau de dificuldade desta prova na parte de Formação Geral?	
    # del pfEnade['CO_RS_I2'] #	62 - C - 1 - 2 - Qual o grau de dificuldade desta prova na parte do Componente Específico?	
    # del pfEnade['CO_RS_I3'] #	63 - C - 1 - 3 - Considerando a extensão da prova, em relação ao tempo total, você considera que a prova foi:	
    # del pfEnade['CO_RS_I4'] #	64 - C - 1 - 4 - Os enunciados das questões da prova na parte de Formação Geral estavam claros e objetivos?	
    # del pfEnade['CO_RS_I5'] #	65 - C - 1 - 5 - Os enunciados das questões na parte do Componente Específico estavam claros e objetivos?	
    # del pfEnade['CO_RS_I6'] #	66 - C - 1 - 6 - As informações/instruções fornecidas para a resolução das questões foram suficientes para resolvê-las?	
    # del pfEnade['CO_RS_I7'] #	67 - C - 1 - 7 - Você se deparou com alguma dificuldade ao responder à prova. Qual?	
    # del pfEnade['CO_RS_I8'] #	68 - C - 1 - 8 - Considerando apenas as questões objetivas da prova, você percebeu que:	
    # del pfEnade['CO_RS_I9'] #	69 - C - 1 - 9 - Qual foi o tempo gasto por você para concluir a prova?	
    # del pfEnade['QE_I01'] #	70 - C - 1 - Qual o seu estado civil?	
    # del pfEnade['QE_I02'] #	71 - C - 1 - Qual é a sua cor ou raça?	
    # del pfEnade['QE_I03'] #	72 - C - 1 - Qual a sua nacionalidade?	
    # # del pfEnade['QE_I04'] #	73 - C - 1 - Até que etapa de escolarização seu pai concluiu?	
    # # del pfEnade['QE_I05'] #	74 - C - 1 - Até que etapa de escolarização sua mãe concluiu?	
    # del pfEnade['QE_I06'] #	75 - C - 1 - Onde e com quem você mora atualmente?	
    # del pfEnade['QE_I07'] #	76 - C - 1 - Quantas pessoas da sua família moram com você? Considere seus pais, irmãos, cônjuge, filhos e outros parentes que moram na mesma casa com você.	
    # # del pfEnade['QE_I08'] #	77 - C - 1 - Qual a renda total de sua família, incluindo seus rendimentos?	
    # del pfEnade['QE_I09'] #	78 - C - 1 - Qual alternativa a seguir melhor descreve sua situação financeira (incluindo bolsas)?	
    # del pfEnade['QE_I10'] #	79 - C - 1 - Qual alternativa a seguir melhor descreve sua situação de trabalho (exceto estágio ou bolsas)?	
    # del pfEnade['QE_I11'] #	80 - C - 1 - Que tipo de bolsa de estudos ou financiamento do curso você recebeu para custear todas ou a maior parte das mensalidades? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração.	
    # del pfEnade['QE_I12'] #	81 - C - 1 - Ao longo da sua trajetória acadêmica, você recebeu algum tipo de bolsa de permanência? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração.	
    # del pfEnade['QE_I13'] #	82 - C - 1 - Ao longo da sua trajetória acadêmica, você recebeu algum tipo de bolsa acadêmica? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração.	
    # del pfEnade['QE_I14'] #	83 - C - 1 - Durante o curso de graduação, você participou de programas e ou atividades curriculares no exterior?	
    # del pfEnade['QE_I15'] #	84 - C - 1 - Seu ingresso no curso de graduação se deu por meio de políticas de ação afirmativa ou inclusão social?	
    # # del pfEnade['QE_I16'] #	85 - N - 2 - Em que unidade da Federação você concluiu o ensino médio?	
    # # del pfEnade['QE_I17'] #	86 - C - 1 - Em que tipo de escola você cursou o ensino médio?	
    # del pfEnade['QE_I18'] #	87 - C - 1 - Qual modalidade de ensino médio você concluiu?	
    # del pfEnade['QE_I19'] #	88 - C - 1 - Quem mais lhe incentivou a cursar a graduação?	
    # del pfEnade['QE_I20'] #	89 - C - 1 - Algum dos grupos abaixo foi determinante para você enfrentar dificuldades durante seu curso superior e conclui-lo?	
    # del pfEnade['QE_I21'] #	90 - C - 1 - Alguém em sua família concluiu um curso superior?	
    # del pfEnade['QE_I22'] #	91 - C - 1 - Excetuando-se os livros indicados na bibliografia do seu curso, quantos livros você leu neste ano?	
    # del pfEnade['QE_I23'] #	92 - C - 1 - Quantas horas por semana, aproximadamente, você dedicou aos estudos, excetuando as horas de aula?	
    # del pfEnade['QE_I24'] #	93 - C - 1 - Você teve oportunidade de aprendizado de idioma estrangeiro na Instituição?	
    # del pfEnade['QE_I25'] #	94 - C - 1 - Qual o principal motivo para você ter escolhido este curso?	
    # del pfEnade['QE_I26'] #	95 - C - 1 - Qual a principal razão para você ter escolhido a sua instituição de educação superior?	
    # del pfEnade['QE_I27'] #	96 - N - 1 - As disciplinas cursadas contribuíram para sua formação integral, como cidadão e profissional.	
    # del pfEnade['QE_I28'] #	97 - N - 1 - Os conteúdos abordados nas disciplinas do curso favoreceram sua atuação em estágios ou em atividades de iniciação profissional.	
    # del pfEnade['QE_I29'] #	98 - N - 1 - As metodologias de ensino utilizadas no curso desafiaram você a aprofundar conhecimentos e desenvolver competências reflexivas e críticas.	
    # del pfEnade['QE_I30'] #	99 - N - 1 - O curso propiciou experiências de aprendizagem inovadoras.	
    # del pfEnade['QE_I31'] #	100 - N - 1 - O curso contribuiu para o desenvolvimento da sua consciência ética para o exercício profissional.	
    # del pfEnade['QE_I32'] #	101 - N - 1 - No curso você teve oportunidade de aprender a trabalhar em equipe.	
    # del pfEnade['QE_I33'] #	102 - N - 1 - O curso possibilitou aumentar sua capacidade de reflexão e argumentação.	
    # del pfEnade['QE_I34'] #	103 - N - 1 - O curso promoveu o desenvolvimento da sua capacidade de pensar criticamente, analisar e refletir sobre soluções para problemas da sociedade.	
    # del pfEnade['QE_I35'] #	104 - N - 1 - O curso contribuiu para você ampliar sua capacidade de comunicação nas formas oral e escrita.	
    # del pfEnade['QE_I36'] #	105 - N - 1 - O curso contribuiu para o desenvolvimento da sua capacidade de aprender e atualizar-se permanentemente.	
    # del pfEnade['QE_I37'] #	106 - N - 1 - As relações professor-aluno ao longo do curso estimularam você a estudar e aprender.	
    # del pfEnade['QE_I38'] #	107 - N - 1 - Os planos de ensino apresentados pelos professores contribuíram para o desenvolvimento das atividades acadêmicas e para seus estudos.	
    # del pfEnade['QE_I39'] #	108 - N - 1 - As referências bibliográficas indicadas pelos professores nos planos de ensino contribuíram para seus estudos e aprendizagens.	
    # del pfEnade['QE_I40'] #	109 - N - 1 - Foram oferecidas oportunidades para os estudantes superarem problemas e dificuldades relacionados ao processo de formação.	
    # del pfEnade['QE_I41'] #	110 - N - 1 - A coordenação do curso esteve disponível para orientação acadêmica dos estudantes.	
    # del pfEnade['QE_I42'] #	111 - N - 1 - O curso exigiu de você organização e dedicação frequente aos estudos.	
    # del pfEnade['QE_I43'] #	112 - N - 1 - Foram oferecidas oportunidades para os estudantes participarem de programas, projetos ou atividades de extensão universitária.	
    # del pfEnade['QE_I44'] #	113 - N - 1 - Foram oferecidas oportunidades para os estudantes participarem de projetos de iniciação científica e de atividades que estimularam a investigação acadêmica.	
    # del pfEnade['QE_I45'] #	114 - N - 1 - O curso ofereceu condições para os estudantes participarem de eventos internos e/ou externos à instituição.	
    # del pfEnade['QE_I46'] #	115 - N - 1 - A instituição ofereceu oportunidades para os estudantes atuarem como representantes em órgãos colegiados.	
    # del pfEnade['QE_I47'] #	116 - N - 1 - O curso favoreceu a articulação do conhecimento teórico com atividades práticas.	
    # del pfEnade['QE_I48'] #	117 - N - 1 - As atividades práticas foram suficientes para relacionar os conteúdos do curso com a prática, contribuindo para sua formação profissional.	
    # del pfEnade['QE_I49'] #	118 - N - 1 - O curso propiciou acesso a conhecimentos atualizados e/ou contemporâneos em sua área de formação.	
    # del pfEnade['QE_I50'] #	119 - N - 1 - O estágio supervisionado proporcionou experiências diversificadas para a sua formação.	
    # del pfEnade['QE_I51'] #	120 - N - 1 - As atividades realizadas durante seu trabalho de conclusão de curso contribuíram para qualificar sua formação profissional.	
    # del pfEnade['QE_I52'] #	121 - N - 1 - Foram oferecidas oportunidades para os estudantes realizarem intercâmbios e/ou estágios no país. 	
    # del pfEnade['QE_I53'] #	122 - N - 1 - Foram oferecidas oportunidades para os estudantes realizarem intercâmbios e/ou estágios fora do país.	
    # del pfEnade['QE_I54'] #	123 - N - 1 - Os estudantes participaram de avaliações periódicas do curso (disciplinas, atuação dos professores, infraestrutura).	
    # del pfEnade['QE_I55'] #	124 - N - 1 - As avaliações de aprendizagem realizadas durante o curso foram compatíveis com os conteúdos ou temas trabalhados pelos professores.	
    # del pfEnade['QE_I56'] #	125 - N - 1 - Os professores apresentaram disponibilidade para atender os estudantes fora do horário das aulas.	
    # del pfEnade['QE_I57'] #	126 - N - 1 - Os professores demonstraram domínio dos conteúdos abordados nas disciplinas.	
    # del pfEnade['QE_I58'] #	127 - N - 1 - Os professores utilizaram tecnologias da informação e comunicação (TIC's) como estratégia de ensino (projetor, multimídia, laboratório de informática, ambiente virtual de aprendizagem).	
    # del pfEnade['QE_I59'] #	128 - N - 1 - A instituição dispôs de quantidade suficiente de funcionários para o apoio administrativo e acadêmico.	
    # del pfEnade['QE_I60'] #	129 - N - 1 - O curso disponibilizou monitores ou tutores para auxiliar os estudantes.	
    # del pfEnade['QE_I61'] #	130 - N - 1 - As condições de infraestrutura das salas de aula foram adequadas.	
    # del pfEnade['QE_I62'] #	131 - N - 1 - Os equipamentos e materiais disponíveis para as aulas práticas foram adequados para a quantidade de estudantes.	
    # del pfEnade['QE_I63'] #	132 - N - 1 - Os ambientes e equipamentos destinados às aulas práticas foram adequados ao curso.	
    # del pfEnade['QE_I64'] #	133 - N - 1 - A biblioteca dispôs das referências bibliográficas que os estudantes necessitaram.	
    # del pfEnade['QE_I65'] #	134 - N - 1 - A instituição contou com biblioteca virtual ou conferiu acesso a obras disponíveis em acervos virtuais.	
    # del pfEnade['QE_I66'] #	135 - N - 1 - As atividades acadêmicas desenvolvidas dentro e fora da sala de aula possibilitaram reflexão, convivência e respeito à diversidade.	
    # del pfEnade['QE_I67'] #	136 - N - 1 - A instituição promoveu atividades de cultura, de lazer e interação social.	
    # del pfEnade['QE_I68'] #	137 - N - 1 - A instituição dispôs de refeitório, cantina e banheiros em condições adequadas que atenderam as necessidades dos seus usuários.	
    
    #return pfEnade
