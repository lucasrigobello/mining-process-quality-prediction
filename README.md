# Case Predictive Qualidade de Minério - API com FastAPI
[![Docker Image CI](https://github.com/lucasrigobello/mining-process-quality-prediction/actions/workflows/docker-image.yml/badge.svg)](https://github.com/lucasrigobello/mining-process-quality-prediction/actions/workflows/docker-image.yml)

## 📌 Sobre o projeto
Este projeto de predição de qualidade de minério de ferro.
O processo de flotação, na indústria de mineração, é utilizado para concentrar o minério de ferro. A porcentagem de Ferro na entrada do processo é providenciado pelo planejamento de Lavra. Além do minério desejando, também, são encontrados impurezas, como Sílica. Assim, o objetivo do processo de flotação é aumentar a concentração de Ferro e remover as impurezas.
- Objetivo da Predição: estimar o valor de qualidade do concentrado, em termos de impureza, % Silica Concentrate (sílica no concentrado).

Os modelos são expostos via FastAPI, permitindo integração com sistemas de industriais de monitoramento e simulação de processo.

## 🚀 Tecnologias utilizadas
- **Python** (para implementação do modelo e da API)
- **FastAPI** (para exposição do modelo via API REST)
- **Scikit-learn** ( para framework para machine learning)
- **Docker** (para conteinerização da aplicação)
- **Kubernetes** (para orquestração e deploy)
- **Swagger** (para documentação da API)

## 📂 Estrutura do projeto
```bash
├── src
│   ├── classes/              # Código de objetos
│   ├── config/               # Configurações gerais do projeto
│   ├── models/               # Repositório do modelo / modelo em deploy
│   ├── utils/                # Código de funções
│   └── main.py               # Ponto de entrada da API
├── eda notebook/             # Pasta com estrutura de EDA e Treinamento do modelo
│   ├── config/               # Configurações gerais do projeto
│   ├── data/                 # Pasta para organização das bases de dados e dataset
│   ├── EDA Results/          # Repositório de resultados/imagens de EDA
│   ├── models/               # Pasta como repositório dos modelos treinados
│   └── eda notebook.ipynb    # Notebook com resultados de EDA e Treinamento do modelo
│
├── .github/                  # Workflows para Github Action
├── helm-charts/              # Manifests para deploy no Kubernetes
├── Dockerfile                # Configuração do container Docker
├── requirements.txt          # Dependências do projeto
├── LICENSE                   # Licença MIT
├── README.md                 # Documentação do projeto
└── .gitignore                # Arquivos ignorados no repositório Git
````

## 🛠 Como configurar o projeto
1.	Clone este repositório:

```bash
git clone https://github.com/lucasrigobello/mining-process-quality-prediction
cd mining-process-quality-prediction
````

2.	Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

3.  Para iniciar a API:
```bash
python src/main.py 
```

## 🖥️ Utilização da API
A API expõe um endpoint para prever % de Sílica no Concentrado:

- **POST** ```/predict/``` 
    - **Parâmetros:** ```{
                            "ironfeed": 70,
                            "silicafeed": 10,
                            "starchflow": 10,
                            "aminaflow": 10,
                            "oreflow": 10,
                            "oreph": 10,
                            "oredensity": 0,
                            "airflow01": 0,
                            "airflow02": 0,
                            "airflow03": 0,
                            "airflow04": 0,
                            "airflow05": 0,
                            "airflow06": 0,
                            "airflow07": 0,
                            "level01": 0,
                            "level02": 0,
                            "level03": 0,
                            "level04": 0,
                            "level05": 0,
                            "level06": 0,
                            "level07": 0
                                        }```
    - **Retorno:** ```{"% Silica Concentrate": "Valor predito"}```

## 📦 Executando com Docker
Para construir e executar o container:
```bash
docker build -t mining-process-quality-prediction .
docker run -p 8000:8000 mining-process-quality-prediction
```

## ☁️ Deploy no Kubernetes
Para implantar no Kubernetes, use os manifests disponíveis na pasta ```kubernetes/```:
```bash
kubectl apply -f ./helm-charts/templates/deployment.yaml
kubectl apply -f ./helm-charts/templates/service.yaml
```

## 📖 Documentação
A documentação da API pode ser acessada via Swagger em:
```
http://localhost:8000/docs
```

## 📜 Licença
Este projeto está sob a licença MIT.
________________________________________