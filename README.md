# Projetos5
Projeto ProDataViz para a SafeCare: Transformando Dados em Insights Estratégicos

Em um cenário empresarial cada vez mais dinâmico, a capacidade de compreender e interpretar dados é crucial para o sucesso organizacional. Nesse contexto, surge o projeto ProDataViz, uma iniciativa voltada para a análise e visualização de dados da renomada empresa SafeCare. O objetivo central é potencializar a capacidade da SafeCare em tomar decisões fundamentadas e estratégicas por meio da interpretação visual de seus dados corporativos.

Objetivo do Projeto:
O ProDataViz visa proporcionar à SafeCare uma visão aprofundada e intuitiva de suas métricas operacionais, financeiras e de desempenho. Ao transformar dados brutos em visualizações claras e informativas, a empresa terá a capacidade de identificar padrões, tendências e oportunidades de melhoria de forma rápida e eficaz.

Metodologia:
A implementação do projeto seguirá uma abordagem estruturada, iniciando com a identificação das necessidades específicas da SafeCare. Serão realizadas reuniões para compreender os objetivos estratégicos da empresa, os principais indicadores de desempenho desejados e os desafios enfrentados na interpretação dos dados existentes.

Posteriormente, será desenvolvido um plano personalizado de análise de dados, utilizando ferramentas avançadas de visualização. A seleção cuidadosa de gráficos, dashboards interativos e outras técnicas visuais permitirá à SafeCare explorar dados complexos de maneira acessível, promovendo uma compreensão mais profunda e facilitando a tomada de decisões fundamentadas.

Benefícios Esperados:

Tomada de Decisão Embasada: Visualizações claras e intuitivas facilitarão a interpretação dos dados, capacitando os tomadores de decisão da SafeCare a agir com base em informações sólidas.

Identificação de Oportunidades: A análise aprofundada revelará oportunidades de melhoria operacional, identificação de nichos de mercado e otimização de recursos.

Monitoramento Contínuo: A implementação de dashboards interativos permitirá à SafeCare monitorar continuamente seus indicadores de desempenho, promovendo uma abordagem proativa na gestão.

Compartilhamento de Informações: A geração de relatórios visuais facilitará a comunicação interna e externa, permitindo à SafeCare compartilhar eficientemente insights valiosos com partes interessadas e colaboradores.

Compromisso com a Segurança:
Reconhecendo a importância dos dados sensíveis da SafeCare, o ProDataViz implementará rigorosas medidas de segurança para garantir a confidencialidade e integridade das informações.

Conclusão:
O projeto ProDataViz representa uma parceria estratégica para a SafeCare, capacitando-a a explorar o potencial máximo de seus dados. Ao adotar uma abordagem centrada na visualização, a empresa estará posicionada para enfrentar os desafios do mercado com confiança, transformando dados em ativos valiosos para a tomada de decisões estratégicas e o sucesso sustentável a longo prazo.

# Instruções para Conectar um Banco de Dados ao Metabase Usando Docker Desktop e Windows
Este README descreve o processo de configuração e execução do Metabase em conjunto com um banco de dados PostgreSQL usando Docker. O Metabase é uma ferramenta de visualização de dados que permite criar painéis e relatórios a partir de fontes de dados. Caso você esteja usando **wsl** ou **linux**, ao executar o **script run_all.sh**, o processo é automatizado! Para isso, é necessário criar um arquivo chamada ip_adress.txt, e colocá-lo na mesma pasta do seu projeto, junto com o arquivo csv, e os jobs.py

## Pré-requisitos
Antes de começar, certifique-se de ter instalado os seguintes componentes:
 
**Docker Desktop:** Certifique-se de que o Docker Desktop esteja instalado em seu sistema. Você pode baixá-lo em Docker Desktop.

**Python:** É necessário ter o Python instalado. Recomendamos a versão 3.10 ou 3.11, pois a versão 3.12 pode não ser compatível com a biblioteca psycopg2, que será necessária.

**Bibliotecas Python:** Instale as seguintes bibliotecas Python executando os seguintes comandos no terminal:

```
pip install sqlalchemy
pip install psycopg2
pip install pandas
```
## Configurando o Banco de Dados PostgreSQL
Antes de executar o Metabase, você deve configurar um banco de dados PostgreSQL. Siga estas etapas:

1. Certifique-se de que o arquivo de banco de dados que você deseja usar esteja na mesma pasta dos scripts job_1.py e job_2.py.

2. Inicialize o Docker Desktop.

3. No terminal, execute os seguintes comandos para baixar e executar uma instância do PostgreSQL usando o Docker:

```
docker pull postgres:latest
docker run --name etl-database -e POSTGRES_PASSWORD=root -d -p 5432:5432 postgres:latest
```
4. Conecte-se ao banco de dados PostgreSQL com o comando psql:
```
docker run -it --network=host postgres /bin/bash
psql -h SEUIP -U postgres
```
Certifique-se de substituir **SEUIP** pelo seu endereço IP. Você pode verificar o IP usando **ipconfig** (Windows) ou **ifconfig** (Linux).

5. No prompt do psql, crie um banco de dados com o nome "etl-database":

```
CREATE DATABASE "etl-database";
```
6. Para sair do prompt psql, digite:

```
\q
```

7.E, em seguida, saia do contêiner Docker:
```
\exit
```

## Executando os Scripts ETL

Agora, você pode executar os scripts **job_1.py** e **job_2.py** para realizar a extração, transformação e carregamento de dados.

## Configurando e Executando o Metabase
Para configurar e executar o Metabase, siga estas etapas:

1. Baixe a imagem mais recente do Metabase do Docker Hub:

```
docker pull metabase/metabase:latest
```

2. Execute o Metabase em um contêiner Docker:
```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```
3. Agora, abra um navegador da web e acesse o Metabase digitando o seu endereço IP seguido de :3000 (a porta padrão do Metabase). Por exemplo:
```
http://SEUIP:3000
```
Você será direcionado para a interface do Metabase, onde poderá configurar fontes de dados, criar painéis e relatórios.


