from requests_html import HTMLSession

s = HTMLSession()
query = 'Loreal+True+Match+The+Foundation+Podkład+1N'
cocolita_url = f'https://www.cocolita.pl/s?q={query}'
minti_url = f'https://mintishop.pl/search.php?text={query}'
makeup_url = f'https://makeup.pl/search/?q={query}'
coco_resp   =   s.get(cocolita_url)
coco_resp.html.render()

minit_resp  = s.get(minti_url)
makeup_resp = s.get(makeup_url)
print(coco_resp.html.find('div[data-type="product-list"] div.product-price-container span.discount-price',first=True).text)