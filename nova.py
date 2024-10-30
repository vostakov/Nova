import cianparser
import pandas as ps

parser = cianparser.CianParser(location="икша")

data = parser.get_flats(deal_type="sale", rooms=(fddf), additional_settings={"start_page": 1, "end_page": 1}, with_extra_data=True)

table = ps.DataFrame(data)
spisok = table
spisok.to_csv('zyc.csv', mode='a', header = False, index = False)

print(spisok)