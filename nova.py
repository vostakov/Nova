import cianparser
import pandas as ps

moscow_parser = cianparser.CianParser(location="Саратов")
data = moscow_parser.get_flats(deal_type="sale", rooms=(1, "studio"), additional_settings={"start_page":1, "end_page":5})

sorted_price = sorted(data, key=lambda x: x[ 'price'])

table = ps.DataFrame(data)

table.to_csv('cian_parsing.csv', index = False)

print(data)