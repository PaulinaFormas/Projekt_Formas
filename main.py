async def getData(query):
    print(f'Szukanie: {query}')
    cocolita_url = f'https://www.cocolita.pl/s?q={query}'
    minti_url = f'https://mintishop.pl/search.php?text={query}'
    makeup_url = f'https://makeup.pl/search/?q={query}'

    coco_resp   =   await sessionCoco.get(cocolita_url)
    minti_resp  =  await sessionMinti.get(minti_url)
    makeup_resp =  await sessionMakeup.get(makeup_url)

    await coco_resp.html.arender()
    await minti_resp.html.arender()
    await makeup_resp.html.arender()
    #cocolita
    if (coco_resp is None or coco_resp.html.find('div.no-items')):
        coco_price_raw = "Nie znaleziono"
    else:
        coco_item = coco_resp.html.find('div[data-type="product-list"] h2.product-name a[data-type="product-url"]',first=True).text
        coco_price_raw = coco_resp.html.find('div[data-type="product-list"] div.product-price-container span.discount-price',first=True).text
    #minti
    if(minti_resp is None or minti_resp.html.find('div.noproduct_page')):
        minti_price_raw = "Nie znaleziono"
    else:
        minti_item = minti_resp.html.find('section#search h3 a.product__name',first=True).text      
        minti_price_raw = minti_resp.html.find('section#search strong.price',first=True).text
    #makeup
    if (makeup_resp is None or makeup_resp.html.find('div.search-results strong',first=True).text == 0):
        makeup_price_raw = "Nie znaleziono"
    else:
        makeup_item = makeup_resp.html.find('div.catalog-products div.info-product-wrapper a',first=True).text
        makeup_price_raw = makeup_resp.html.find('div.catalog-products span.price_item',first=True).text
    return ((coco_price_raw,minti_price_raw,makeup_price_raw),(coco_item,minti_item,makeup_item))

def formatData(data):
    rExp = r"\d+(,|.)\d{2}"
    ret = list()
    for i in range(len(data)):
        ret.append(data[i])
        ret[i] = re.sub(r",",".",ret[i])
        ret[i] = re.match(rExp, ret[i])
        if ret[i] is not None :
            ret[i] = ret[i].group(0)
    return ret
    
  

async def main():
    query  = input("Podaj nazwe produktu: ")
    data =  await getData(query)
    prices = formatData(data[0])
    print(data[1])
    print(prices)

from requests_html import AsyncHTMLSession
import nest_asyncio
import asyncio
import re

if asyncio.get_event_loop().is_running():
    nest_asyncio.apply()


sessionCoco = AsyncHTMLSession()
sessionMinti = AsyncHTMLSession()
sessionMakeup = AsyncHTMLSession()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())