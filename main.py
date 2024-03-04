import re
import time
from multiprocessing import cpu_count
import concurrent.futures
import requests


print("RESULTADOS")
print("cpu: ", cpu_count())
print("----------")

RANGE = range(10000, 11000)
RESULTS = []

URL = ["https://www.homecenter.com.co/homecenter-co/product/"+str(sku) for sku in RANGE]

def get_pages(web_url, time_out):
    """Get the page and add in the response array"""
    response = requests.get(web_url, timeout=time_out)
    content = response.text

    pattern_price = r"\"price\": \"(.*)\""
    pattern_name = r"\"name\": \"(.*)\""
    pattern_sku = r"\"sku\": \"(.*)\""
    prices = re.findall(pattern_price, str(content))
    names = re.findall(pattern_name, str(content))
    sku = re.findall(pattern_sku, str(content))
    if len(prices) > 0:
        RESULTS.append({
            'sku': sku[0], 
            'name': "\'"+names[0]+"\'", 
            'price': prices[0]})

TIME_START = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=cpu_count()-1) as e:
    future_to_url = {e.submit(get_pages, url, 120): url for url in URL}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        data = future.result()

TIME_END = time.time()
print("Time: "+ str(TIME_END - TIME_START))

with open('data.txt', 'w', encoding="utf-8") as f:
    f.write(str(RESULTS))
