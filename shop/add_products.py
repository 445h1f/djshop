from .models import Product
import json
x = 10
# with open('./shop/sample_prod.json', encoding='utf-8') as r:
#     products = json.load(r)

with open('./shop/sample/flipkart_data.json', encoding='utf-8') as r:
    products = json.load(r)

"""
for prod in products:
    try:
        newProd = Product()
        newProd.title = prod["title"]
        newProd.discount_price = float(prod["price"].replace(',', ''))
        newProd.price = float(prod["original_price"].replace(',', ''))

        # applying 15% discount to all products
        # newProd.discount_price = round(prod["price"]*0.85, 2)

        newProd.category = prod["category"]
        newProd.description = prod["description"]
        newProd.image = prod["images"].split('|')[0].strip()
        # newProd.image = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/660px-No-Image-Placeholder.svg.png?20200912122019"
        newProd.save()
    except Exception as e:
        # print(str(e))
        pass

"""

# Product.objects.all().delete()