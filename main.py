import openpyxl
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#1- Acesse o site do G1 (ou outro portal de notícias).
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(), options=chrome_options)

driver.maximize_window()
driver.get('https://g1.globo.com')


#2- Busque por uma palavra-chave (ex: tecnologia, economia, esportes).
botao_pesquisa = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='BUSCAR']"))
)
# botao_pesquisa = driver.find_element(By.XPATH,"//input[@placeholder='BUSCAR']")
botao_pesquisa.send_keys("Tecnologia")
botao_pesquisa.send_keys(Keys.ENTER)
sleep(5)


# laço principal das notícias
noticias = driver.find_elements(By.XPATH,"//li[@class='widget widget--card widget--info']")
for i, noticia in enumerate (noticias[:10],start=1):

    #3- Extraia os títulos das notícias, os resumos e o link da matéria.
    try:
        titulos_noticias = noticia.find_element(By.XPATH,".//div[@class='widget--info__title product-color ']").text
    except:
        titulos_noticias = "Sem Título"
    try:
        resumo_noticias = noticia.find_element(By.XPATH,".//p[@class='widget--info__description']").text
    except:
        resumo_noticias = "Sem resumo"
    
    try:
        link_noticias = noticia.find_element(By.XPATH,".//a").get_attribute("href")
    except:
        link_noticias = "Sem link"

    print(f"\nNotícia {i}")
    print("Título:", titulos_noticias)
    print("Resumo:", resumo_noticias)
    print("Link:", link_noticias)
    
    #4- Salve tudo em um Excel organizado com openpyxl.
