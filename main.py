from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--headless")

drive = webdriver.Chrome(options=options)
while True:
    music = input('Digite a música:').strip()
    if not music:
        print("Nome da música não informado")
    else:

        drive.get('https://www.letras.mus.br/')

        elem = drive.find_element(By.ID, 'main_suggest')
        elem.clear()
        elem.send_keys(music)
        elem.send_keys(Keys.ENTER)
        print("Busca feita com sucesso")

        elem = drive.find_element(By.XPATH,
                                  '/html/body/div[1]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[5]/div['
                                  '2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a')
        elem.click()
        print("Página encontra com sucesso")

        try:
            letra = drive.find_element(By.CLASS_NAME, 'cnt-letra').text
        except NoSuchElementException:
            letra = drive.find_element(By.CLASS_NAME, 'cnt-trad_l ').text

        print(f'Segue a letra: \n{letra}')
        break
