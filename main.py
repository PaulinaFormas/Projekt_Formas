async def getData(query):
    query ="Loreal+True+Match+The+Foundation+Podkład+1N+Neutral+Undertone"
    cocolita_url = f'https://www.cocolita.pl/s?q={query}'
    minti_url = f'https://mintishop.pl/search.php?text={query}'
    makeup_url = f'https://makeup.pl/search/?q={query}'

    coco_resp   =   await s.get(cocolita_url)
    minti_resp  =  await s.get(minti_url)
    makeup_resp =  await s.get(makeup_url)

    await coco_resp.html.arender()
    await minti_resp.html.arender()
    await makeup_resp.html.arender()
    coco_price_raw = coco_resp.html.find('div[data-type="product-list"] div.product-price-container span.discount-price',first=True).text
    minti_price_raw = minti_resp.html.find('section#search strong.price',first=True).text
    makeup_price_raw = makeup_resp.html.find('div.catalog-products span.price_item',first=True).text
    return (coco_price_raw,minti_price_raw,makeup_price_raw)

async def main():
    #query  = input("Podaj nazwe produkut: ")
    #print(query)
    prices =  await getData("Loreal+True+Match+The+Foundation+Podkład+1N+Neutral+Undertone")
    print(prices)

from requests_html import AsyncHTMLSession
import asyncio

import asyncio
if asyncio.get_event_loop().is_running(): # Only patch if needed (i.e. running in Notebook, Spyder, etc)
    import nest_asyncio
    nest_asyncio.apply()


s = AsyncHTMLSession()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())