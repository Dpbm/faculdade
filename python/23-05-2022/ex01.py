from random import choice

alternatives = ("A", "B", "C", "D")

template = [ choice(alternatives) for i in range(10) ]


answers = [ [choice(alternatives)  for j in range(10)] for i in range(5)  ]

each_potuation = []

for student_answer in answers:

    pontuation = 0
    for answer in range(10):
        if(template[answer] == student_answer[answer]):
            pontuation += 1
    
    each_potuation.append( pontuation )


print(f"{'-'*4} gabarito {'-'*4}")
for i in template:
    print(i, end=" ")

print('\n\n')


for i in answers:
    for j in i:
        print(j, end=" ")
    print()
print()


print(f"{'-'*4} pontuacao {'-'*4}")
for i in each_potuation:
    print(i, end=" ")