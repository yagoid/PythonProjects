# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:32:59 2021

@author: yagoi
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

url="https://opensea.io/"


def get_data():
    
    sleep(4)
    
    nfts = driver.find_element_by_xpath("//div[@role='grid']")
    nfts = nfts.text
    
    #print("\n", nfts)
    
    nft_propieties = nfts.split('\n')
    #print("\n", nft_propieties, "\n")
    
    # Se filtra la información para conseguir los datos que se quieren
    cont = 0
    for nft_property in nft_propieties:
        
        if nft_property == 'Price' or nft_property == 'favorite_border' or nft_property == 'play_arrow':
            nft_propieties.pop(cont)
            
        if nft_property == 'Last' or nft_property == 'timelapse' or nft_property == 'Offer for' or nft_property == 'a day left':
            nft_propieties.remove(nft_property)
            nft_propieties.pop(cont)
            
        cont = cont+1
        
        
    for nft_property in nft_propieties:
        
        if nft_property == 'favorite_border' or nft_property == 'Buy now':
            nft_propieties.remove(nft_property)
            
            
    print("\n", nft_propieties, "\n")
    
    autores = list()
    titulo = list()
    precio_eth = list()
    likes = list()
    
    for i in range(0, len(nft_propieties), 4):
        autores.append(nft_propieties[i])
        titulo.append(nft_propieties[i+1])
        precio_eth.append(nft_propieties[i+2])
        likes.append(nft_propieties[i+3])
        
    
    df = pd.DataFrame({'Autores':autores, 'Titulo':titulo, 'Precio_eth':precio_eth, 'Likes':likes})
    
    print(df)
    df.to_csv('nfts.csv', index=False)
    


def interact_with_nft():
    
    # Se pulsa sobre el menu
    menu = driver.find_element_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq NavItem--main ']")
    menu.click()
    
    sleep(2)

    # Se pulsa en el filtro de "Buy Now"
    buy_now = driver.find_element_by_xpath("//div[@class='Panel--isContentPadded FeaturedFilter--items']/button[1]")
    buy_now.click()
    
    sleep(1)
    
    # Se pulsa el desplegable de elegir la moneda
    menu_price = driver.find_element_by_xpath("//div[@class='Inputreact__StyledContainer-sc-3dr67n-0 iAeYiQ Selectreact__SelectInput-sc-1shssly-0 cJLIjY']")
    menu_price.click()
    
    sleep(1)
    
    # Se pulsa en la moneda ETH
    menu_price = driver.find_element_by_xpath("//ul[@class='Blockreact__Block-sc-1xf18x6-0 Listreact__List-sc-6eey6c-0 Listreact__FramedList-sc-6eey6c-1 dBFmez iPBORQ cDhIsv']/li[2]/button")
    menu_price.click()
    
    sleep(1)
    
    # Se elige escribe el precio mínimo
    min_price = driver.find_element_by_xpath("//input[@class='browser-default Input--input']")
    min = "1"
    min_price.send_keys(min)
    
    # Se elige escribe el precio máximo
    max_price = driver.find_element_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 SpaceBetweenreact__SpaceBetween-sc-jjxyhg-0 karjuF jYqxGr gJwgfT']/div[3]/section/div/div/input")
    max = 50
    max_price.send_keys(max)
    
    # Se pulsa el boton aplicar para confirmar el precio
    apply = driver.find_element_by_xpath("//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 kmCSYg hJoTEY']")
    apply.click()
    
    
def main():
    
    # Maximiza el Chrome
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    
    # Se pasa la URL (OpenSea)
    driver.get(url)
    
    # Se llama a la función de navegar
    interact_with_nft()
    
    # Se llama a la función de recoger información
    get_data()


if __name__ == "__main__":
    main()