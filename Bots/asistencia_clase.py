# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:49:57 2021

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

url="https://campus.europaeducationgroup.es/courses/3723"


def checkear_asistencia():
    
    
    wait = WebDriverWait(driver, 900)
    
    
    # Se pone el usuario
    usuario = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='pseudonym_session[unique_id]']")))
    user = "21836404"
    usuario.send_keys(user)
    
    
    # Se pone la contrasenia
    contrasenia = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='pseudonym_session[password]']")))
    password = "08344346"
    contrasenia.send_keys(password)
    
    # Se pulsa el botón de inciar sesion
    iniciar_sesion = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='Button Button--login']")))
    iniciar_sesion.click()
    
    
    # Se pulsa el botón de qwickly_attendance
    qwickly_attendance = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='context_external_tool_365']")))
    qwickly_attendance.click()
    
    '''
    sleep(2)
    # Se pulsa el botón de autorizar
    autorizar = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='Button Button--primary Button--block']")))
    autorizar.click()
    '''
    
    sleep(5)
    
    i = 0
    
    while(True):
        
        url2 = "https://uk.qwickly.tools/attendance/takerecord/?request_lms=canvas&id=3723&domain=campus.europaeducationgroup.es&initial_request=%27initial%27&initial_user_id=11207"
        driver.get(url2)
        
        sleep(5)
        
        try:
            # Se pulsa el botón de check_in
            check_in = driver.find_element_by_xpath("//input[@id='student_check_in']")
            check_in.click()
            
            print("Asistencia checkeada!")
            break
           
        except:
          print("No está el botón check_in")
          #print(driver.current_url)
          
          i = i+1
          print(i)
          
          sleep(55)
          
    
    
def main():
    
    # Maximiza el Chrome
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    
    # Se pasa la URL (OpenSea)
    driver.get(url)
    
    # Se llama a la función de navegar
    checkear_asistencia()
    


if __name__ == "__main__":
    main()