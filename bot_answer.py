from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MyBot():

    def __init__(self):
        """ Abre navegador e cria conexão, também informa os dados 
        de login para iniciar sessão."""

        self.browser = webdriver.Firefox()
        self.browser.get("https://academicoweb.ifg.edu.br/qacademico/index.asp?t=1001")

        self.login_values = {
                'login': 'MATRÍCULA',
                'pass': 'SENHA'
            }

    def entryLogin(self):
        """Função para preencher formulário de login"""

        login = self.browser.find_element_by_id("txtLogin")
        login.clear()
        login.send_keys(self.login_values['login'])

        passwd = self.browser.find_element_by_id("txtSenha")
        passwd.clear()
        passwd.send_keys(self.login_values['pass'] + Keys.RETURN)

    def getLinks(self):
        """Coletar os endereços de cada formulário e coloca-los
        em uma lista."""

        tags = WebDriverWait(self.browser,10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@class='conteudoLink']"))
        )

        print(tags)

        self.linksList = [tag.get_attribute('href') for tag in tags]
    
    def entryLinks(self):
        """ Func para entrar nos links"""

        for link in self.linksList:
            self.browser.get(link)
            self.fillForm()

    def fillForm(self):
        """ Função para preencher os formulários """

        tags_span = self.browser.find_elements_by_class_name('textoResposta')
        initial_value = 435 # valor inicia do atributo value da tag input,
                            # é aumentado 10 a cada tag span

        for span in tags_span:
            random_num = randint(value, value + 10) # value + 10 é o valor da ultima tag input da tag span selecionada

            op_input = span.find_element_by_xpath("//input[@value='%i']"%random_num)
            op_input.click()
            
            value += 11 # aumentar valor do value para próxima span.

        self.browser.find_element_by_id('Enviar').click()
        

if __name__ == '__main__':
    bot = MyBot()

    bot.entryLogin()
    bot.getLinks()
    bot.entryLinks()
