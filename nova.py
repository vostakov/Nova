import cianparser
import pandas as ps

parser = cianparser.CianParser(location="икша")

data = parser.get_flats(deal_type="sale", rooms=(1, 2), additional_settings={"start_page": 12, "end_page": 13}, with_extra_data=True)

table = ps.DataFrame(data)
spisok = table
spisok.to_csv('zxc.csv', mode='a', header = False, index = False)

print(spisok)