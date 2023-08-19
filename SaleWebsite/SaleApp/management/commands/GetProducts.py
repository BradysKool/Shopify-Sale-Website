import requests
import pandas as pd

def getProducts():

    brandInfo = [
        ['allbirds','.com'],
        ['stix','.golf'],
        # ['tenthousand','.cc'],
        ['goruck','.com'],
        ['hukgear','.com']
                ]

    productList = []


    for brand in brandInfo:
        for i in range(50):
            data = requests.get('https://' + brand[0] + brand[1] + '/products.json?page=' + str(i)).json()
            if data['products']:
                for item in data['products']:
                    used = False
                    name = item['title']
                    url = 'https://' + brand[0] + brand[1] + '/products/' + str(item['handle'])
                    handel = item['handle']
                    for variant in item['variants']:
                        msrp =  variant['compare_at_price']
                        salePrice = variant['price']
                        if msrp is not None and msrp != "0.00":
                            for product in productList:
                                if name == product['Name']:
                                    used=True
                            percentOnSale = ((float(msrp)-float(salePrice))/float(msrp))*100
                            product = {
                                'Brand':brand[0],
                                'Name':name,
                                'Url': url,
                                'Handle':handel,
                                'MSRP': msrp,
                                "Sale Price": salePrice,
                                'On Sale Percent':percentOnSale
                            }
                            if used == False:
                                productList.append(product)
    return productList

productList = getProducts()

df = pd.DataFrame(productList)
df.to_csv("C:\\Users\\brady\\OneDrive\Desktop\\Shopify sale website 2.0\\SaleWebsite\\SaleApp\\management\\commands\\Products.csv")
