# [dadosfera.ai](https://dadosfera.ai/)  

With [Kanban](https://trello.com/b/6TZ1gF76/dadosfera) you can manage this project    
- [Home](https://app.dadosfera.ai/en-US/) Dadosfera  
- [Metabase](https://metabase-treinamentos.dadosfera.ai/) de treinamentos da Dadosfera  
- [Módulo de Inteligência](https://app-intelligence-treinamentos.dadosfera.ai/) da Dadosfera  
- [E-commerce Case](https://app-intelligence-treinamentos.dadosfera.ai/pipeline?project_uuid=dc2f4baf-ea3e-4287-8e36-383eb4f77c1d&pipeline_uuid=50b28133-3610-49c0-b15e-138a0f8c33b4) no Módulo de Inteligência  

## Time management using [pomodoro](/pomodoro.csv)

[Context of this case](https://docs.google.com/document/d/1mZ2trmr7D-0Vr297WOJQNhQM0g1tmSF-laQprPqeY_Y/edit?usp=sharing)  

0. [Kanban Board about the E-commerce Case](https://trello.com/b/6TZ1gF76/dadosfera)  
1. [About the Database](./generate-synthetic-data.py/)   
2. [About Dadosfera - Integrate](./img/upload-tables.png)  
3. [About Dadosfera - Explore](https://metabase-treinamentos.dadosfera.ai/collection/671-colecao-pessoal-de-luizotavioautomacao-treinamentos)  
    - [catalog KPI(s)](./img/upload-tables.png)  
    - [catalog tables/collections](./img/catalog2.png)  
    - [catalog automatic](./img/catalog3.png)  
4. About Data Quality  
5. About using GenAI and LLMs - Process  
6. [About Data Modeling](https://trello.com/c/pl3OeNJ5/23-6-sobre-modelagem-de-dados)  
7. [About Data Analysis - Analyze](https://metabase-treinamentos.dadosfera.ai/dashboard/160-dashboard-e-commerce?tab=9-aba-1)  
    - [Total Sales](./img/total-sales.png)  
    - [Average Ticket](./img/average-ticket.png)  
    - [Total Orders](./img/order.png)  
    - [Monthly Sales](./img/monthly-sales.png)  
    - [LTV](./img/LTV.png)  
8. [About Pipelines](https://app-intelligence-treinamentos.dadosfera.ai/pipeline?project_uuid=dc2f4baf-ea3e-4287-8e36-383eb4f77c1d&pipeline_uuid=50b28133-3610-49c0-b15e-138a0f8c33b4)  
9. [Sobre Data Apps](/img/data-apps.png)  
10. [Case apresentation](https://docs.google.com/presentation/d/1xCvihPQVDYsewTFi6hq6VRbWaOJudJoPRytGWiU7vm0/edit?usp=sharing)  

<!-- [Video of this projetct]()   -->
- [User jorney](/img/user-jorney.png)  
- [Performance analysis of company professionals](https://trello.com/c/o33iEneJ/2-an%C3%A1lise-de-desempenho-de-profissionais-da-empresa)  
- [Route Optimization](https://trello.com/c/GpIQZ4FV/3-otimiza%C3%A7%C3%A3o-rotas-log%C3%ADsticas)  
- [End-point in Flask to fetch kpis processed in pipeline](./img/api.png)  
- [WebScraping](https://trello.com/c/q3zeM3WE/36-webscraping-do-site-da-magalu)  
- [Streamlit access endpoint and create dashboards and kpis](./img//dashboard.png)  
- [Represent interdependencies and critical points of the project](https://trello.com/c/GcvRMevg/5-representar-interdepend%C3%AAncias-e-pontos-cr%C3%ADticos-do-projeto)  
- [Risk analysis, cost estimates and resource allocation](https://trello.com/c/lCVk2lMY/4-an%C3%A1lises-de-risco-estimativas-de-custos-e-aloca%C3%A7%C3%A3o-de-recursos)  
- [Draw the diagram representing the proposed final DW layers](https://miro.com/app/board/uXjVKhhLbUM=/?share_link_id=422827693134)  
- [Processing-of-unstructured-ad-data](https://trello.com/c/UlHHejQx/1-processamento-de-dados-desestruturados-de-an%C3%BAncios)  

## [Generate Synthetic Data](./generate-synthetic-data.py/)  
#### To generate synthetic data, we can use the `pandas` library to create a DataFrame with random  
 - install dependencies: `make i`   
 - generate synthetic data: `make g`  

## Docs and [References](https://trello.com/c/pYHZjT8p/21-refer%C3%AAncias)
 - [Apresentation](https://docs.google.com/presentation/d/1xCvihPQVDYsewTFi6hq6VRbWaOJudJoPRytGWiU7vm0/edit?usp=sharing)  
 - [Key Performance Indices](https://docs.google.com/document/d/19pY2qD9arGb413rYfRLJQIyi-qh-5OrXx0Hw32yhB84/edit?usp=sharing)   
 - [Improvements during the dadosfera journey](https://docs.google.com/document/d/1tJErv_qk8IVRQDJPHScZyLJPXpj5u8senv8zGsERluc/edit?usp=sharing)  
 - [Intelligence Module](https://docs.google.com/document/d/1jTreSvX2p8NYafMrLVt7fP-_R-n6KR5nHUK0bfbvuLQ/edit?usp=sharing)  
 - [Data Quality](https://docs.google.com/document/d/1-R6fJG-oOl7djTnm_s9nxKv6FZplP7HBnVwKYeBPEgA/edit?usp=sharing)  
 - [Terms and Services of Dadosfera](https://docs.google.com/document/d/1NocVfFwGnuHN1txQHNvK6n0IJE588Z2fH0NRlOuRe3w/edit?usp=sharing)  
 - [Mind map of Módulo de Inteligência](https://miro.com/app/board/uXjVKhhLbUM=/?share_link_id=897532648866)  
 - [Dadosfera login API](https://docs.dadosfera.ai/reference/authcontroller_signin)  

## Data Life Cycle in Dadosfera
- [What is Data Lake](https://docs.google.com/document/d/1rf3_g0txT6ub24TunV-Og84e7OKhgc8T-G1ZZDGwYFA/edit?usp=sharing)  
![Data Life Cycle](./img/data-life-cycle.png)

 ## About DataLake e DataWareHouse
 &nbsp;              | DataLake                                                          | DataWareHouse  
 ---------           | -------                                                           | ------
 Estrutura de Dados  | Crua, Sem estrutura, Semi estruturado e Estruturado               | Estruturado e Processado (sanitilzado)  
 Finalidade de Dados | Ainda não determinado                                             | Atualmente em uso  
 Usuários            | Cientistas, arquiteto e engenheiro de dados, Analista de negócios | Profissionais de negócios e times de dados  
 Acessibilidade      | Altamente acessíveis e rápido de atualizar                        | Mais complicado e caro para fazer alterações  
 Consulta            | Sem otimização                                                    | Altamente otimizada
 Uso                 | Complexo e mais difícil                                           | Facilitado  