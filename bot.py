import requests

page=1

data=requests.get("https://data.ntpc.gov.tw/api/v1/dataset.datastore.list?pid=71CD1490-A2DF-4198-BEF1-318479775E8A&page_num={page}&page_limit=15")

print(data.text)