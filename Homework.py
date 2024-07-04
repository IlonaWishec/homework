grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 4, 3], [5, 5, 5, 4, 5]] #Cписок
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #Множество
grades0 = sum(grades[0])/len(grades[0])
print(grades0) #Среднее арифметическое 4.0
grades1 = sum(grades[1])/len(grades[1])
print(grades1) #Среднее арифметическое 2.25
grades2 = sum(grades[2])/len(grades[2])
print(grades2) #Среднее арифметическое 3.6666666666666665
grades3 = sum(grades[3])/len(grades[3])
print(grades3) #Среднее арифметическое 4.8
students1 = list(students)
print(students1) #['Steve', 'Aaron', 'Khendrik', 'Johnny', 'Bilbo']
students1.sort()
print(students1) #['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
pupls = {students1[0]: grades0, students1[1]: grades1, students1[2]: grades2, students1[3]: grades3}
print(pupls) #{'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 3.6666666666666665, 'Khendrik': 4.8}
