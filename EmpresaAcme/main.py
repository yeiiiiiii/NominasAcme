import time
from modulos.registros import*
from modulos.nomina import*

print('\n****************************************************')
print('***************** EMPRESA ACME *********************')
print('****************************************************')
def menu():
    while True:
        print('_____________________MENÚ _______________________')
        time.sleep(0.9)
        print('\n1. Registro de empleados\n'
              '2. Registro de inasistencia\n'
              '3. Registro de bonos extra-legales\n'
              '4. Calcular nomina\n'
              '5. Salir')
        print('Escoge una opción:')
        opcion = int(input())
        
        if opcion == 1:
            Registros()
        elif opcion == 2:
            RegistroInasistencia()
        elif opcion == 3:
            RegistroBonos()     
        elif opcion == 4:
            CalcularNomina()  
        elif opcion == 5:
            print('Hasta luego...')
            time.sleep(1.3)
            print('Vuelve pronto ♥')
            break
        else:
            time.sleep(1.3)
            print('Opción no permitida, es del 1 al 5, gracias ✨')
menu()
