import csv 

with open("insurance.csv") as insurance_file:
    insurance_data = csv.DictReader(insurance_file)
    for row in insurance_data:
        print(row)