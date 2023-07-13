# utilizo o selenium para acessar o link do cd search e pegar o elemento textarea que corresponde ao box para digitar a sequência de nucleotídeos
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# preciso do BeautifulSoup pra pegar o resultado que o selenium consegue acessar
# o time eh utilizado para dar um tempo para a página com o resultado ser carregada, principalmente naquelas com muito JS
import time

'''
Envia cada sequência de um arquivo fasta para o site ExPASy e salva em um output a tradução de acordo com seu reading frame.
'''


def sequence_list(file):
    # sequences é uma lista que conterá as sequências a serem buscadas no ExPASy
    sequences = []
    tags = []
    i = 0

    for line in file:
        line = line.rstrip()
        i += 1
        if '>' not in line:
            sequences.append(line)
        else:
            tags.append(line)

    print('Quantidade de sequências: ', len(sequences))
    return sequences, tags

# função que joga cada sequência no ExPASy, pega o primeiro resultado da tradução e salva em um arquivo .txt ou .fas


def translation(file1, ORffinder_result):
    output = open(sys.argv[3], 'w')
    contador = 1
    # primeiramente roda a função que irá separar as sequências nucleotídicas de seus títulos
    sequences, tags = sequence_list(file1)
    results_ORF = sequence_list(ORffinder_result)
    results_ORF = results_ORF[0]
    print(results_ORF)
    result = ''

    # abre o navegador Chrome
    driver = webdriver.Chrome(
        executable_path="C:/Program Files (x86)/chromedriver.exe")
    # acessa o link do cd search
    driver.get("https://web.expasy.org/translate/")

    for tag in range(len(sequences)):
        print('O nome da sequência de número {} é: {}\n'.format(contador, tags[tag]))

        # pega o id correspondente ao elemento textarea onde digitamos à sequência
        textarea = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/form/div[1]/textarea")
        # envia a sequência para o textarea
        textarea.send_keys(sequences[tag])  # arquivo com a sequência

        # clica no botão Submit para ver o resultado da busca
        button = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[2]/form/div[3]/input[2]')
        button.click()
        time.sleep(4)

        if results_ORF[tag] == '+1':
            frame = driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/form/div[5]/fieldset[1]/div").text
            print(frame)
        elif results_ORF[tag] == '+2':
            frame = driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/form/div[5]/fieldset[2]/div").text
            print(frame)
        elif results_ORF[tag] == '+3':
            frame = driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/form/div[5]/fieldset[3]/div").text
            print(frame)
        elif results_ORF[tag] == '-1':
            frame = driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/form/div[5]/fieldset[4]/div").text
            print(frame)
        elif results_ORF[tag] == '-2':
            frame = driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/form/div[5]/fieldset[5]/div").text
            print(frame)
        elif results_ORF[tag] == '-3':
            frame = driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/form/div[5]/fieldset[6]/div").text
            print(frame)

        # substitui o '-' por '*' na sequência
        if '-' in frame:
            frame1 = frame.replace('-', '*')
        else:
            frame1 = frame

        result = str(tags[tag]) + '\n' + str(frame1) + '\n'
        print('A sequência traduzida é :\n{}'.format(result))
        output.write(str(result))

        # após pegar o resultado, clica em reset para recomeçar
        reset = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/form/div[3]/input[1]")
        reset.click()

        contador += 1


file = open(sys.argv[1], 'r')
ORFfinder_result = open(sys.argv[2], 'r')
translation(file, ORFfinder_result)
