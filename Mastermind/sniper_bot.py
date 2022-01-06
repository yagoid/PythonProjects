from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://www.pccomponentes.com/gigabyte-geforce-gtx-1050ti-d5-4gb-gddr5"
url_coolmod = "https://www.coolmod.com/msi-geforce-rtx-3090-suprim-x-24gb-gddr6x-tarjeta-grafica-precio"


def buy_product():
    driver = webdriver.Firefox()
    driver.get(url_coolmod)
    driver.find_element_by_class_name("confirm").click()
    driver.find_element_by_class_name("accept").click()
    sleep(2)
    driver.find_element_by_class_name("button-buy").click()
    sleep(1)
    driver.find_element_by_class_name("confirm").click()
    sleep(2)
    driver.find_element_by_class_name("button-buy").click()

    is_form_loaded = False
    form = None

    while not is_form_loaded:
        try:
            form = driver.find_element_by_class_name("login100-form")
            is_form_loaded = True
        except NoSuchElementException:
            print("Nombre de la clase del boton inexistente :(")

    sleep(1)
    email = form.find_element_by_name("jform[email]")
    password = form.find_element_by_name("jform[password]")

    email.send_keys("yago@gmail.com")
    password.send_keys("password")


def check_stock(session):
    # Pccomponentes
    '''
    while True:
        product = session.get(url)
        buy_zone = product.html.find("#buy-buttons-section")
        if len(buy_zone) > 0:
            print("HAY STOCK!!!")
            break
        else:
            print("No hay stock :(")
        sleep(30)
    '''
    # Coolmod
    while True:
        product_page = session.get(url_coolmod)
        found = product_page.html.find("#main-buy")
        if len(found) > 0:
            print("HAY STOCK!!!")
            break
        else:
            print("No hay stock :(")
        sleep(30)


def main():
    session = HTMLSession()
    # Comprobamos si hay stock de la gráfica
    check_stock(session)

    # Hacemos los clicks y rellenamos los datos para comprar la gráfica
    buy_product()


if __name__ == "__main__":
    main()