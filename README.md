# Dashboard Interativo: Análise de Salários no Mercado de Dados

## Sobre o Projeto

Este projeto é a culminação da **Imersão de Dados com Python da Alura**, uma jornada de aprendizado que me guiou do zero à criação e publicação de um dashboard interativo. 
O dashboard permite filtrar informações por ano, nível de experiência, tipo de trabalho e tamanho da empresa, fornecendo insights sobre o mercado de trabalho global de forma intuitiva.

---

## Jornada de Aprendizado: Da Teoria à Produção

O projeto foi construído em etapas, refletindo o processo de um cientista de dados:

### **Aula 1: Primeiros Passos e Exploração**

Nesta fase, utilizei o Google Colab para ter o primeiro contato com a manipulação de dados. A principal ferramenta foi a biblioteca **Pandas**, que usei para:
- **Carregar os dados** de um arquivo CSV.
- **Explorar o dataset** usando métodos como `.head()`, `.info()`, `.describe()` e `.shape` para entender sua estrutura, tipos de dados e medidas estatísticas básicas.
- **Limpar o conjunto de dados**, renomeando colunas e corrigindo valores categóricos para preparar a base para análises futuras.

### **Aula 2: Limpeza e Tratamento de Dados**

Aprofundando na qualidade dos dados, esta etapa foi crucial para garantir a confiabilidade das análises. Os principais pontos abordados foram:
- **Tratamento de dados ausentes (`NaN`)** usando o método `.dropna()` para remover linhas com valores nulos, uma estratégia segura quando a perda de dados é mínima.
- **Conversão de tipos de dados** com o método `.astype()` para garantir que colunas numéricas (como o ano) estivessem no formato correto (`int64`), removendo casas decimais indesejadas e facilitando as visualizações.

### **Aula 3: Análise Visual e Criação de Gráficos**

Esta foi a fase onde os conceitos de ADE foram aplicados na prática. Utilizando as bibliotecas **Seaborn**, **Matplotlib** e **Plotly**, criei uma série de gráficos para extrair insights:
- **Gráfico de Barras e Histograma:** Para visualizar a distribuição de variáveis categóricas (senioridade) e quantitativas (salários), respectivamente.
- **Boxplot:** Um gráfico poderoso para analisar a distribuição salarial por nível de experiência e identificar outliers (valores discrepantes).
- **Gráfico de Rosca:** Para mostrar a proporção de cada tipo de trabalho (remoto, presencial, híbrido), de forma interativa.

### **Aula 4: Dashboard Interativo e Publicação**

A etapa final do projeto, onde todo o aprendizado foi consolidado:
- **Configuração do Ambiente Local:** Migrei do Google Colab para o **VSCode**, configurando um ambiente virtual (`venv`) para gerenciar as bibliotecas do projeto de forma profissional.
- **Construção do Dashboard:** Usei a biblioteca **Streamlit** para transformar os códigos Python em uma aplicação web. A interface foi construída com filtros interativos na barra lateral e componentes como colunas para exibir métricas e gráficos.
- **O Desafio do Mapa:** Para responder ao desafio de visualizar a média salarial por país, utilizei a biblioteca **`pycountry`** para converter códigos de países e criei um mapa interativo (**Choropleth**) com o Plotly.
- **Publicação:** Por fim, utilizei o **GitHub** para versionar o código e o **Streamlit Cloud** para publicar o dashboard, tornando-o acessível a qualquer pessoa na internet.

---

## Tecnologias Utilizadas

- **Python**
- **Pandas**: Manipulação e análise de dados.
- **Streamlit**: Criação do dashboard interativo.
- **Plotly**: Visualização de dados interativa (gráficos e mapa).
- **Matplotlib/Seaborn**: Visualizações estáticas e análises estatísticas.
- **pycountry**: Conversão de códigos de países.
- **GitHub**: Controle de versão e hospedagem do código.
- **Streamlit Cloud**: Deploy (publicação) da aplicação.

---

## Autor

**Cleverson Moura Andrade**
