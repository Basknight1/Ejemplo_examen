import funciones as fn

alumnos = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
           "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
creditos_alumnos = {}

while True:
    try:
        print("SISTEMA DE GESTIÓN DE CRÉDITOS ESTUDIANTILES AWS.")
        print("\n¿QUÉ NECESITA HACER?\n0. Inicializar Créditos.\n1. Asignar Créditos.\n2. Clasificar Créditos.\n3. Cálculo de Estadísticas de Créditos.\n4. Generar Reporte CSV.\n5. Salir del Sistema.")
        opc = int(input("Ingrese una opción: "))

        if opc == 0:
            creditos_alumnos = {alumno: 0 for alumno in alumnos}
            print("Créditos Inicializados correctamente.")

        elif opc == 1:
            if not creditos_alumnos:
                print("Primero debe Inicializar los Créditos.")
            else:
                creditos_alumnos = fn.asignar_creditos(alumnos)

        elif opc == 2:
            if creditos_alumnos:
                fn.clasificar_estadisticas(creditos_alumnos)
            else:
                print("Primero debe asignar Créditos.")

        elif opc == 3:
            if creditos_alumnos:
                max_credito, min_credito, promedio_credito = fn.calcular_creditos(
                    creditos_alumnos)
                if max_credito is not None:
                    print("Crédito máximo: ", max_credito)
                    print("Crédito mínimo: ", min_credito)
                    print("Promedio de Créditos: ", promedio_credito)
            else:
                print("Primero debe asignar Créditos.")

        elif opc == 4:
            if creditos_alumnos:
                fn.generar_reporte(creditos_alumnos)
            else:
                print("Primero debe ingresar los créditos.")

        elif opc == 5:
            print("Saliendo del Sistema...")
            break
        else:
            print("Opción no válida, por favor ingrese una opción entre 0 y 5.")
    except ValueError:
        print("Ingrese solo números.")
