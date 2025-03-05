#to creat a csv file and read it
import csv
file_name = input('Create a new CSV file (filename.csv): ')
if not file_name.endswith('.csv'):
    file_name += '.csv'
with open(file_name,'w',encoding='utf-8',newline='') as f:
    fieldnames = ['Name','Age','City']
    writer = csv.DictWriter(f,fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'Name':'Alice','Age':'30','City':'New York'})