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
options.add_argument('--disable-extensions')
driver_path = 'C:\scraping python\chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)
# Inicializamos el navegador
driver.get('https://sidico-web.mendoza.gov.ar/Sidico/servlet/hptrf01')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#W0010vUSUARIO')))\
    .send_keys('O115FRIGOL')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#W0010vPASSWORD')))\
    .send_keys('1Nc414ne3v')

driver.find_element_by_name('W0010BUTTON1').click()
WebDriverWait(driver, 30)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td[1]/div/div/table/tbody/tr[2]/td[2]/table')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#yui-gen1-field')))\
    .send_keys('2022')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#yui-gen3-field')))\
    .send_keys('1')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#yui-gen7-field')))\
    .send_keys('15')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#yui-gen11-field')))\
    .send_keys('01')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#yui-gen15-field')))\
    .send_keys('115')
WebDriverWait(driver, 30)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input[1]')))\
    .click()


WebDriverWait(driver, 30)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/img')))\
    .click()

WebDriverWait(driver, 30)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/img')))\
    .click()
time.sleep(10)

#hasta acá funciona


WebDriverWait(driver, 30)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/form/div[1]/div/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td[1]/a')))\
    .click()




#driver.find_element_by_xpath('/html/body/form/div[1]/div/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td[1]/a/img').click()

#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                      'input#vCGTOACUGESTCRE')))\
#    .send_keys('I96013')
#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                      'input#vCGTOACUECONRO')))\
#    .send_keys('41306')


time.sleep(10)
#driver.find_element_by_xpath('//*[@id="INSERT"]').click()

#driver.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/img').click()
#driver.find_element_by_name('img#vLINKSELECTION_0006').click()
#driver.find_element_by_name('img#IMAGEUPDEXP').click()
#código para select

#select = driver.find_element_by_xpath('//*[@id="vSISTEMAPA"]')
#option = select.find_element_by_tag_name("G")
#option.click()
#WebDriverWait(driver, 30)\
#    .until(EC.element_to_be_clickable((By.XPATH,
#                                      '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input[1]')))\
#    .click()

#WebDriverWait(driver, 30)\
#    .until(EC.element_to_be_clickable((By.XPATH,
#                                      '/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/img')))\
#    .click()
#WebDriverWait(driver, 5)\

#WebDriverWait(driver, 30)\
#    .until(EC.element_to_be_clickable((By.XPATH,
#                                      '//*[@id="vLINKSELECTION_0006"]')))\
#    .click()
#WebDriverWait(driver, 5)\



# acá poner el código de word para select ver en el notpad lo del xpath y las opciones




#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                      'input#uEXPENTNRO')))\
#    .send_keys('926674')
#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                      'input#vEXPENTANIO')))\
#    .send_keys('2021')
#WebDriverWait(driver, 30)\
#    .until(EC.element_to_be_clickable((By.XPATH,
#                                      '/html/body/form/div[1]/div/table/tbody/tr[5]/td/input[1]')))\
#    .click()
#

#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                      'input#term')))\
#    .send_keys('Madrid')
#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                      'i.icon.icon-search')))\
#    .click()
#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                      'span.item-name')))\
#    .click()



#WebDriverWait(driver, 30)\
#    .until(EC.element_to_be_clickable((By.XPATH,
#                                      '/html/body/div[5]/div[1]/div[4]/div/main/section[5]/section/div/article/section[1]/ul/li[2]/h2/a ')))\
#    .click()
#texto_columnas = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[4]/div/main/section[2]/section/article/div[2]/section/div[2]/p[2]')

#texto_columnas = texto_columnas.text
#print("resultado:", texto_columnas)
#llega a sacar un elemento falta ver el xpath full de una tabla para usar con pandas
#horas = list()
#temp = list()
#direcc_viento = list()
#velocidad_viento=list()
#rachas=list()
#lluvias=list()
#nieves=list()
#nubes=list()
#tormenta=list()
#vacio=list()

#for i in range(0, len(texto_columnas), 10):
#    horas.append(texto_columnas[i])
#    temp.append(texto_columnas[i+1])
#    direcc_viento.append(texto_columnas[i+2])
#    velocidad_viento.append(texto_columnas[i+3])
#    rachas.append(texto_columnas[i+4])
#    lluvias.append(texto_columnas[i+5])
#    nieves.append(texto_columnas[i+6])
#    nubes.append(texto_columnas[i+7])
#    tormenta.append(texto_columnas[i+8])
#    vacio.append(texto_columnas[i+9])


#df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'DireccVie': direcc_viento, 'Velocvien': velocidad_viento, 'Rachas': rachas, 'Lluvias': lluvias, 'Nieves': nieves, 'Nubes': nubes, 'Tormenta': tormenta, 'Vacio': vacio})
#print(df)
#df.to_csv('tiempo_hoy.csv', index=False)

#driver.quit()