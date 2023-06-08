import requests
from requests_html import HTMLSession
import re

def getCoco(query):
    cocolita_url = f'https://www.cocolita.pl/s?q={query}'
    sessionCoco = HTMLSession()
    coco_resp   = sessionCoco.get(cocolita_url)
    coco_resp.html.render(scrolldown =10, sleep=2)

    if (coco_resp is None or coco_resp.html.find('div.no-items')):
        return None
    else:
        coco_item = coco_resp.html.find('div[data-type="product-list"] ul li h2.product-name a[data-type="product-url"]',first=True).text
        coco_price_raw = coco_resp.html.find('div[data-type="product-list"] ul li div.product-price-container span.discount-price',first=True).text
        coco_image = requests.get(coco_resp.html.find('div[data-type="product-list"] ul li div.product-image img',first = True).attrs["src"]).content
        return coco_item, formatData(coco_price_raw), coco_image

def getMinti(query):
    minti_url = f'https://mintishop.pl/search.php?text={query}'
    sessionMinti = HTMLSession()
    minti_resp  =   sessionMinti.get(minti_url)
    minti_resp.html.render(scrolldown =10)
    if(minti_resp is None or minti_resp.html.find('div.noproduct_page')):
        return None
    else:
        minti_item = minti_resp.html.find('section#search h3 a.product__name',first=True).text      
        minti_price_raw = minti_resp.html.find('section#search strong.price',first=True).text
        minti_image = requests.get(minti_resp.html.find('section#search div picture img',first = True).attrs["src"]).content
        return minti_item, formatData(minti_price_raw), minti_image

def getMakeup(query):
    makeup_url = f'https://makeup.pl/search/?q={query}'
    sessionMakeup = HTMLSession()
    makeup_resp =   sessionMakeup.get(makeup_url)
    makeup_resp.html.render( scrolldown =10)
    if (makeup_resp is None or makeup_resp.html.find('div.search-results strong',first=True).text == 0):
        return None
    else:
        makeup_item = makeup_resp.html.find('div.catalog-products div.info-product-wrapper a',first=True).text
        makeup_price_raw = makeup_resp.html.find('div.catalog-products span.price_item',first=True).text
        makeup_image = requests.get(makeup_resp.html.find('div.catalog-products li[data-touch-event="product_select"] div.simple-slider-list__link a img',first = True).attrs["data-src"]).content
        return makeup_item, formatData(makeup_price_raw), makeup_image
    
def formatData(data):
    rExp = r"\d+.\d{2}"
    data = re.sub(r",",".",data)
    data = re.match(rExp, data)
    if data is not None :
        data = data.group(0)
    return data


