# IMA

## PT: 
IMA ( Automação de Mapeamento de Infraestrutura ) é um aplicativo de código aberto feito com Python Kivy e integrado a nuvem pública da AWS ( a ideia é expandir para outras Cloud Providers ) para ajudar na captura e na organização dos serviços em execução no ambiente de nuvem.

### Requisitos:
- Python 3.8.0 ou superior
- pip3 já instalado
- Verifique se você já instalou o aws cli. Siga as instruções no link para instalar o aws cli: [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

### Instalar a aplicação:
1. Para instalar a aplicação primeiro clone o repositório:
```git
git clone https://github.com/NicolasThiesen/IMA.git
```
2. Atualiza, instala as dependências e cria um ambiente virtual:

- No Windows:
```shell
python -m pip install --upgrade pip setuptools virtualenv
cd IMA
python -m virtualenv kivy_venv
kivy_venv\Scripts\activate
pip3 install -r requirements.txt
```
- No linux:
```shell
python -m pip install --upgrade pip setuptools virtualenv
cd IMA
python -m virtualenv kivy_venv
source kivy_venv/bin/activate
pip3 install -r requirements.txt
```

3. Rode a aplicação
```shell
cd app
python app.py
```

## ENG: 
IMA ( Infrastructure Mapping Automation ) is a open source application made on Python Kivy and integrated with AWS ( the ideia is expand to others Cloud Providers ) to help capture and organize all services running on the cloud environmen.  

### Requirements
- Python 3.8.0 or higher
- pip3
- Make shure you have already installed the aws cli. Follow the instructions on the link to install aws cli: [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

### Install application:

1. Firs clone the repository:
```git
git clone https://github.com/NicolasThiesen/IMA.git
```
2. Update pip, install the dependencies and create virtualenv:

- On Windows:
```shell
python -m pip install --upgrade pip setuptools virtualenv
cd IMA
python -m virtualenv kivy_venv
kivy_venv\Scripts\activate
pip3 install -r requirements.txt
```
- On linux:
```shell
python -m pip install --upgrade pip setuptools virtualenv
cd IMA
python -m virtualenv kivy_venv
source kivy_venv/bin/activate
pip3 install -r requirements.txt
```
3. Run the application:
```shell
cd app
python app.py
```
