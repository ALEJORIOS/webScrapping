import re
# from colorama import Fore
import requests

print("RESULTADOS")
print("----------")
for i in range(33190, 33200):
    WEB_URL = "https://www.homecenter.com.co/homecenter-co/product/"+str(i)
    response = requests.get(WEB_URL, timeout=2)
    content = response.text

    PATTERN_PRICE = r"\"price\": (.*),"
    PATTERN_NAME = r"\"name\": \"(.*)\""
    PATTERN_SKU = r"\"sku\": \"(.*)\""
    prices = re.findall(PATTERN_PRICE, str(content))
    names = re.findall(PATTERN_NAME, str(content))
    sku = re.findall(PATTERN_SKU, str(content))
    # print(content)
    if len(prices) > 0:
        print("Precio: "+prices[0])
        print("Nombre: "+names[0])
        print("SKU: "+sku[0])
        print("----------")
