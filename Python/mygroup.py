groupmates = [
{
"name": "Платон",
"surname": "Ильин",
"exams": ["Информатика", "ЭЭиС", "Web"],
"marks": [5, 3, 5]
},
{
 "name": "Роман",
 "surname": "Дроздов",
 "exams": ["Философия", "Матан", "Ин.яз"],
 "marks": [3, 2, 3]
},
{
"name": "Аркадий",
"surname": "Киселёв",
"exams": ["Философия", "ИС", "КТП"],
"marks": [4, 3, 3]
},
{
"name": "Александра",
"surname": "Белоусова",
"exams": ["История", "ИС", "КТП"],
"marks": [3, 5, 4]
},
{
"name": "Денис",
"surname": "Яковлев",
"exams": ["Философия", "Web", "ИС"],
"marks": [3, 3, 3]
},
{
"name": "Людмила",
"surname": "Иванова",
"exams": ["Философия", "Web", "ИС"],
"marks": [5, 5, 5]
}
]
#print(groupmates)

filtr =int(input('Введите средний балл'))

def func(filtr):
	for i in range(len(groupmates)):
		student = groupmates[i]
		marks = student['marks']
		s =int((marks[0] + marks[1] + marks[2])/3)
		if s >= filtr :
			print (student['name'],student['surname'])
u = func(filtr)
print(u)




