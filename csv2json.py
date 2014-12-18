import csv
import json
import re

with open("data.csv","r") as i:
    csv_data=csv.DictReader(i)

    json_data=[]
    for row in csv_data:
        clean_row={}
        for  rec in row :
            clean_name = "".join([c for c in rec.title() if re.match(r'\w', c)])
            clean_row[clean_name] = row[rec]
        json_data.append(clean_row)

    # print json_data
    with open("data.json","w") as o:
        o.write(json.dumps({"murders": json_data}))
