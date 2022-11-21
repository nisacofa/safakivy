import requests
import bs4
def web_scra():
    pagina = requests.get(
        "https://www.courir.es/es/c/zapatos/sneakers/marca/jordan+nike/dunk+jordan/?pmin=85.00&pmax=240.00&prefn1=size&prefv1=38%7C38%202%2F3%7C38%2C5%7C39%7C39%201%2F3%7C39%2C5%7C40%7C40%202%2F3%7C40%2C5%7C41%7C41%201%2F3%7C41%2C5%7C42%7C42%202%2F3%7C42%2C5%7C43%7C43%201%2F3%7C43%2C5%7C44%7C44%2C5%7C45%7C45%201%2F3%7C45%2C5%7C46&sz=84")
    pagina2 = requests.get(
        "https://www.courir.es/es/c/zapatos/sneakers/marca/jordan+nike/dunk+jordan/?pmin=85.00&pmax=240.00&start=60&sz=24&format=page-element&prefn1=size&prefv1=38%7C38%202%2F3%7C38%2C5%7C39%7C39%201%2F3%7C39%2C5%7C40%7C40%202%2F3%7C40%2C5%7C41%7C41%201%2F3%7C41%2C5%7C42%7C42%202%2F3%7C42%2C5%7C43%7C43%201%2F3%7C43%2C5%7C44%7C44%2C5%7C45%7C45%201%2F3%7C45%2C5%7C46")

    soup = bs4.BeautifulSoup(pagina.content,"html.parser")
    soup2 = bs4.BeautifulSoup(pagina2.content, "html.parser")

    zapatos = soup.find_all("div", {"class": "product__tile js-product-tile"})
    zapatos2 = soup2.find_all("li", {"class": "grid-tile grid-tile__quickbuy js-grid-tile__quickbuy"})

    diccionario = {
        "marca": None,
        "modelo": None,
        "precio": None,
        "genero": None
    }

    lista_zapatos = []

    for zapatilla in zapatos:
        dic_zapato = diccionario.copy()
        if not zapatilla.find_all("span", {"class": "product-tags-item js--promotion-tag"}):
            marca = zapatilla.find("span", {"class": "product__name__brand js-product-name_brand"}).text
            modelo = zapatilla.find("span", {"class": "product__name__product js-product-name_product"}).text
            precio = zapatilla.find("span",
                                    {"class": "product__price__sales-price js-product__price__sales-price"}).text
            genero = zapatilla.find("span", {"itemprop": "suggestedGender"}).text
            dic_zapato["marca"] = marca
            dic_zapato["modelo"] = modelo
            dic_zapato["precio"] = precio
            dic_zapato["genero"] = genero
            if "JORDAN 11" in dic_zapato["modelo"]:
                continue
            if "DUNK LOW" in dic_zapato["modelo"] or "JORDAN 1" in dic_zapato["modelo"]:
                lista_zapatos.append(dic_zapato)



    for zapatillas in zapatos2:
        dic_zapato = diccionario.copy()
        marca = zapatillas.find("span", {"class": "product__name__brand js-product-name_brand"}).text
        modelo = zapatillas.find("span", {"class": "product__name__product js-product-name_product"}).text
        precio = zapatillas.find("span", {"class": "product__price__sales-price js-product__price__sales-price"}).text
        genero = zapatillas.find("span", {"itemprop": "suggestedGender"}).text
        dic_zapato["marca"] = marca
        dic_zapato["modelo"] = modelo
        dic_zapato["precio"] = precio
        dic_zapato["genero"] = genero
        if "JORDAN 11" in dic_zapato["modelo"]:
            continue
        if "DUNK LOW" in dic_zapato["modelo"] or "JORDAN 1" in dic_zapato["modelo"]:
            lista_zapatos.append(dic_zapato)
    return lista_zapatos
web_scra()