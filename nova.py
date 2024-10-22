import cianparser
import pandas as ps
import time

moscow_parser = cianparser.CianParser(location="Москва")
data = []
for i in range(56, 60):
    a = moscow_parser.get_flats(deal_type="sale", rooms=(1, "studio"), additional_settings={"start_page":i, "end_page":i})
    data.extend(a)
    time.sleep(15)

table = ps.DataFrame(data)

columbs = ['author', 'price', 'deal_type', 'location', 'floors_count', 'rooms_count', 'total_meters', 'accommodation_type', 'district', 'street', 'house_number', 'underground', 'residential_complex']
spisok = table[columbs]
spisok.to_csv('cian_parsing.csv', mode='a', header = False, index = False)
print(spisok)