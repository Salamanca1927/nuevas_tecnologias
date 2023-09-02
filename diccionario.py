# Lista de asignaturas por semestre
semestre_1 = ["Lógica de progrmación", "Bases de datos", "Diseño web"]
semestre_2 = ["Bases de datos 2", "Programación web", "Web para dummies"]
semestre_3 = ["Programación", "Nuevas Tecnologías", "Web 2"]

# Agregar la materia "Diseño" en la cuarta posición del segundo semestre
semestre_2.insert(3, "Diseño")

# Agregar la materia "Historia del Color" al final del tercer semestre
semestre_3.append("Historia del Color")

# Lista de todos los semestres
asignaturas_por_semestre = [semestre_1, semestre_2, semestre_3]

# Función para imprimir las asignaturas en mayúsculas y ordenadas de Z a A
def imprimir_asignaturas_ordenadas(semestre):
    asignaturas_ordenadas = sorted(semestre, reverse=True)
    for asignatura in asignaturas_ordenadas:
        print(asignatura.upper())

# Imprimir las asignaturas de cada semestre en mayúsculas y ordenadas de Z a A
for semestre in asignaturas_por_semestre:
    print("Asignaturas del semestre:")
    imprimir_asignaturas_ordenadas(semestre)
    print()



