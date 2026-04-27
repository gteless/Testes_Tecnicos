import time
import logging
from src.config import URL_AMAZON, AMAZON_EMAIL, AMAZON_PASSWORD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


def configurar_driver(headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def buscar_produtos_amazon(produto_alvo, visual=True):
    driver = configurar_driver(headless=not visual)
    wait = WebDriverWait(driver, 15)
    dados_finais = []

    try:
        # Acesso ao Login
        logger.info(f"Acessando o site da Amazon pela URL: {URL_AMAZON}")
        driver.get(URL_AMAZON)

        # Fluxo de Login
        logger.info(f"Aguarda o carregamento do campo de e-mail e digita o e-mail do usuário: {AMAZON_EMAIL}")
        wait.until(EC.presence_of_element_located((By.ID, "ap_email_login"))).send_keys(AMAZON_EMAIL)
        logger.info(f"E-mail digitado com sucesso, clicando em continuar.")
        driver.find_element(By.ID, "continue").click()
        
        logger.info(f"Aguarda o carregamento do campo de senha e digita a senha do usuário.")
        wait.until(EC.presence_of_element_located((By.ID, "ap_password"))).send_keys(AMAZON_PASSWORD)
        logger.info(f"Senha digitada com sucesso, clicando em login.")
        driver.find_element(By.ID, "signInSubmit").click()

        # Tratamento de CAPTCHA
        if "captcha" in driver.page_source.lower() or driver.title == "Amazon.com.br":
            print("Amazon solicitou verificação humana. Resolva no navegador.")
            logger.info(f"Amazon solicitou verificação humana. Resolva no navegador.")
            # No modo headless isso falharia, por isso o modo visual é importante no 1º acesso
            time.sleep(15) 

        # Realizar Busca
        logger.info(f"Clica no campo de pesquisa da Amazon")
        busca = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
        logger.info(f"Digita o produto alvo: {produto_alvo}")
        busca.send_keys(produto_alvo)
        logger.info(f"Manda a tecla ENTER para realizar a pesquisa")
        busca.send_keys(Keys.ENTER)

        # Coleta de Itens
        logger.info(f"Inicia a coleta dos resultados.")
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
        cards = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')

        for card in cards:
            try:
                titulo = card.find_element(By.TAG_NAME, "h2").text
                # Captura preço completo (Inteiro + Centavos)
                parte_inteira = card.find_element(By.CLASS_NAME, "a-price-whole").text
                parte_decimal = card.find_element(By.CLASS_NAME, "a-price-fraction").text
                preco = f"R$ {parte_inteira},{parte_decimal}"
                dados_finais.append({"titulo": titulo, "preco": preco})
            except:
                continue # Ignora itens sem preço (ex: anúncios ou produtos esgotados)

    finally:
        driver.quit()
    
    return dados_finais