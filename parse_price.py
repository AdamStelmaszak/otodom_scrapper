def parse_price_for_apartment(price):
    return float(price.replace(u'\xa0', '').replace(',','.').replace('zł',''))

def parse_price_per_meter(price):
    return float(price.replace(u'\xa0', '').replace(',','.').replace('zł/m²',''))


