#Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
#Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions') #ver cuando uso token
driver_path = 'C:\scraping python\chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)
# Inicializamos el navegador
driver.get('https://eltiempo.es')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#term')))\
    .send_keys('Madrid')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'i.icon.icon-search')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      '//*[@id="cityTable"]/div[1]/section/ul[1]/li[2]/h2/a')))\
    .click()



WebDriverWait(driver, 30)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[5]/div[1]/div[4]/div/main/section[4]/section/div/article')))\
    .click()
texto_columnas = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[4]/div/main/section[4]/section/div/article')

texto_columnas2 = texto_columnas.text
print("resultado:", texto_columnas2)
#llega a sacar un elemento falta ver el xpath full de una tabla para usar con pandas
horas = list()
temp = list()
direcc_viento = list()
velocidad_viento=list()
rachas=list()
lluvias=list()
nieves=list()
nubes=list()
tormenta=list()
vacio=list()

for i in range(0, len(texto_columnas2), 10):
    horas.append(texto_columnas2[i])
    temp.append(texto_columnas2[i+1])
    direcc_viento.append(texto_columnas2[i+2])
    velocidad_viento.append(texto_columnas2[i+3])
    rachas.append(texto_columnas2[i+4])
    lluvias.append(texto_columnas2[i+5])
    nieves.append(texto_columnas2[i+6])
    nubes.append(texto_columnas2[i+7])
    tormenta.append(texto_columnas2[i+8])
    vacio.append(texto_columnas2[i+9])


df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'DireccVie': direcc_viento, 'Velocvien': velocidad_viento, 'Rachas': rachas, 'Lluvias': lluvias, 'Nieves': nieves, 'Nubes': nubes, 'Tormenta': tormenta, 'Vacio': vacio})
print(df)
df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()