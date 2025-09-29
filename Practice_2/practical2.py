

# List Comprehension

cohort_1 = ['Schivanee', 'Saranya', 'Aiman', 'Ilia', 'Daveraj', 'Panya', 'Bryan', 'Abdul', 'Jibril', 'Maksym', 'Ano']
better_cohort_1 = [person for person in cohort_1 if len(person) % 2 != 0]

print(better_cohort_1)

# Unicode Characters

emoji = '\u2728'

cohort_1 = ['Schivanee', 'Saranya', 'Aiman', 'Ilia', 'Daveraj', 'Panya', 'Bryan', 'Abdul', 'Jibril', 'Maksym', 'Ano']
better_cohort = [name + emoji for name in cohort_1 if len(name) % 2 != 0 ]
print(better_cohort)

# String slicing
name = "Saranya"
extract = name[3:]
new_name = "P" + extract
print(new_name)

#String method
print(name.find('a'))
print(name.replace('Sar', 'P'))
