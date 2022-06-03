from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico) # criação instância navegador

navegador.get("https://google.com")


navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('aisweb')

time.sleep(50)


