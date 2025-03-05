#to creat a csv file and read it
import csv
file_name = input('enter a new CSV file (filename.csv): ')
if not file_name.endswith('.csv'):
    file_name += '.csv'
with open(file_name,'r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'],row['Age'],row['City'])