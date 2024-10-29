import cianparser
import pandas as ps

parser = cianparser.CianParser(location="икша")

data = parser.get_flats(deal_type="sale", rooms=(3, 4, 5), additional_settings={"start_page": 41, "end_page": 43}, with_extra_data=True)

table = ps.DataFrame(data)
spisok = table
spisok.to_csv('zxc.csv', mode='a', header = False, index = False)

print(spisok)