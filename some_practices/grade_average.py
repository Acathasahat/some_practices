#Use to store a math  grade of student and calculate the average grade
print('This code is used to store the math grades of students. and calculat the average.')
d = input('Now,lets go.')


    
students_grade = {}
#print(f'The grades: {students_grade}\n')
while True:
    name = input(f'Enter a name (or \'done\' when finished): ')
    if name.lower() == 'done':
        reassure = input(f'Are you done with all students\' names and grades? (Yes/No): ')
        if reassure.lower() == 'yes' or reassure.lower() == 'y':
            result = input(f'Now let me show you the average of the result.\n')
            break
        else:
            name = name
            
    while True:
        try:
            grade = float(input(f'Enter the grade of {name}: '))
            break
        except ValueError:
            print(f'It\'s not a valid grade of {name}.')
            continue
    students_grade[name] = grade
    print(f'The grades so far: {students_grade}\n')
    
if len(students_grade) > 0:
    tot_grade = sum(students_grade.values())#sum up all the grades
    print(f'The grades: {students_grade}')
    print(f'The sum of math grade: {tot_grade}')
    average = tot_grade / len(students_grade)
    print(f'The average grade of math: {average}')
  
else:
    print('No grades entered.')
    
godbye = input(f'Good bye! Press Enter to exit.')
        

    