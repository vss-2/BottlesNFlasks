import os, time
from selenium import webdriver

# Baixar geckodriver e colocar no mesmo repositório (https://github.com/mozilla/geckodriver/releases)
profile = webdriver.Firefox(executable_path=str(os.getcwd()+'/geckodriver'))
# Source: https://stackoverflow.com/questions/18439851/how-can-i-download-a-file-on-a-click-event-using-selenium

with open('output_texto_filter.txt') as links_file:
        links = links_file.readlines()
        for link in links:
                profile.get(link)
                profile.find_element_by_xpath('/html/body/div[4]/main/article[1]/div/div/div[2]/div').click()
                # Caso eu encontre como selecionar com botão direito e salvar arquivo
                
                time.sleep(10)
                # Jeito manual de fazer o descrito acima
