from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
car_info_list = []
edf = pd.DataFrame()
filename = 'cars'
















def save_data(filename, data):
    f = open(fr'C:\Users\abhi\Desktop\{filename}.json', 'w')
    json.dump(data, f, indent=2)
def convert_image(v):
    try:
        return fr'https://fastly-production.24c.in/{v["url"]}'
    except:
        return ''
for i in range(1, 6):
    for j in range(1, 10):
        url = f'https://api-sell24.cars24.team/buy-used-car?sort=P&serveWarrantyCount=false&gaId=1656381752.1658676791&page={j}&storeCityId={i}&pinId=110001'

        response = requests.get(url)

        data = response.json()['data']['content']
        save_data(filename, data)
        print(edf)
        df = pd.read_json(fr'C:\Users\abhi\Desktop\{filename}.json')
        edf = pd.concat([edf, df])
edf['mainImage'] = edf['mainImage'].apply(convert_image)
edf.to_csv(fr'C:\Users\abhi\Desktop\{filename}.csv')
print(edf)
'''get car data'''