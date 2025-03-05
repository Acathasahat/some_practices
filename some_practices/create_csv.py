#to creat a csv file and read it
import csv
def dictionary(**kwargs):
    dic = {}
    for key,value in kwargs.items():
        dic[key] = value
    return dic
file_name = input('Create a new CSV file (filename.csv): ')
if not file_name.endswith('.csv'):
    file_name += '.csv'
with open(file_name,'w+',encoding='utf-8',newline='') as f:
    fieldnames = ['Name','Age','City']
    writer = csv.DictWriter(f,fieldnames = fieldnames) #DictWriter()创建了一个对象
    writer.writeheader()
    while True:
        row_d = input('Enter the data in the order of name, age and city: ')
        if row_d.lower() == 'done': break
        try:
            name,age,city=row_d.split(',')
            row_data = dictionary(Name=name.strip(),Age= age.strip(),City=city.strip())
        except ValueError:
            print('Enter the datas in the order of name, age and city. e.g. Alice, 33, New York ')
            continue
        writer.writerow(row_data)
        print(f'\nIf you finished, please enter \'done\'\n')
    f.seek(0)#将文件指针移动到开头的位置
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.seek(0)
    reader= csv.DictReader(f)
    for row in reader:
        print(row['Name'],row['Age'],row['City'])