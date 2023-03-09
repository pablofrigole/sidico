#Librerías
#PARA REVISAR OJOOOO SI EN EL MONTO DE CAPITAL VIENE 0 AL IGUAL QUE EN INTERES Y SOLO VIENE IVA Y TOTAL NO ACTIVAR LAS LINEAS QUE LLENAN CAPITAL E INTERES VER DE ARMAR UN IF
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
import pandas as pd
from datetime import datetime
#define fecha hoy
hoy = datetime.now()
print(hoy)
anio = str(hoy.year)
mes = str(hoy.month)
dia = str(hoy.day)
print(len(dia))
if len(dia) == 1:
    diafinal = str('0' + dia)
else:
    diafinal = dia
if len(mes) == 1:
    mesfinal = str('0' + mes)
else:
    mesfinal = mes

print(diafinal, mesfinal, anio)
#fecha de corrido sacar los últimos dos dígitos del año ver función
ultimodiganio = anio[2:4]
print(ultimodiganio)
fechacorrida = str(diafinal + mesfinal +ultimodiganio)
print(fechacorrida)
#lectura de tabla
tabla = pd.read_csv('Libro1.csv', sep=';')
filas = len(tabla.axes[0])
#inicia el for

for i in range(0,filas):
    #Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    driver_path = 'C:\scripingpython\chromedriver.exe'
    driver = webdriver.Chrome(driver_path, options=options)
    #Definición de funciones para llenar y clickear
    def click_element(xpath, time):
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    def fill_input(name, keys, time):
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, name))).send_keys(keys)
    # Inicializamos el navegador ver si esto puede quedar fuera del for para no loguearse cada vez
    driver.get('https://sidico-web.mendoza.gov.ar/Sidico/servlet/hptrf01')
    # Datos de usuario y contraseña ver de poner en archivos luego
    archivousur = open("usur.txt", mode="r")
    archivopassw = open("passw.txt", mode="r")
    usur = archivousur.read()
    passw = archivopassw.read()
    fill_input('input#W0010vUSUARIO', usur, 5)
    fill_input('input#W0010vPASSWORD', passw, 5)
    driver.find_element_by_name('W0010BUTTON1').click()
    #camino atajo para volante preventivo
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td[1]/div/div/table/tbody/tr[2]/td[2]/table', 30)
    #datos de contexto de presupuesto
    fill_input('input#yui-gen1-field', anio, 5)
    fill_input('input#yui-gen3-field', '1', 5)
    fill_input('input#yui-gen7-field', '15', 5)
    fill_input('input#yui-gen11-field', '01', 5)
    fill_input('input#yui-gen15-field', '115', 5)
    monto_capital = tabla.iloc[i,12]
    monto_interes = tabla.iloc[i,13]
    monto_iva = tabla.iloc[i,14]
    monto_total = tabla.iloc[i,15]
    num_exp_adm = int(tabla.iloc[i,24]) 
    anio_exp_adm = int(tabla.iloc[i,25]) 
    texto_preventivo = tabla.iloc[i,16]
    print(texto_preventivo, monto_capital, monto_interes, monto_iva, monto_total, num_exp_adm, anio_exp_adm)
    #Las funciones de abajo están repetidas porque están arriba
    def click_element(xpath, time):
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    def fill_input(name, keys, time):
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, name))).send_keys(keys)
    #inicia preventivo
    click_element('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input[1]', 30)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/img', 30)
    fill_input('input#PREVGESCRE', 'I96013', 5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#PREVECOCTL')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#PREVECOCTL')))\
        .send_keys('41306')
    #datos particulares del volante
    #variables de cada registro
    fill_input('textarea#vTEXTOCOMPLETO', texto_preventivo, 5)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/img', 30) 
    time.sleep(10)
    #frame del popup que se abre
    iframe = driver.find_element_by_id("gxp0_ifrm")
    driver.switch_to.frame(iframe)
    #abajo es código para actuar sobre el frame
    select = driver.find_element_by_xpath('//*[@id="vSISTEMAPA"]')
    opcion = select.find_elements_by_tag_name("option")
    #con full xpath seleccionar = Select(driver.find_element_by_xpath('/html/body/form/div[1]/div/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select'))
    seleccionar = Select(driver.find_element_by_xpath('//*[@id="vSISTEMAPA"]'))
    seleccionar.select_by_value("G")
    time.sleep(10)
    fill_input('input#vEXPENTNRO', num_exp_adm, 5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vEXPENTANIO')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vEXPENTANIO')))\
        .send_keys(anio_exp_adm)
    click_element('/html/body/form/div[1]/div/table/tbody/tr[5]/td/input[1]', 30)
    #confirma el popup y sale del mismo
    time.sleep(10)
    #confirma el volante preventivo en la cabecera
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table[1]/tbody/tr[3]/td/input[1]', 30) 
    time.sleep(10)
    #buscar el preventivo por el número una vez confirmado para subirlo en impresión
    elem = WebDriverWait(driver, 5)\
    .until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                    'span#DETCOMPROBANTE.Title')))\
    .text
    print(elem)
    num_preventivo = elem[39:44]
    print(num_preventivo)
    #elem es una variable de texto que tiene Preventivo Compras Mayores: 2022- 115- xxx hay que sacar las xxx desde el espacio 40 3 lugares
    #línea 1 de capital
    fill_input('input#vPREVGESGTO', 'I00493', 5)
    fill_input('input#vPREVINSUNRO', '196000028', 5)
    fill_input('input#vPREVINSUSNRO', '1', 5)
    # usar clear porque no llena bien
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVCANLIN')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVCANLIN')))\
        .send_keys('1')
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVPRELIN')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVPRELIN')))\
        .send_keys(monto_capital)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[8]/td/fieldset/table/tbody/tr[4]/td/table/tbody/tr/td[1]/input', 30) 
    time.sleep(10)
    #línea 2 de interes
    fill_input('input#vPREVGESGTO', 'I00493', 5)
    fill_input('input#vPREVINSUNRO', '196000031', 5)
    fill_input('input#vPREVINSUSNRO', '1', 5)
    # agregar para que se ponga en clear
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVCANLIN')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVCANLIN')))\
        .send_keys('1')
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVPRELIN')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVPRELIN')))\
        .send_keys(monto_interes)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[8]/td/fieldset/table/tbody/tr[4]/td/table/tbody/tr/td[1]/input', 30) 
    time.sleep(10)
    #
    #linea 3 iva
    #hay que cambiar la coma por punto para poder evaluar el número ver cómo es el proceso
    letra = monto_iva
    posicion = letra.find(',')
    letra1 = letra[0:posicion]
    letra2= letra[posicion + 1:posicion + 3]
    letranueva = str(letra1 + '.' + letra2)
    print(letra1)
    print(letra2)
    print(letra)
    print(letranueva)
    numero = float(letranueva)
    suma = numero +1
    print(suma)
    
    if numero > 0:
            fill_input('input#vPREVGESGTO', 'I00493', 5)
            fill_input('input#vPREVINSUNRO', '196000026', 5)
            fill_input('input#vPREVINSUSNRO', '0', 5)
            # agregar para que se ponga en clear
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'input#vPREVCANLIN')))\
                .clear()
            time.sleep(5)
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'input#vPREVCANLIN')))\
                .send_keys('1')
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'input#vPREVPRELIN')))\
                .clear()
            time.sleep(5)
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'input#vPREVPRELIN')))\
                .send_keys(monto_iva)
            click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[8]/td/fieldset/table/tbody/tr[4]/td/table/tbody/tr/td[1]/input', 30) 
            time.sleep(10)


    #distribuir el gasto
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/input[4]', 30) 
    #abre un popup ver código para popup
    #para el caso de noviembre el imput es input#PREVNG11 y va el monto total (ver que requiere un clear como en el año)
    #luego se da click en button input#BTN_ENTER
    #luego de cerrar popup va a click en link span#TEXTBLOCK7
    #código para popup iframe
    # se agregó un código que identifique en el mes que estamos y poner input#PREVNG12 (y poner 1 o 12 según el mes)
    # es en la variablexpathmes
    variablexpathmes = str('input#PREVNG'+mes)
    time.sleep(10)
    iframe = driver.find_element_by_id("gxp0_ifrm")
    driver.switch_to.frame(iframe)
    #recordar cambiar PREVNG12 por el mes que corresponda
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        variablexpathmes)))\
        .clear()
    time.sleep(5)
    print(monto_capital)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        variablexpathmes)))\
        .send_keys(monto_total)
    time.sleep(10)
    click_element('/html/body/form/div[1]/div/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input', 30) 
    time.sleep(10)
    #hacer una búsqueda en la página para sacar el número del comprobante preventivo
    #poner el código de búsqueda del número y guardarlo en una variable
    #lo de abajo es click en el link para volver a trabajar con preventivo
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/span/a', 30) 
    time.sleep(10)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVNRO')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vPREVNRO')))\
        .send_keys(num_preventivo)
    time.sleep(10)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[5]/td/input', 30)
    #con la búsqueda poner el número del comprobante guardado en la variable de búsqueda luego hacer el clicj para que suba el prev
    # llenar con el número en el imput#vPREVNRO luego click en botón /html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[5]/td/input
    #poner el valor de la vareiable en el cuadro imput#vPREVNRO (ver si necesita dejar en cero)
    time.sleep(20)
    # cuando se encuentra el preventivo sin detalle se clickea para que se suba al gde en /html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[54]/img
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[54]/img', 30) 
    time.sleep(10)
    #cerrar la ventana con el pdf del preventivo
    #/html/body/div[2]/div[1]/span[2]
    click_element('/html/body/div[2]/div[1]/span[2]', 30) 
    time.sleep(10)
    #hacer click en el lápiz para modificar el definitivo Ojo ver IF si hay IVA para ponerlo en la línea
    #/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/img
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/img', 30) 
    time.sleep(10)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/input[2]', 30) 
    time.sleep(10)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[7]/td/table/tbody/tr/td[2]/table/tbody/tr/td/fieldset/table/tbody/tr[1]/td/table/tbody/tr/td[1]/span/input', 30) 
    time.sleep(10)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[7]/td/table/tbody/tr/td[2]/table/tbody/tr/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td[1]/span/input', 30) 
    time.sleep(10)
    #se abrieron las opciones y hay que llenar los cuadros en este nivel
    #usar lista desplegable
    seleccionar = Select(driver.find_element_by_xpath('//*[@id="vADEFTIPNOR"]'))
    seleccionar.select_by_value("3")
    time.sleep(10)
    #funciona ahora hay que llenar con datos recordar cambiar número de ley de presupuesto OJO que con IF hay una línea más de iva
    fill_input('input#vADEFNRONOR', '9433', 5)
    time.sleep(10)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vADEFAANOR')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vADEFAANOR')))\
        .send_keys('2022')
    time.sleep(10)
    #funciona ahora hay que llenar con num proveedor tesoreria
    fill_input('input#vADEFPROVENRO', '5095', 5)
    # para click en casilla 1 /html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[9]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td/div/table/tbody/tr[1]/td[26]/label/input
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[9]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td/div/table/tbody/tr[1]/td[26]/label/input', 30) 
    time.sleep(10)
    #para click en casilla 2 /html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[9]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td[26]/label/input
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[9]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td[26]/label/input', 30) 
    time.sleep(10)
    #para click en casilla 3 si hay IVA /html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[9]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td[26]/label/input
    if numero > 0:
            click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[9]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td[26]/label/input', 30) 
            time.sleep(10)
    # boton de modificar
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[7]/td/table/tbody/tr/td[2]/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/input', 30) 
    time.sleep(10)
    #pasa a validar cada línea en una pantalla /html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input', 30) 
    time.sleep(30)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input', 30) 
    time.sleep(30)
    #OJO con IF hay que validar la tercer línea de IVA
    if numero > 0:
            click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input', 30) 
            time.sleep(30)
    #pasa a imputación definitiva /html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/input[4]
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/input[4]', 30) 
    time.sleep(30)
    # abre un popup ifram
    time.sleep(10)
    iframe = driver.find_element_by_id("gxp0_ifrm")
    driver.switch_to.frame(iframe)
    fill_input('input#vDEFDEPO', '367', 5)
    time.sleep(30)
    # boton emitir definitivo /html/body/form/div[1]/div/div/table/tbody/tr[7]/td/input[2] darle tiempo abre pdf cerrar
    click_element('/html/body/form/div[1]/div/div/table/tbody/tr[7]/td/input[2]', 10)
    #dejar el tiempo que sigue para que aparezca el pdf del definitivo
    time.sleep(30)
    ####VER DE CERRAR EL PDF Y ARRANCAR CON EL MENU INICIAL Y OP PARA NO VOLVER A LOGUEARSE NO FUNCIONA 
    #click_element('/html/body/div[4]/div[1]/span[2]', 30) 
    ########################################################################################################
    #arrancar con la op###### revisar porque cuando se loguea para arrancar da error parece que en el fecinitivo cierra login
    ##############################
    ### poner el logeo porque no funciona la anterior
    #Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    driver_path = 'C:\scripingpython\chromedriver.exe'
    driver = webdriver.Chrome(driver_path, options=options)
    #Definición de funciones para llenar y clickear
    def click_element(xpath, time):
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    def fill_input(name, keys, time):
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, name))).send_keys(keys)
    # Inicializamos el navegador ver si esto puede quedar fuera del for para no loguearse cada vez
    driver.get('https://sidico-web.mendoza.gov.ar/Sidico/servlet/hptrf01')
    # Datos de usuario y contraseña ver de poner en archivos luego
    fill_input('input#W0010vUSUARIO', usur, 5)
    fill_input('input#W0010vPASSWORD', passw, 5)
    driver.find_element_by_name('W0010BUTTON1').click()
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td[1]/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/div/table/tbody/tr[1]/td[2]', 30)
    #datos de contexto de presupuesto cambiar con el año
    fill_input('input#yui-gen1-field', anio, 5)
    fill_input('input#yui-gen3-field', '1', 5)
    fill_input('input#yui-gen7-field', '15', 5)
    fill_input('input#yui-gen11-field', '01', 5)
    fill_input('input#yui-gen15-field', '115', 5)
    click_element('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input[1]', 30)
    #nueva orden de pago
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/img[2]', 30)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[6]/td/input[1]', 30)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/img', 30)
    time.sleep(30) 
    # abre popup para expediente GDE
    monto_total = tabla.iloc[i,15]
    num_exp_adm = int(tabla.iloc[i,24]) 
    anio_exp_adm = int(tabla.iloc[i,25]) 
    texto_op = tabla.iloc[i,17]
    print(texto_op, monto_total, num_exp_adm, anio_exp_adm)
    def click_element(xpath, time):
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    def fill_input(name, keys, time):
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, name))).send_keys(keys)
    #frame del popup que se abre no lo está encontrando
    iframe = driver.find_element_by_id("gxp0_ifrm")
    driver.switch_to.frame(iframe)
    #abajo es código para actuar sobre el frame
    select = driver.find_element_by_xpath('//*[@id="vSISTEMAPA"]')
    opcion = select.find_elements_by_tag_name("option")
    #con full xpath seleccionar = Select(driver.find_element_by_xpath('/html/body/form/div[1]/div/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select'))
    seleccionar = Select(driver.find_element_by_xpath('//*[@id="vSISTEMAPA"]'))
    seleccionar.select_by_value("G")
    time.sleep(10)
    fill_input('input#vEXPENTNRO', num_exp_adm, 5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vEXPENTANIO')))\
        .clear()
    time.sleep(5)
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vEXPENTANIO')))\
        .send_keys(anio_exp_adm)
    click_element('/html/body/form/div[1]/div/table/tbody/tr[5]/td/input[1]', 30)
    #confirma el popup y sale del mismo
    #empezar a llenar el formulario de la op
    time.sleep(5)
    fill_input('input#OPAGORETII', '78', 10)
    time.sleep(5)
    fill_input('input#OPAGOPROVE', '5095', 10)
    time.sleep(5)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#OPAGOTOTGR')))\
        .clear()
    time.sleep(10)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#OPAGOTOTGR')))\
        .send_keys(monto_total)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#OPADEPO')))\
        .clear()
    time.sleep(10)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#OPADEPO')))\
        .send_keys('367')
    time.sleep(10)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'textarea#vTEXTOCOMPLETO')))\
        .clear()
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'textarea#vTEXTOCOMPLETO')))\
        .send_keys(texto_op)
    time.sleep(10)
    
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input', 30)
    #hay que leer el número de la op ver el objeto que son es ese span#det...
    # acá está el texto para sacar el número /html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/fieldset/legend  
    # confirmar líneas ver archivo de texto para terminar op.txt revisar como queda el span pero luego del numeral estaría bien
    elem = WebDriverWait(driver, 5)\
    .until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                    'span#span_W0024OPAGONRO')))\
    .text
    print(elem)
    num_op = elem[39:44]
    print(num_op)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/div/table/tbody/tr[1]/td[15]/input', 30)
    time.sleep(20)
    # OJO con el IF hay que liquidar también la línea de IVA
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#W0028vCANTLIQ_0001')))\
        .send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT,'1',Keys.TAB)
    time.sleep(20)
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#W0028vCANTLIQ_0002')))\
        .send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT,'1',Keys.TAB)
    time.sleep(20)
    # acá podría ir el IF
    if numero > 0:
            WebDriverWait(driver, 20)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#W0028vCANTLIQ_0003')))\
                .send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT,'1',Keys.TAB)
            time.sleep(20)
            
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#W0028vCANTLIQ_0001')))\
        .send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT,'1',Keys.TAB)
    time.sleep(20)
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#W0028vCANTLIQ_0002')))\
        .send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT,'1',Keys.TAB)
    time.sleep(20)
    # acá podría ir el IF
    if numero > 0:
            WebDriverWait(driver, 20)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#W0028vCANTLIQ_0003')))\
                .send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT,'1',Keys.TAB)
            time.sleep(20)
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#W0028vCANTLIQ_0002')))\
        .send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT,'1',Keys.TAB)
    time.sleep(20)
    # acá podría ir el IF
    if numero > 0:
            WebDriverWait(driver, 20)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#W0028vCANTLIQ_0003')))\
                .send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT,'1',Keys.TAB)
            time.sleep(20)
    #confirma las líneas
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/fieldset/table[2]/tbody/tr/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/fieldset/table/tbody/tr[4]/td[1]/input[1]', 10)
    time.sleep(20)
    #abre el popup de la factura
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[1]/td/table/tbody/tr/td[1]/input[3]', 30)
    #copiar código de ifrm
    time.sleep(10)
    iframe = driver.find_element_by_id("gxp0_ifrm")
    driver.switch_to.frame(iframe)
    click_element('/html/body/form/div[1]/div/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/img', 30)
    fill_input('input#GTOFACCPBT', 'SF', 5)
    time.sleep(10)   
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#GTOFACFEC')))\
        .send_keys(Keys.CLEAR, '1',Keys.TAB)
    time.sleep(20)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#GTOFACIMP')))\
        .clear()    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#GTOFACIMP')))\
        .send_keys(monto_total)
    time.sleep(10)
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'img#IMAGE1')))\
        .send_keys(Keys.TAB)
    time.sleep(20)
    #armar una función fecha con la del día y ponerlo como número sin barras
    #armar un archivo con número de expediente número de autos juz circ y vol prev def y op (confirmation box)
    #cambiar fecha 311222 la que corresponda
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#GTOFACFEC')))\
        .send_keys(fechacorrida)
    time.sleep(20)    
    ##confirma popup
    click_element('/html/body/form/div[1]/div/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/input[1]', 30)
    ## vuelve a la pagina
    click_element('/html/body/form/div[1]/div/table/tbody/tr[6]/td/input', 40)
    time.sleep(20)
    #emite op 
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[1]/td/table/tbody/tr/td[1]/input[6]', 40)
    time.sleep(20)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(20)
    #cerrar pdf
    click_element('/html/body/div[2]/div[1]/span[2]', 30)
    #busca la op (no veo que la busque sólo saca cesión de la última op que figura) llenar con el bucle completo no llena con la función
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vOPAGONRO')))\
        .clear()
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#vOPAGONRO')))\
        .send_keys(num_op)
    time.sleep(30)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr[6]/td[3]/input', 30)
    time.sleep(30)
    #cesión
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[4]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[8]/img', 30)
    time.sleep(30)
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/img', 30)
    fill_input('input#CESIOPROVE', '5548', 5)
    time.sleep(20)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#CESIOIMP')))\
        .clear()
    time.sleep(10)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input#CESIOIMP')))\
        .send_keys(monto_total)
    time.sleep(10)
    #confirma bien
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/fieldset/table/tbody/tr[3]/td/input[1]', 30)
    # imprime la cesión no se guarda
    click_element('/html/body/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[3]/td[1]/input', 30)
    # fin de la cesión de la op
    driver.quit




    




