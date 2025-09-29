#Data types

#int
group_number = 4

#string
name = "Saranya"

#float
pi = 3.14

#boolean
comparison = (group_number == pi)

#list
group_members = ['Schivanee', 'Saranya']

#set
country_names = {'Spain', 'Sweden'}
mixed_set = {1, 3.14, "Spain", True, (1, 2)}

#dictionary
person = {'Name': 'Saranya', 'Age': 55}

#tuple
cohort_1 = ('Schivanee', 'Saranya', 'Aiman', 'Ilia', 'Daveraj', 'Panya', 'Bryan', 'Abdul', 'Jibril', 'Maksym', 'Ano')
print(len(cohort_1) == 11)


#Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def elevator_pitch(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old.")

person1 = Person('Saranya', 55)
person1.elevator_pitch()