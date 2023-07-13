# utilizo o selenium para acessar o link do cd search e pegar o elemento textarea que corresponde ao box para digitar a sequência de nucleotídeos
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# o time eh utilizado para dar um tempo para a página com o resultado ser carregada, principalmente naquelas com muito JS
import time


def sequence_list(file):
    # sequences - lista somente com a sequências nucleotídicas
    sequences = []
    # tags - lista somente com o título dado às sequências nucleotídicas
    tags = []
    i = 0
    for line in file:
        line = line.rstrip()
        i += 1
        if '>' not in line:
            sequences.append(line)
        else:
            tags.append(line)

    print("Esse arquivo possui:", len(tags), " sequências nucleotídicas")
    return sequences, tags


# função que jogar cada sequência no ORFfinder, pega o frame de leitura da primeira ORF e salva num arquivo .txt
# além disso, retorna somente uma lista como frame de leitura do primeiro ORF resultante
def orffinder_search(list):
    # o terceiro argumento é o nome do output
    output_aa = open(sys.argv[2], 'w')
    output_nt = open(sys.argv[3], 'w')
    sequences, tags = sequence_list(list)
    # o output para outra função é result_list:
    #result_list = []

    # abre o navegador Chrome
    driver = webdriver.Chrome(
        executable_path="C:/Program Files (x86)/chromedriver.exe")
    # acessa o link do cd search
    driver.get("https://www.ncbi.nlm.nih.gov/orffinder/")

    # loop que vai encontrar a ORF de cada sequência:
    for tag in range(len(sequences)):
        print('sequencia numero:', tag + 1)
        # pega o id correspondente ao elemento textarea onde digitamos à sequência
        textarea = driver.find_elements_by_tag_name('textarea')[0]
        # envia a sequência para o textarea
        textarea.send_keys(sequences[tag])  # arquivo com a sequência

        # clica no botão Submit para ver o resultado da busca
        button = driver.find_element_by_id('button_submit')
        button.click()
        time.sleep(20)  # espera um tempo para aparecer o resultado

        '''
            Implementar depois um método do selenium WebDriverWait para verificar se o length_aa está disponível.
            Desse modo, posso incluir algo do tipo:
            try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "myDynamicElement"))
            )
            finally:
                driver.quit()

            Onde no driver.quit posso tentar dar um reload na página e tentar novamente até dar certo para evitar
            ficar dando tanto erro no ORFfinder...
        '''

        # tamanho do melhor ORF em aminoácidos
        """ length_aa = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[4]/div[4]/div[5]/div[2]/span[1]/span[2]").text

        print("tamanho total de aa:", length_aa)
        # full sequencia de amionácidos da melhor ORF
        best_orf_aa = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[4]/div[4]/div[5]/div[2]/div/form/textarea").get_attribute('value')

        # o loop serve pra pegar somente da metionina pra frente, sem o tag do NCBI
        for letter in range(len(best_orf_aa)):
            if best_orf_aa[letter] == 'M':
                best_orf_aa = best_orf_aa[letter:]
                print(best_orf_aa)
                break """
        # clica no botão pra trocar pra nucleotídeos
        troca = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[4]/div[4]/div[5]/div[2]/span[2]/a")
        troca.click()

        button_nt = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[4]/div[4]/div[5]/div[2]/span[2]/div/div[2]/div[2]")
        button_nt.click()

        # tamanho do melhor ORF em nucleotídeos
        length_nt = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[4]/div[4]/div[5]/div[2]/span[1]/span[2]").text

        print("tamanho total de nt:", length_nt)
        # full sequencia de nucleotideos do melhor ORF

        # o time é para dar o tempo pra trocar o textarea de aa para nt
        time.sleep(5)
        best_orf_nt = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[4]/div[4]/div[5]/div[2]/div/form/textarea").get_attribute('value')

        # loop para pegar o primeiro A ignorando o tag do NCBI
        for letter in range(len(best_orf_nt)):
            if best_orf_nt[letter] == 'A':
                best_orf_nt = best_orf_nt[letter:]
                print(best_orf_nt)
                break

        # salva o resultado do melhor aa em um output
        """ result_aa = str(tags[tag]) + '\n' + best_orf_aa + '*' + '\n'
        output_aa.write(result_aa) """

        # salva o resultado do melhor nt em outro output
        result_nt = str(tags[tag]) + '\n' + best_orf_nt + '\n'
        output_nt.write(result_nt)

        # clica em 'Go back to the submitting page...'
        reset = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[4]/div[4]/div[6]/a")
        reset.click()

    return


# o segundo argumento é o nome do arquivo fasta
fasta_file = open(sys.argv[1], 'r')
orffinder_search(fasta_file)
