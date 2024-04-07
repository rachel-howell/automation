from woocommerce import API

wcapi = API(
    # url="http://webstore.local/wp-json/wc/v3/products",
    url="http://webstore.local/",
    consumer_key="ck_b238c7e95261b133cd569019c54ea1bbb7f23965",
    consumer_secret="cs_84e3a49d9abfc02e2d75602d41915902f272efb5",
    version="wc/v3"
)

r = wcapi.get("orders")

import pprint
pprint.pprint(r.json())
