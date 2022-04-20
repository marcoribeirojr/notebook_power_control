# Controle de nível de bateria notebook

Controle de nível de bateria de notebook de forma automatizada utilizando tomada inteligente acionada através de uma URL.  

Após a execução do código, o dispositivo inteligente é acionado de acordo com o nível de bateria do aparelho.

**Possível caso de uso:**

Tomada inteligente com acionamento por URL controlado através da plataforma IFTT

### Clonando o projeto
```
git clone https://github.com/marcoribeirojr/notebook_power_control.git
```

### Instalando as dependências do projeto
```
pip install python-decouple notify
```

### Configurando o projeto

Renomear o arquivo [.env_modelo](.env_modelo) na raiz do projeto para ```.env``` e definir conforme segue:

- ```min``` e ```max``` definem o nível mínimo e máximo da bateria do notebook.

- URL de acesso ao dispositivo inteligente: ```url_power_on``` e ```url_power_off```.

*Estão configurados por padrão o valor mínimo como 20% e máximo de 80% com intuito de melhorar a vida útil da bateria do dispositivo.*



### Executando o projeto
```
python main.py
```
