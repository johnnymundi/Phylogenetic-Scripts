# para utilizar, é só digitar no prompt: python get_cdsearch_results.py 'nome do output blast'

# utilizo o selenium para acessar o link do cd search e pegar o elemento textarea que corresponde ao box para digitar a sequência de nucleotídeos
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# o time eh utilizado para dar um tempo para a página ser carregada, principalmente naquelas com JS
import time

# abre o navegador Chrome (é preciso colocar a PATH exata do seu computador)
driver = webdriver.Chrome(
    executable_path="C:/Program Files (x86)/chromedriver.exe")
# acessa o link do cd search
driver.get("https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi")
# time.sleep(10)  - pode ser necessário acrescentar essa linha, caso a internet seja instável

# pega o id correspondente ao elemento textarea onde digitamos à sequência
textarea = driver.find_elements_by_tag_name('textarea')[0]
# envia a sequência para o textarea
textarea.send_keys(open(sys.argv[1], "r"))  # arquivo com a sequência

# clica no botão Submit para ver o resultado da busca
button = driver.find_element_by_id('sbmt_newsearch')
button.click()
time.sleep(4)


result = driver.find_element_by_id('div_img_container')
result.screenshot('resultcdsearch.png')

driver.quit()
