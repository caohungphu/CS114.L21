# Source: https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json

import csv
import json

csvfile = open('Test_Sarcasm_Detection_Full.csv', 'r', encoding="UTF-8")
jsonfile = open('Test_Sarcasm_Detection_Full.json', 'w', encoding="UTF-8")


reader = csv.DictReader(csvfile)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')