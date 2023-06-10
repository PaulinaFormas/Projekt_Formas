import requests
from requests_html import HTMLSession
import re

def getCoco(query):
    query_url = f'https://www.cocolita.pl/s?q={query}'
    sessionCoco = HTMLSession()
    coco_resp   = sessionCoco.get(query_url)
    sessionCoco.close()
    coco_resp.html.render(scrolldown =10, sleep=2)
    try:
        ret = {}
        ret["item"] = coco_resp.html.find('div[data-type="product-list"] ul li h2.product-name a[data-type="product-url"]',first=True).text
        ret["price"] = formatData(coco_resp.html.find('div[data-type="product-list"] ul li div.product-price-container span.discount-price',first=True).text)
        ret["image"] = requests.get(coco_resp.html.find('div[data-type="product-list"] ul li div.product-image img',first = True).attrs["src"]).content
        ret["url"] = coco_resp.html.find('div[data-type="product-list"] ul li div.product-image a.product-hover-opacity',first=True).attrs["href"]
    except:
        return None
    else:
        return ret

def getMinti(query):
    query_url = f'https://mintishop.pl/search.php?text={query}'
    sessionMinti = HTMLSession()
    minti_resp  =   sessionMinti.get(query_url)
    sessionMinti.close()
    minti_resp.html.render(scrolldown =10)
    try:
        ret = {}
        ret["item"] = minti_resp.html.find('section#search h3 a.product__name',first=True).text      
        ret["price"] = formatData(minti_resp.html.find('section#search strong.price',first=True).text)
        ret["image"] = requests.get(minti_resp.html.find('section#search div picture img',first = True).attrs["src"]).content
        ret["url"] = minti_resp.html.find('section#search a.product__icon',first=True).attrs["href"]
    except:
        return None
    else:
        return ret

def getMakeup(query):
    query_url = f'https://makeup.pl/search/?q={query}'
    sessionMakeup = HTMLSession()
    makeup_resp =   sessionMakeup.get(query_url)
    sessionMakeup.close()
    makeup_resp.html.render(scrolldown =10)
    try:
        ret = {}
        ret["item"] = makeup_resp.html.find('div.catalog-products div.info-product-wrapper a',first=True).text
        ret["price"] = formatData(makeup_resp.html.find('div.catalog-products span.price_item',first=True).text)
        ret["image"] = requests.get(makeup_resp.html.find('div.catalog-products li[data-touch-event="product_select"] div.simple-slider-list__link a img',first = True).attrs["data-src"]).content
        ret["url"] = makeup_resp.html.find('div.catalog-products li[data-touch-event="product_select"] div.simple-slider-list__link a',first=True).attrs["href"]
    except:
        return None
    else:
        return ret
    
def formatData(data):
    rExp = r"\d+.\d{2}"
    data = re.sub(r",",".",data)
    data = re.match(rExp, data)
    if data is not None :
        data = data.group(0)
    return data


