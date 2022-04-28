import json
import pandas as pd

with open('./data/data_transport_line.json', 'r', encoding='utf-8') as f:
  rawDataTransportLine = json.load(f)

with open('./data/data_transport_station.json', 'r', encoding='utf-8') as f:
  rawDataStation = json.load(f)

for i in rawDataStation:
  i.pop('subdistrictId')

modStation = rawDataStation

for i in modStation:
  for j in rawDataTransportLine:
    if i['transportationId'] == j['id']:
      i['lineName'] = j['name']
      i['lineNameEng'] = j['nameEng']
      i['lineColorHex'] = j['lineColorHex']
      i['lineServiceName'] = j['service']

for i in modStation:
  i.pop('transportationId')

with open('dist/data.json', 'w', encoding='utf-8') as f:
  json.dump(modStation, f, ensure_ascii=False, indent=4)

modStationDf = pd.DataFrame(modStation)

modStationDf.index += 1

modStationDf.to_csv('dist/data.csv', index=True)