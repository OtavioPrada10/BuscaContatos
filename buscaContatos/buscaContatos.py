import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from login import Login
from selenium.webdriver.common.by import By
from parsel import Selector
import csv


class BuscaContatos:
    def __init__(self):
        self.SITE_LINK = "https://www.linkedin.com/"
        self.SITE_GOOGLE = "https://www.google.com/"
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
    '''
    Função responsavel por entrar no site solicitado neste contexto o Linkedin
    :param self
    '''
    def abrirSite(self):
        sleep(1)
        self.driver.get(self.SITE_LINK)
        sleep(1)
    '''
    Função responsavel por efetuar o login
    '''
    def loga(self):
        usuario_input = self.driver.find_element('name', 'session_key')
        usuario_input.send_keys(Login.EMAIL)

        senha_input = self.driver.find_element('name', 'session_password')
        senha_input.send_keys(Login.SENHA)
        senha_input.send_keys(Keys.RETURN)
    '''
    Função responsavel por fazer a busca pelo nome da empresa
    :param Nome da empresa
    '''
    def buscaEmpresa(self, nomeEmpresa, cargo, cidade):
        # arquivo csv
        writer = csv.writer(open('LinksContatos.csv', 'w', encoding='utf-8'))
        writer.writerow(['Link'])

        self.driver.get(self.SITE_GOOGLE)
        sBusca = 'site:linkedin.com/in'
        sBusca = sBusca+ ' and '+ nomeEmpresa #site:linkedin.com/in and Lean Sales 
        if(cargo):
            sBusca = sBusca+ ' and '+ cargo       #site:linkedin.com/in and Lean Sales and programador
        if cidade:
            sBusca = sBusca+ ' and '+ cidade      #site:linkedin.com/in and Lean Sales and programador and rio do sul
            time.sleep(1)
        oBarraBuscaGoogle = self.driver.find_element('name', 'q')
        oBarraBuscaGoogle.send_keys(sBusca)
        oBarraBuscaGoogle.send_keys(Keys.RETURN)
        lista_perfil = self.driver.find_elements('xpath','//div[@class="yuRUbf"]/div/span/a')
        lista_perfil = [perfil.get_attribute('href') for perfil in lista_perfil]
        for perfil in lista_perfil:
            sleep(2)
            # response = Selector(text=self.driver.page_source)
            # url_perfil = self.driver.current_url
            # escrever no arquivo csv
            writer.writerow([perfil])
        # sair do driver
        self.driver.quit()  
