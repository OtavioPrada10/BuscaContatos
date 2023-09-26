import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BuscaContatos:
    def __init__(self):
        self.SITE_LINK = "https://www.linkedin.com/feed/"
        self.SITE_MAP = {
            "Login":{
                "Email": {
                    "xpath":"/html/body/div[1]/main/div/div/form/div[1]/div[1]/div/div/input"
                }
            }
        }
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)
        
    def loga(self):
        self.driver.find_element(self.SITE_MAP["Login"]["Email"]["xpath"]).click()
        time.sleep(10)
        


Contato = BuscaContatos()
Contato.abrir_site()
Contato.loga()