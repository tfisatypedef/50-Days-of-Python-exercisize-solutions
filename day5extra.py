students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

plo = 0
pla = 0
for student in students:
    if student.lower() == "male":
        plo = plo + 1
        
    elif student.lower() == "female":
        pla = pla + 1


tup1 = ('Male', plo)
tup2 = ('female,', pla)
li1 = [tup1, tup2]
print(li1)