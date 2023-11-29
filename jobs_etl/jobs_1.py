import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

num_rows = 1000

data = {
    'Operadora': np.random.choice(['Operadora1', 'Operadora2', 'Operadora3', 'Operadora4', 'Operadora5'], num_rows),
    'Código do Cliente': np.random.randint(1000, 9999, num_rows),
    'Razão Social do Cliente': [fake.company() for _ in range(num_rows)],
    'Código do Associado': np.random.randint(100, 999, num_rows),
    'Nome do Associado': [fake.name() for _ in range(num_rows)],
    'Tipo de Associado': np.random.choice(['Titular', 'Dependente'], num_rows),
    'Sexo': np.random.choice(['M', 'F'], num_rows),
    'Data de Nascimento': [fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d') for _ in range(num_rows)],
    'Grupo Tipo de Atendimento': np.random.choice(['Ambulatorial', 'Internação', 'Consulta', 'Exame'], num_rows),
    'Valor': np.random.randint(50, 500, num_rows),
    'Data do Atendimento': [fake.date_this_decade().strftime('%Y-%m-%d') for _ in range(num_rows)],
    'Competência': [fake.job() for _ in range(num_rows)],
    'CGC do Prestador Local': [fake.random_number(digits=14) for _ in range(num_rows)],
    'Nome do Prestador Local': [fake.company() for _ in range(num_rows)],
    'Especialidade - Descrição': np.random.choice(['Clínico Geral', 'Ortopedia', 'Dermatologia', 'Cardiologia', 'Oftalmologia'], num_rows),
    'Prestador Local Próprio': np.random.choice([1, 0], num_rows),
    'Cidade do Prestador Local': [fake.city() for _ in range(num_rows)],
    'Estado do Prestador Local': [fake.state_abbr() for _ in range(num_rows)],
    'Código do Procedimento': np.random.randint(1, 100, num_rows),
    'Nome do Procedimento': [fake.word() for _ in range(num_rows)],
    'Código do CID': [fake.random_number(digits=5) for _ in range(num_rows)],
    'Qtd Procedimentos': np.random.randint(1, 5, num_rows),
    'Cód do Grupo de Contrato': np.random.randint(1, 10, num_rows),
    'Plano - Código': np.random.randint(100000, 999999, num_rows),
    'Plano - Descrição': np.random.choice(['Plano1', 'Plano2', 'Plano3', 'Plano4'], num_rows),
    'GUIA': np.random.randint(100, 999, num_rows),
    'Especialidade - Codigo': np.random.randint(1000, 9999, num_rows),
    'Classe de procedimento': np.random.choice(['Cirurgia', 'Exame', 'Consulta'], num_rows),
    'Grupo Familiar': np.random.choice(['Familiar1', 'Familiar2', 'Familiar3'], num_rows),
    'CPF Titular': [fake.random_number(digits=11) for _ in range(num_rows)],
    'Carteirinha Titular': [str(fake.random_number(digits=5)) + '-A' for _ in range(num_rows)],
    'Nome Titular': [fake.name() for _ in range(num_rows)],
}

df = pd.DataFrame(data)

df = df.rename(columns={
    'Operadora': 'Operadora',
    'Código do Cliente': 'Codigo_do_Cliente',
    'Razão Social do Cliente': 'Razao_Social_do_Cliente',
    'Código do Associado': 'Codigo_do_Associado',
    'Nome do Associado': 'Nome_do_Associado',
    'Tipo de Associado': 'Tipo_de_Associado',
    'Sexo': 'Sexo',
    'Data de Nascimento': 'Data_de_Nascimento',
    'Grupo Tipo de Atendimento': 'Grupo_Tipo_de_Atendimento',
    'Valor': 'Valor',
    'Data do Atendimento': 'Data_do_Atendimento',
    'Competência': 'Competencia',
    'CGC do Prestador Local': 'CGC_do_Prestador_Local',
    'Nome do Prestador Local': 'Nome_do_Prestador_Local',
    'Especialidade - Descrição': 'Especialidade_Descricao',
    'Prestador Local Próprio': 'Prestador_Local_Proprio',
    'Cidade do Prestador Local': 'Cidade_do_Prestador_Local',
    'Estado do Prestador Local': 'Estado_do_Prestador_Local',
    'Código do Procedimento': 'Codigo_do_Procedimento',
    'Nome do Procedimento': 'Nome_do_Procedimento',
    'Código do CID': 'Codigo_do_CID',
    'Qtd Procedimentos': 'Qtd_Procedimentos',
    'Cód do Grupo de Contrato': 'Cod_do_Grupo_de_Contrato',
    'Plano - Código': 'Plano_Codigo',
    'Plano - Descrição': 'Plano_Descricao',
    'GUIA': 'GUIA',
    'Especialidade - Codigo': 'Especialidade_Codigo',
    'Classe de procedimento': 'Classe_de_procedimento',
    'Grupo Familiar': 'Grupo_Familiar',
    'CPF Titular': 'CPF_Titular',
    'Carteirinha Titular': 'Carteirinha_Titular',
    'Nome Titular': 'Nome_Titular'
})

print(df.head())

df.to_csv('dados_gerados.csv', index=False)