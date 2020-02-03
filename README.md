### Flask tutorial 

Este repositório de código tem o objetivo de introduzir o uso do _framework web_ [Flask](https://www.palletsprojects.com/p/flask/), com exemplos simples de aplicações que podem ser utilizadas para análise de dados.

### Instalando Conda 

Iniciaremos utilizando [Conda](https://docs.conda.io/en/latest/), uma aplicação utilizada para gerenciar ambientes (_environments_), facilitando a instalação de _software_.

Abra o terminal e copie e cole as seguintes linhas para instalar o Conda.

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
```

Reinicie o terminal e faça

```
which conda
```

### Criando uma aplicação com Flask

Clone o presente diretório fazendo:

```
git clone https://github.com/computational-chemical-biology/flask_tutorial.git
# Entre no diretório
cd flask_tutorial
```

Dentro do diretório temos três aplicações com níveis crescentes de complexidade, `gaussian`, `upload_plot` e `complex`.

Antes de testar estas aplicações, vamos construir nossa primeira aplicação. Crie um diretório:

```
mkdir app
cd app
```
Crie e ative um ambiente com _Conda_:

```
conda create -n myapp python=3
conda activate myapp
```

Instale o Flask

```
# Onde meus módulos serão instalados?
which pip
pip install flask
```

Abra seu [IDE](https://www.sublimetext.com/) e cole o código abaixo no IDE

```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Alô, alô Terezinha!'

if __name__ == '__main__':
    app.run()
```

e salve como **app.py** e execute a aplicação fazendo:

```
python app.py
```

Acessando o seu navegador [http://0.0.0.0:5000](http://0.0.0.0:5000)

Você deve observar a impressão da mensagem _Alô, alô Terezinha!_.

A [aplicação web](http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html) submete requisições do navegador a uma aplicação. 


### Entendendo as aplicações exemplo

Para entender as aplicações exemplo, volte ao diretório __flask_tutorial__ e execute:

```
# se o app ainda está sendo executado pressione CTR+C
cd ..
# saia do ambiente atual
conda deactivate
# instale um ambiente para os testes
conda env create -f environment.yml
conda activate flask_tutorial
```

Após instalado o ambiente, abra outro terminal, navegue até o diretório e execute o jupyter:

```
cd flask_tutorial
conda activate flask_tutorial
jupyter notebook
```

Leia atentamente as explicações para cada aplicação.

No outro terminal, entre nos diretórios de cada uma das aplicações `gaussian`, `upload_plot`, `complex` e inspecione o código _app.py_ com o IDE, execute a aplicação como realizado acima. Note que a url presente no decorador (sentença seguida por @) de cada função levará a uma url específica que deve ser acessada no navegador, exemplo http://0.0.0.0:5000/NOME. Para a aplicação `upload_plot` utilize o arquivo 'data.tsv', dentro do diretório 'flask_tutorial' para testar. Abra o arquivo no modo gráfico, clicando duas vezes, para inspecionar o conteúdo.

Após executar a aplicação, faça uma apresentação explicando como ela funciona, pesquise na internet como fazer outra figura com a mesma aplicação e modifique a apresentação.


### Avançado

Uma alternativa para executar a aplicação é utilizar o servidor [gunicorn](https://gunicorn.org/). Abra o arquivo __run_server.sh__ com o seu IDE e inspecione o arquivo. 

```
conda activate flask_tutorial
# Para ver as opções do gunicorn, faça
gunicorn -h
# Para executar, faça
sh run_server.sh
```

Outra alternativa é o gerenciador de ambientes [Docker](https://www.docker.com/), que facilita a criação e compatilhamento de aplicações.

Para utilizar o Docker com a aplicação `complex` faça:

```
cd complex
docker build -t complex .
```

Abra o arquivo `Makefile` e veja comandos do Docker presente. 

```
# Voltando ao terminal, se a aplicação ainda estiver sendo executada, faça
# CTR+C e depois
make build
```

### Notas

Caso sejam feitas modificações/adições de módulos:

```
conda env export | grep -v "^prefix: " > environment.yml
```

### Reference tutorials:

