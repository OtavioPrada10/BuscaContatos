import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from login import Login
from selenium.webdriver.common.by import By


class BuscaContatos:
    def __init__(self):
        self.SITE_LINK = "https://www.linkedin.com/"
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
    '''
    Função responsavel por entrar no site solicitado neste contexto o Linkedin
    :param self
    '''
    def abrirSite(self):
        time.sleep(1)
        self.driver.get(self.SITE_LINK)
        time.sleep(1)
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
    def buscaEmpresa(self, nomeEmpresa):
        #Busca o elemnto da barra de pesqisa
        barraPesquisa = self.driver.find_element('css selector', '#global-nav-typeahead > input')
        barraPesquisa.send_keys(nomeEmpresa)
        barraPesquisa.send_keys(Keys.RETURN)
        filtroEmpresa = self.driver.find_element('css selector', '#search-reusables__filters-bar > ul > li:nth-child(2) > button')
        filtroEmpresa.click()
