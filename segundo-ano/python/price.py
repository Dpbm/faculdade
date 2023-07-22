import pandas as pd
import matplotlib.pyplot as plt 
"""
DATA

https://www.mercadolivre.com.br/notebook-acer-aspire-3-a314-35-pure-silver-14-intel-celeron-n4500-4gb-de-ram-128gb-ssd-intel-uhd-graphics-jasper-lake-16-eu-1920x1080px-windows-11-home/p/MLB19309449?pdp_filters=deal:MLB779362-1#searchVariation=MLB19309449&position=2&search_layout=grid&type=product&tracking_id=eff0e4d0-f559-4da2-a646-6473f2c3e482&c_id=/home/promotions-recommendations/element&c_element_order=2&c_uid=d5144a55-0060-4356-8d4c-09299674b019

price: 1789R$
weight: 1.62Kg


https://www.mercadolivre.com.br/notebook-samsung-book-celeron-4gb-256gb-ssd-156-w11/p/MLB19692109#reco_item_pos=3&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=bb2fe8ff-8229-497c-a70b-427a7aa70a40&c_id=/home/navigation-recommendations/element&c_element_order=4&c_uid=f7713b1d-2833-40d0-9f8c-327e9342c408

price: 2157.54R$
weight: 1.8Kg

https://www.mercadolivre.com.br/disco-solido-interno-kingston-sa400s37480g-480gb-preto/p/MLB17978326#reco_item_pos=0&reco_backend=machinalis-pdp-domains&reco_backend_type=low_level&reco_client=pdp-other-domain&reco_id=203cc7ff-307e-4762-9b63-cf0fccaf82e0

price: 159R$
weight: 0.04Kg

"""

notebooks = {
        "products": ["Notebook Acer", "Notebook Samsung"],
        "prices":[1789, 2157.54],
        "weights":[1.62, 1.8]
}

others = {
        "products":["SSD Kingston"],
        "prices":[159],
        "weights":[0.04]
        }

data_dict = {
    "products": [*notebooks["products"], *others["products"]],
    "prices": [*notebooks["prices"], *others["prices"]],
    "weights": [*notebooks["weights"], *others["weights"]]
}

data = pd.DataFrame(data_dict)
print(data)

notebooks_data = pd.DataFrame(notebooks)
others_data = pd.DataFrame(others)

plt.scatter(notebooks_data["prices"], notebooks_data["weights"], color="red")
plt.scatter(others_data["prices"], others_data["weights"], color="blue")
plt.show()
