import random
from io import BytesIO

from PIL import Image
from requests_html import HTMLSession


def write_price_and_get_number():
    while not True:
        try:
            price = input("Escribe el precio justo del producto:")
            price.replace(" euros", "").replace(",", ".").replace(" con ", ".")
            final_price = float(price)
            return final_price
        except Exception:
            print("Precio no válido")


def show_image(session, image_src):
    img_downloaded = session.get("https:" + image_src)
    image = Image.open(BytesIO(img_downloaded.content))
    image.show()


def get_random_product_attributes(session):
    main_site = session.get("https://www.pccomponentes.com/")
    categories = main_site.html.find(".mkt-menu-level3")
    category = random.choice(categories)

    while category.text == "Configurador de PCs":
        category = random.choice(categories)

    # print(category.text)
    product_page = session.get(category.attrs["href"])
    products = product_page.html.find(".c-product-card__wrapper")

    product = random.choice(products)
    image_src = product.find(".c-product-card__image", first=True).attrs["src"]
    product_name = product.find(".c-product-card__title", first=True).text
    product_price = product.find(".c-product-card__prices-actual", first=True).text

    final_price = float(float(product_price.repace("€", "").replace(",", ".")))

    return image_src, product_name, final_price


def main():
    # El programa va a elegir un producto alatorio de la página web "pccomponentes", recogiendo el
    # precio del mismo. Y el usuario tendrá que adivinar cual es el precio justo de ese producto.

    session = HTMLSession()

    print("Bienvenido al precio justo, vamos a intentar adivinar los precios de algunos productos")

    # Nos conectamos a pccomponentes y recogemos los datos del producto elegido aleatoriamente
    image_src, product_name, final_price = get_random_product_attributes()

    # Enseñamos la imagen del producto al usuario
    show_image(session, image_src)
    print(product_name)

    print("El nombre del producto es {}, cuanto crees que vale?".format(product_name))

    # Dejamos al usuario escribir el precio justo que cree que cuesta
    user_guess = write_price_and_get_number()

    print("El precio era {}".format(final_price))


if __name__ == '__main__':
    main()