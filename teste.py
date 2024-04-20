from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Caminho do driver do Chrome
service = Service(executable_path='./chromedriver.exe')

# Opções do Chrome (opcional)
options = webdriver.ChromeOptions()

# Iniciar o navegador Chrome
navegador = webdriver.Chrome(service=service, options=options)

# URL do portal
url_portal = "https://yduqs.service-now.com/esc?id=ec_dashboard"

# Abrir a URL
navegador.get(url_portal)

# Aguardar página carregar
wait = WebDriverWait (navegador, 10)
wait.until(EC.presence_of_all_elements_located(By.XPATH, '//*[@id="favorites"]/i'))

# Xpath do botão Favoritos
xpath_btn_favoritos = '//*[@id="favorites"]/i'

# Clicar no botão Favoritos
btn_favoritos = navegador.find_element(By.XPATH, xpath_btn_favoritos)
btn_favoritos.click()

# Repetir o processo 5 vezes
for _ in range(5):
    # Xpath da solicitação
    xpath_solicitacao = "//*[@id='favorite_card_f82c61861bcd2150ff94404be54bcbf3']"

    # Clicar na solicitação
    solicitacao = navegador.find_element(By.XPATH, xpath_solicitacao)
    solicitacao.click()

    # Id do campo Descrição
    id_campo_descricao = "//*[@id='sp_formfield_descricao']"

    # Texto para a descrição
    texto_descricao = "Suporte de laboratório."

    # Preencher o campo Descrição
    campo_descricao = navegador.find_element(By.ID, id_campo_descricao)
    campo_descricao.clear()
    campo_descricao.send_keys(texto_descricao)

    # Id do botão Enviar
    id_btn_enviar = "//*[@id='submit-btn']"

    # Clicar no botão Enviar
    btn_enviar = navegador.find_element(By.ID, id_btn_enviar)
    btn_enviar.click()

    # Voltar para a lista de favoritos
    navegador.back()