import csv
import random


def asignar_creditos(alumnos):  # 1
    credito_alumnos = {}
    for alumno in alumnos:
        credito = random.randint(50, 200)
        credito_alumnos[alumno] = credito
    print("Créditos aleatorios asignados correctamente.")
    print(credito_alumnos)

    return credito_alumnos


def clasificar_estadisticas(creditos_alumnos):  # 2
    menor_100 = {}
    entre_100_150 = {}
    mayor_150 = {}

    for alumno, credito in creditos_alumnos.items():
        if credito < 100:
            menor_100[alumno] = credito
        elif credito <= 150:
            entre_100_150[alumno] = credito
        else:
            mayor_150[alumno] = credito
    print("Créditos menores a 100, Total: ", len(menor_100))
    for alumno, credito in menor_100.items():
        print(alumno, ": $", credito)

    print("Créditos entre 100 y 150, Total: ", len(entre_100_150))
    for alumno, credito in entre_100_150.items():
        print(alumno, ": $", credito)

    print("Créditos mayores a 150, Total: ", len(mayor_150))
    for alumno, credito in mayor_150.items():
        print(alumno, ": $", credito)


def calcular_creditos(creditos_alumnos):  # 3
    creditos = list(creditos_alumnos.values())
    if not creditos:
        print("no se han asignado créditos aún.")
        return None, None, None

    max_credito = max(creditos)
    min_credito = min(creditos)
    promedio_credito = sum(creditos) / len(creditos)

    return max_credito, min_credito, promedio_credito


def generar_reporte(creditos_alumnos):  # 4
    with open('reporte_creditos', 'w', newline='') as archivo:
        escritor = csv.writer(archivo, delimiter=',')
        escritor.writerow(['Nombre', 'Crédito'])
        for alumno, credito in creditos_alumnos.items():
            escritor.writerow([alumno, credito])
