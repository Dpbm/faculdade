def more_than_six(grades):
    for student in grades:
        data = student.split()
        if(len(data[1:]) >= 6):
            print(data[0])
        
def students_grades_average(grades):

    grades_average = lambda grades : sum(grades) / len(grades)

    for student in grades:
        data = student.split()
        
        name = data[0]
        grades = list(map(int, data[1:]))
        average = grades_average(grades)

        print(f"{name} tem a média {average}")



def students_min_and_max_grade(grades):

    for student in grades:
        data = student.split()
        
        name = data[0]
        grades = list(map(int, data[1:]))

        min_grade = min(grades)
        max_grade = max(grades)

        print(f"{name} tem a nota minima {min_grade} e a máxima de {max_grade}")




if __name__ == "__main__":
    with open("notas_estudantes.txt", "r") as arq:
        data = list(map(lambda x: x.replace('\n', ''), arq.readlines()))

        print("Alunos com mais de seis notas")
        more_than_six(data)

        print("\nMédia de cada aluno")
        students_grades_average(data)

        print("\nNota máxima e minima de cada aluno")
        students_min_and_max_grade(data)

