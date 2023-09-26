import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BuscaContatos:
    def __init__(self):
        self.SITE_LINK = "https://www.linkedin.com/"
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(4)
        
    def loga(self):
        usuario_input = self.driver.find_element('name', 'session_key')
        usuario_input.send_keys("xxxxxx@xxxxxx.com")

        senha_input = self.driver.find_element('name', 'session_password')
        senha_input.send_keys("XXXXXXXXXXXX")
        time.sleep(5)
        senha_input.send_keys(Keys.RETURN)


Contato = BuscaContatos()
Contato.abrir_site()
Contato.loga()
