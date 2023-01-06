from requests_html import HTMLSession

s = HTMLSession()

query = 'Delhi'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User-Agent': ''})

temp = r.html.find('span#wob_tm', first=True).text

unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text

desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print(query, temp, unit, desc)
