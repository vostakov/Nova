import cianparser
import pandas as ps
import time
#import random

moscow_parser = cianparser.CianParser(location="Королёв")
data = []
for i in range(25, 30):
    a = moscow_parser.get_flats(deal_type="sale", rooms=(1, "studio", 2, 3, 4, 5), additional_settings={"start_page":i, "end_page":i})
    data.extend(a)
    time.sleep(2)

table = ps.DataFrame(data)

columbs = ['author', 'price', 'deal_type', 'location', 'floors_count', 'rooms_count', 'total_meters', 'accommodation_type', 'district', 'street', 'house_number', 'underground', 'residential_complex']
spisok = table[columbs]
spisok.to_csv('cian_parsing.csv', mode='a', header = False, index = False)
print(spisok)