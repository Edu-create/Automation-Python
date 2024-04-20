from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

# Aguardar o carregamento da página
wait = WebDriverWait(navegador, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]')))

# Xpath do campo email
xpath_campo_email = '//*[@id="i0116"]'

# Seu email
seu_email = "eduardo.brandao@estacio.br"

# Preencher o campo email
campo_email = navegador.find_element(By.XPATH, xpath_campo_email)
campo_email.clear()
campo_email.send_keys(seu_email)

# Xpath do botão Avançar
xpath_btn_avancar = '//*[@id="idSIButton9"]'


# Clicar no botão Avançar
btn_avancar = navegador.find_element(By.XPATH, xpath_btn_avancar)
btn_avancar.click()

# Aguardar o carregamento da página
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='i0118']")))

# Xpath do campo Pass
xpath_campo_pass = "//*[@id='i0118']"

# Seu apelido
campo_senha = "Esfera@0223"

# Preencher o campo Pass
campo_pass1 = navegador.find_element(By.XPATH, xpath_campo_pass)
campo_pass1.clear()
campo_pass1.send_keys(campo_senha)

# Xpath do botão Avançar
xpath_campo_pass = '//*[@id="idSIButton9"]'

# Clicar no botão Entrar (mesmo XPath do botão Avançar)
btn_entrar = navegador.find_element(By.XPATH, xpath_campo_pass)
btn_entrar.click()

# Aguardar o carregamento da página após o login
wait.until(EC.title_is("Portal do Aluno - Yduqs"))  # Substitua por título da página após login

# Xpath do botão Favoritos
xpath_btn_favoritos = "/html/body/div/section/header/div/nav/div[1]/div/div/div/ul/li[4]"

# Clicar no botão Favoritos
btn_favoritos = navegador.find_element(By.XPATH, xpath_btn_favoritos)
btn_favoritos.click()

def preencher_e_enviar_formulario(navegador):
    # Id do campo Descrição
    id_campo_descricao = "//*[@id='sp_formfield_descricao']"

    # Texto para a descrição
    texto_descricao = "Suporte de laboratório."

    # Preencher o campo Descrição
    campo_descricao = navegador.find_element(By.ID, id_campo_descricao)
    campo_descricao.clear()
    campo_descricao.send_keys(texto_descricao)

# Repetir o processo 5 vezes
for _ in range(5):
    # Xpath da solicitação
    xpath_solicitacao = "//*[@id='favorite_card_f82c61861bcd2150ff94404be54bcbf3']"

    # Clicar na solicitação
    solicitacao = navegador.find_element(By.XPATH, xpath_solicitacao)
    solicitacao.click()

    # Preencher e enviar o formulário
    preencher_e_enviar_formulario(navegador)

    # Voltar para a lista de favoritos
    navegador.back()

