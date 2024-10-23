from modulos.validaciones import*

def Registros():
    print('\n*****************************************************')
    print('********************* REGISTROS ********************')
    print('****************************************************')

    empleados = DatosCargar()
    print('Por favor ingrese ID')
    ID = input()
    if validacion_EncontrarEmpleado(empleados, ID):
        print('El empleado ya se encuentra registrado')
        return
    
    print('Ingrese nombre')
    nombre = input()
    print('Cargo del empleado')
    cargo = input()
    
    while True:
        try:
            print('Ingrese el salario del empleado')
            salario = float(input())
            if salario < 0:
                raise ValueError("El salario no debe tener negativos")
            break
        except ValueError:
            print(f"Error Por favor no ingrese letras, gracias 😠")

    empleado = {
        'Identificacion': ID,
        'Nombre': nombre,
        'Cargo': cargo,
        'Salario': salario,
        'Inasistencias': [],
        'Bonos': []
    }

    empleados.append(empleado)
    DatosGuardar(empleados)
    print('***************************************')
    print('Empleado registrado exitosamente :)')
    print('***************************************')

def RegistroInasistencia():

    print('\n*****************************************************')
    print('****************** INASISTENCIA ********************')
    print('****************************************************')

    empleados = DatosCargar()
    print('Ingrese ID del empleado')
    ID = input()
    empleado = validacion_EncontrarEmpleado(empleados, ID)
    if not empleado:
        print('Lo siento, empleado no encontrado.')
        return
    print('Ingrese la fecha de la inasistencia (YYYY-MM-DD)')
    fecha = input()
    empleado['Inasistencias'].append(fecha)
    DatosGuardar(empleados)
    print('Inasistencia registrada correctamente')

def RegistroBonos():

    print('\n*****************************************************')
    print('********************* BONOS ************************')
    print('****************************************************')

    empleados = DatosCargar()
    print('Ingrese ID del empleado')
    ID = input()
    empleado = validacion_EncontrarEmpleado(empleados, ID)
    if not empleado:
        print('No se encontró el empleado.')
        return
    print('Ingrese el valor del bono')
    valor = float(input())
    empleado['Bonos'].append({'Valor': valor})
    DatosGuardar(empleados)

    print('**********************************')
    print('Bono registrado correctamente ♥')
    print('**********************************')