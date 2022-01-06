# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 23:20:32 2021

@author: yagoi
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

url="https://www.binance.com/es/nft/goods/detail?productId=9736557&isProduct=1"


def buy_nft():
    
    
    wait = WebDriverWait(driver, 900)
    
    
    # Se aceptan los términos y condiciones
    terminos_y_condiciones = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' css-1mtehst']")))
    terminos_y_condiciones.click()
    
    
    # Se pulsa el botón de inciar sesion
    inciar_session = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='header_login']")))
    inciar_session.click()
    
    # Se esperan mas de 2 minutos para que Binance deje comprar
    sleep(140)
    
    # Se pulsa el botón de comprar
    comprar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' css-18fem9b']")))
    comprar.click()
    
    
    
    while(True):
        sleep(0.02)
        
        # Se pulsa en confirmar la compra
        cancelar = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-sr9689']/button[2]")))
        cancelar.click()
        
        
        try:
            sleep(0.2)
            # Se pulsa el botón de volver si existe
            volver = driver.find_element_by_xpath("//button[@class=' css-i3fncf']")
            #volver = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' css-i3fncf']")))
            volver.click()
           
            # Se pulsa el botón de comprar
            comprar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' css-18fem9b']")))
            comprar.click()
           
        except:
          print("No hay boton de error")
           
            
        
    
    
    '''
    #CAJAS MISTERIOSAS
    
    # Se aceptan los términos y condiciones
    terminos_y_condiciones = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' css-1mtehst']")))
    terminos_y_condiciones.click()
    
    # Se elige la cantidad de cajas misteriosas // NO FUNCIONAL
    cantidad = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='css-1w6omp2']")))
    cajas = 2
    cantidad.send_keys(cajas)
    
    # Se pulsa el botón de comprar
    comprar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' css-13irzvu']")))
    comprar.click()
    
    # Se pulsa en confirmar la compra
    confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' css-d8znws']")))
    confirmar.click()
    '''
    
    
def main():
    
    # Maximiza el Chrome
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    
    # Se pasa la URL (OpenSea)
    driver.get(url)
    
    # Se llama a la función de navegar
    buy_nft()
    


if __name__ == "__main__":
    main()

