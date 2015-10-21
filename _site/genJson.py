import csv
import json
import sys

# Check the arguments
if (len(sys.argv) != 2):
  print("Usage: genJson.py <CSV File>");
  sys.exit(1)


csvfile = open(sys.argv[1])
jsonfile = open('file.json', 'w')

reader = csv.DictReader( csvfile)
jsonfile.write("[\n")
out_str=""
for row in reader:
    str=json.dumps(row,sort_keys=True,indent=4);
    out_str+=str+",\n"

jsonfile.write(out_str[:-2]+"\n]")
