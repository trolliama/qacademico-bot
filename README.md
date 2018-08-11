# bot-selenium
Esse é um script para preencher um formulário obrigatório do q-acadêmico. <br>

É usada a biblioteca Selenium para Python-3.X.X.  Para instalar as dependências use: <br><br>
```
pip3 install -r requires.txt </b>
```  
Para instalar o driver <b>Geckodriver</b> abra o terminal e digite:

**Para sistemas x64**
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz
```
**E para Arquiteturas x32**
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux32.tar.gz
```
E em seguida, no mesmo diretório
```
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
```
E **pronto**!, é só usar seu editor de texto de preferência e editar as linhas **20** e **21** do arquivo **bot_answer.py**
Em seguida, para executar, use:
```
python3 ./bot_answer.py
```
