from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

import csv

db_host = "172.20.0.1"  # Endereço IP do servidor PostgreSQL...
db_port = "5432"       
db_name = "etl-database"   
db_user = "postgres"  
db_password = "root"

db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class DataSafe(Base):
    __tablename__ = 'DataSafe'

    id = Column(Integer, primary_key=True)
    Operadora = Column(String(100))
    Codigo_do_Cliente = Column(Integer)
    Razao_Social_do_Cliente = Column(String(100))
    Codigo_do_Associado = Column(Integer)
    Nome_do_Associado = Column(String(100))
    Tipo_de_Associado = Column(String(100))
    Sexo = Column(String(100))
    Data_de_Nascimento = Column(Date)
    Grupo_Tipo_de_Atendimento = Column(String(100))
    Valor = Column(Integer)
    Data_do_Atendimento = Column(Date)
    Competencia = Column(String(50))
    CGC_do_Prestador_Local = Column(String(100))
    Nome_do_Prestador_Local = Column(String(100))
    Especialidade_Descricao = Column(String(100))
    Prestador_Local_Proprio = Column(Integer)
    Cidade_do_Prestador_Local = Column(String(100))
    Estado_do_Prestador_Local = Column(String(100))
    Codigo_do_Procedimento = Column(Integer)
    Nome_do_Procedimento = Column(String(100))
    Codigo_do_CID = Column(String(100))
    Qtd_Procedimentos = Column(Integer)
    Cod_do_Grupo_de_Contrato = Column(Integer)
    Plano_Codigo = Column(String(100))
    Plano_Descricao = Column(String(100))
    GUIA = Column(Integer)
    Especialidade_Codigo = Column(Integer)
    Classe_de_procedimento = Column(String(100))
    Grupo_Familiar = Column(String(100))
    CPF_Titular = Column(String(100))
    Carteirinha_Titular = Column(String(100))
    Nome_Titular = Column(String(100))

Base.metadata.create_all(engine)

csv_file = 'dados_gerados.csv'

try:
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
           
            Base_data = DataSafe(
                Operadora=row[0],
                Codigo_do_Cliente=int(row[1]),
                Razao_Social_do_Cliente=row[2][:100],  # Limita o tamanho para 100 caracteres
                Codigo_do_Associado=int(row[3]),
                Nome_do_Associado=row[4][:100],  # Limita o tamanho para 100 caracteres
                Tipo_de_Associado=row[5][:100],  # Limita o tamanho para 100 caracteres
                Sexo=row[6][:100],  # Limita o tamanho para 100 caracteres
                Data_de_Nascimento=datetime.strptime(row[7], '%Y-%m-%d').date(),
                Grupo_Tipo_de_Atendimento=row[8][:100],  # Limita o tamanho para 100 caracteres
                Valor=float(row[9]),  # Alterado para Float
                Data_do_Atendimento=datetime.strptime(row[10], '%Y-%m-%d').date(),
                Competencia=row[11][:50],  # Limita o tamanho para 50 caracteres
                CGC_do_Prestador_Local=row[12][:100],  # Limita o tamanho para 100 caracteres
                Nome_do_Prestador_Local=row[13][:100],  # Limita o tamanho para 100 caracteres
                Especialidade_Descricao=row[14][:100],  # Limita o tamanho para 100 caracteres
                Prestador_Local_Proprio=int(row[15]),
                Cidade_do_Prestador_Local=row[16][:100],  # Limita o tamanho para 100 caracteres
                Estado_do_Prestador_Local=row[17][:100],  # Limita o tamanho para 100 caracteres
                Codigo_do_Procedimento=int(row[18]),
                Nome_do_Procedimento=row[19][:100],  # Limita o tamanho para 100 caracteres
                Codigo_do_CID=row[20][:100],  # Limita o tamanho para 100 caracteres
                Qtd_Procedimentos=int(row[21]),
                Cod_do_Grupo_de_Contrato=int(row[22]),
                Plano_Codigo=row[23][:100],  # Limita o tamanho para 100 caracteres
                Plano_Descricao=row[24][:100],  # Limita o tamanho para 100 caracteres
                GUIA=int(row[25]),
                Especialidade_Codigo=int(row[26]),
                Classe_de_procedimento=row[27][:100],  # Limita o tamanho para 100 caracteres
                Grupo_Familiar=row[28][:100],  # Limita o tamanho para 100 caracteres
                CPF_Titular=row[29][:100],  # Limita o tamanho para 100 caracteres
                Carteirinha_Titular=row[30][:100],  # Limita o tamanho para 100 caracteres
                Nome_Titular=row[31][:100]  # Limita o tamanho para 100 caracteres
            )

            session.add(Base_data)

        session.commit()

        print("Commit successful")

except Exception as e:
    print(f"Error: {e}")
finally:
    session.close()
